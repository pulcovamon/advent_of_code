'''
advent calendar task for day 4 task 1
'''
import re

def day_04_1(file_name):

    with open(file_name) as txt_file:
        lines = txt_file.readlines()
        number = 0

        for i in range(len(lines)):
            low_1 = re.search('^[0-9]+', lines[i]).group(0)
            high_1 = re.search('-([0-9]+),', lines[i]).group(1)
            low_2 = re.search(',([0-9]+)-', lines[i]).group(1)
            high_2 = re.search('[0-9]+$', lines[i]).group(0)

            if (int(low_1) <= int(low_2) and int(high_1) >= int(high_2)) or (int(low_1) >= int(low_2) and int(high_1) <= int(high_2)):
                number += 1


    return number








if __name__ == '__main__':
    print(day_04_1('data_04.txt'))