'''
Advent calendar day 01 task 01
'''

def day_01_1(file_name):

    with open(file_name) as txt_file:

        sum_calories = 0
        max_calories = 0

        for line in txt_file:
            if line != '\n':
                sum_calories = sum_calories + int(line)
            else:
                if sum_calories > max_calories:
                    max_calories = sum_calories
                sum_calories = 0

    return max_calories


if __name__ == '__main__':
    
    print(day_01_1('data.txt'))