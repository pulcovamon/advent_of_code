'''
try of last year
'''
from copy import deepcopy
from time import sleep

def moving_cucumbers(file_name):
    with open(file_name) as txt_file:
        lines = txt_file.readlines()

        for i in range(len(lines)):
            lines[i] = [j for j in lines[i] if j != '\n']

        lines_new = deepcopy(lines)
        lines_new_2 = deepcopy(lines)
        number = 0
            
    while True:
        number += 1
        move = False

        for i in range(len(lines)):
            for j in range(len(lines[i])):

                if j < len(lines[i]) - 1:
                    if lines[i][j] == '>' and lines[i][j+1] == '.':
                        lines_new[i][j] = '.'
                        lines_new[i][j+1] = '>'
                        move = True
                        
                elif lines[i][j] == '>' and lines[i][0] == '.':
                    lines_new[i][j] = '.'
                    lines_new[i][0] = '>'
                    move = True

        lines_new_2 = deepcopy(lines_new)

        for i in range(len(lines)):
            for j in range(len(lines[i])):

                if i < len(lines_new) - 1:
                    if lines_new[i][j] == 'v' and lines_new[i+1][j] == '.':
                        lines_new_2[i][j] = '.'
                        lines_new_2[i+1][j] = 'v'
                        move = True

                elif lines_new[i][j] == 'v' and lines_new[0][j] == '.':
                    lines_new_2[i][j] = '.'
                    lines_new_2[0][j] = 'v'
                    move = True

        lines = deepcopy(lines_new_2)
        lines_new = deepcopy(lines_new_2)

        if not move:
            break

    return number







if __name__ == '__main__':
    print(moving_cucumbers('data_last_year.txt'))