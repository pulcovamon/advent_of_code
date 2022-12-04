'''
Advent calendar day 01 task 02
'''

def day_01_1(file_name):

    with open(file_name) as txt_file:

        sum_calories = 0
        max_calories = [0, 0, 0]

        for line in txt_file:
            if line != '\n':
                sum_calories = sum_calories + int(line)
            else:
                for i in range(len(max_calories)):
                    if sum_calories > max_calories[i]:
                        max_calories.pop(i)
                        max_calories.append(sum_calories)
                        break

                sum_calories = 0
                max_3 = sum(max_calories)

    return max_3


if __name__ == '__main__':
    
    print(day_01_1('data.txt'))