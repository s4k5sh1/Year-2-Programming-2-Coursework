
def load(filename):

 # error message thrown for wrong file format or file that cant be open
    try:
        if filename.endswith(".fna"):
            file = open(filename,"r")
    except (FileNotFoundError, IOError) as e:
        description = "file was not loaded"
        sequence = []

        return description, sequence

    with open(filename,'r') as file:
        header = file.readline().rstrip().lstrip()
        if header.startswith(">"):
            description = header.replace(">","")

            sequence = []
            line = file.readline().rstrip()
 # all alpha-numeric characters (not whitespace/empty elements) are trasnferred to sequence
            while line != "":
                sequence += line
                line = file.readline().rstrip()
                # convert lower case to upper case
                sequence = [x.upper() for x in sequence]


            return  sequence, description



def stats(sequence):

# set a dictionary with 18 enteries
    table = {"A": 0,"C": 0,"G": 0, "T":0
              ,"N": 0, "U":0,"K":0,"S":0,"Y":0
              ,"M":0,"W":0,"R":0,"B":0
              ,"D":0,"H":0,"V":0
             ,"-":0,"other":0}
# for values present in sequence increase count by 1 for each iteration
    for nucleic_acid_codes in sequence:
        table[nucleic_acid_codes] = table[nucleic_acid_codes] + 1

    return table



def format_sequence(sequence,first_index,last_index):

    last_index += 1
# return a string by joining all elements of list
    str_subsequence = "".join(sequence[first_index:last_index])
    formatted_sequences = []
# incrementation as 80 to group together 80 nucleic acid codes
    for x in range(0, len(str_subsequence), 80):
        formatted_sequences.append(str_subsequence[x : x + 80])

    return formatted_sequences




def write(filename,description,sequence,first_index,last_index):

    with open(filename, 'w') as new_file:
        new_file.write(">" + description)
        new_list = sequence[first_index:last_index]
        format_new_list = "".join(new_list)
        new_file.write("\n" + format_new_list)




def find(sequence, sequence_to_find):

    matches = []
# loops for every single code present in sequence list
    for code in range(len(sequence)):
# check if triplet sequence to find matches every 3 codes in sequence list
        if sequence_to_find == sequence[code : code + 3]:
            matches.append(code)

    return matches





def add(sequence,sequence_to_add,index):

    for i in sequence:
# condition 1 : if input index is beyond sequence length
        if index > len(sequence):
            new_sequence = sequence[:index] + sequence[index:] + sequence_to_add
# condition 2: if input index is within sequnce length
        if index < len(sequence):
            new_sequence = sequence[:index] + sequence_to_add + sequence[index:]

    return  new_sequence




def delete(sequence,index,number_of_codes):

# define a stop index
    end_index = index + number_of_codes

    for i in sequence:
# condition 1 : if index and number_of_codes does not exceed sequence length
        if index and number_of_codes < len(sequence):
            new_sequence = sequence[:index] + sequence[end_index:]
# condition 2: if index and number_of_codes exceeds sequence length
        elif index and number_of_codes > len(sequence):
            new_sequence = sequence[:index]
# condition 3: if index exceeds sequence length
        elif index > len(sequence):
            pass

    return  new_sequence




def replace(sequence,sequence_to_add,index,number_of_codes):

# define a stop index
    final_index = index + number_of_codes

    for i in sequence:
# condition 1 : if index and number_of_codes does not exceed sequence length
        if index and number_of_codes < len(sequence):
            new_sequence = sequence[:index] + sequence_to_add + sequence[final_index:]
# condition 2: if index and number_of_codes exceeds sequence length
        elif index and number_of_codes > len(sequence):
            new_sequence = sequence[:index]
# condition 3: if index exceeds sequence length
        elif index > len(sequence):
            new_sequence = sequence[:index] + sequence[final_index:] + sequence_to_add

    return  new_sequence




def dna2protein(dna_sequence):
    # opening and reading csv file
    with open('dna2protein.csv', 'r') as dna_file:
        line = dna_file.readline()

        dna2protein_list = list()
        while line:
            # converting every row within csv file to a list within a list (nested list)
            dna2protein_list.append(line.strip().split(","))
            line = dna_file.readline()

            protein_sequence = []
            # step as 3 to read code as a triplet
            for i in range(0, len(dna_sequence), 3):
                # new list which contains triplet code as list element
                dna_seq_code = [dna_sequence[i], dna_sequence[i + 1], dna_sequence[i + 2]]
                #  check if the triplet in dna_sequence matches the triplet code in dna2protein_list before for loop
                # if final for loop is completed and triplet code doesnt match, jumps to line with if not
                code_deciphered = False
                # row defines the list within the main list
                for row in dna2protein_list:
                    dna2_code = [row[0], row[1], row[2]]
                    if dna_seq_code == dna2_code:
                        # if the two sequence match, appends the mepty list with single code for protein
                        protein_sequence.append(row[4])
                        code_deciphered = True
                        break
                if not code_deciphered:
                    # same as "if code_deciphered == False":
                    protein_sequence.append('?')

    # opening and reading csv file again before forming a dicitonary
    with open("dna2protein.csv", 'r') as dna_file:
        table = {}
        # read through each row in file and extract key (triplet) and value (protein code)
        for row in dna_file.readlines():
            protein = row[10]
            triplet = row[0:5].replace(",", "")
            # add a triplet key and assign it a protein value when dictionary is empty in the start
            if triplet not in table:
                table[triplet] = [protein]
            # if triplet already present in dicitonary, assign the triplet to the protein value
            elif triplet in table:
                table[triplet].append(triplet)
            # removing square brackets from the values(protein code)
            table = {key: value[0] for key, value in table.items()}
 # adding new key and values to exisiting dictionary
        table["???"] ="?"

        return protein_sequence, table




















































    




























































