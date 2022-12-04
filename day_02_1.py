'''
Advent calendar day 01 task 02
'''

def day_02_1(file_name):

    with open(file_name) as txt_file:

        lines = txt_file.readlines()

        score = {'X': 1, 'Y': 2, 'Z': 3}
        definition =  {'A': 'X', 'B': 'Y', 'C': 'Z'}
        counter = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        my_score = 0

        for line in lines:

            my_score = my_score + score[line[2]]

            if counter[line[0]] == line[2]:
                my_score = my_score + 6

            if definition[line[0]] == line[2]:
                my_score = my_score + 3

    return my_score


if __name__ == '__main__':
    print(day_02_1('data_02.txt'))
