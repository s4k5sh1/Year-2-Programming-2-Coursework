import os
import time
import random
import copy


class Cell():

    def __init__(self, alive=False):


        self.alive = alive

    def set_dead(self):

        self.alive = False

    def set_alive(self):

        self.alive = True

    def _is_alive(self):
        if self.alive == True:
            return True
        return False



    def get_status(self):

        if self.alive == True:
            return 'O'
        return '.'

    def __str__(self):

        return self.get_status()

    def update_cell(self,table):
        if row in range(len(table)) and col in range(len(table[0])):
            return self.alive == True if table[row][col] else 0
        return 0

    
        





class Cancer(Cell):

    def __init__(self,alive = False):
        super().__init__(alive)

    def set_dead(self):

        self.alive = False

    def set_alive(self):

        self.alive = True


    def _is_alive(self):
        if self.alive == True:
            return True
        return False


    def get_status(self):
        if self.alive == True:
            return 'X'
        return '.'


    def __str__(self):
        return self.get_status()

    def update_cell(self,table):
        if row in range(len(table)) and col in range(len(table[0])):
            return self.alive == True if table[row][col] else 0
        return 0







class Tissue(Cell):

    def __init__(self,rows=1,cols=1,CellType=Cell):

        self.rows = rows
        self.cols = cols
        self.CellType = CellType
        self.matrix = list()
        for i in range(rows):
            self.matrix.append([CellType]*cols)

    def __str__(self):

        return '\n'.join(''.join(map(str, row)) for row in self.matrix)


    def __getitem__(self,item):

        return self.matrix[item]

    def __setitem__(self, item, new_item):

       self.matrix[item] = new_item


    def seed_from_matrix(self,array):

        self.matrix = array
        self.rows = len(array)
        self.cols = len(array[0])


    def seed_from_file(self,filename,CellType):

        file = open(filename, "r")
        self.matrix = [line.strip() for line in file.readlines()]
        file.close()


    def seed_random(self,con,cell):
        self.matrix = [[cell() for column_cells in range(self.cols)] for row_cells in range(self.rows)]
        for row in self.matrix:
            for column in row:
                chance_number = random.random() < con
                if chance_number:
                    column.set_alive()

        return sef.matrix


    def neighbour_cells(self,table):
        sum = 0
    for row_shift in (-1, 0, 1):
        for col_shift in (-1, 0, 1):
            if row_shift or col_shift:
                #  checking for funcion to not check the state of the cell itself
                sum += get_cell_state(table, row + row_shift, col + col_shift)
    return sum


    def update_table(table, height, width):
     new_table = copy.deepcopy(table)  # deep copy to avoid mutability issues
     for row in range(height):
        for col in range(width):
            neighboring_cells = get_neighboring_cells(table, row, col)
            if neighboring_cells < 2 and table[row][col]:
                # underpopulation
                new_table[row][col] = False
            elif neighboring_cells > 3 and table[row][col]:
                # overpopulation
                new_table[row][col] = False
            elif neighboring_cells == 3 and not table[row][col]:
                # replication
                new_table[row][col] = True
    return new_table




        
    



    


 



























































