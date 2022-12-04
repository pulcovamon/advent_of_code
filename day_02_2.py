'''
Advent calendar day 01 task 02
'''

def day_02_1(file_name):

    with open(file_name) as txt_file:

        lines = txt_file.readlines()

        shape = {'A': [1, 'B', 'C'], 'B': [2, 'C', 'A'], 'C': [3, 'A', 'B']}  # score, counters, countered by

        my_score = 0

        for line in lines:
            score = 0

            if line[2] == 'Z':
                score = shape[shape[line[0]][1]][0] + 6
            elif line[2] == 'Y':
                score = shape[line[0]][0] + 3
            elif line[2] == 'X':
                score = shape[shape[line[0]][2]][0]

            my_score = my_score + score
 

    return my_score


if __name__ == '__main__':
    print(day_02_1('data_02.txt'))
