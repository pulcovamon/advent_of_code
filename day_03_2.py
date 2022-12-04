'''
Advent calendar day 01 task 02
'''

def day_03_1(file_name):

    with open(file_name) as txt_file:
        lines = txt_file.readlines()
        letters = []
        priority_sum = 0

        for i in range(0, len(lines,) - 2, 3):
            
            for letter in lines[i]:
                if letter in lines[i+1] and letter in lines[i+2]:
                    letters.append(letter)

                    if letter.islower():
                        priority = ord(letter) - 96
                    elif letter.upper():
                        priority = ord(letter) - 64 + 26

                    priority_sum = priority_sum + priority
                    break

    print(len(letters), len(lines))

    return priority_sum

def with_sets(file_name):

    with open(file_name) as txt_file:
        lines = txt_file.readlines()
        priority_sum = 0

        for i in range(0, len(lines,) - 2, 3):
            line_1 = set(lines[i].strip())
            line_2 = set(lines[i+1].strip())
            line_3 = set(lines[i+2].strip())

            letter = ''.join(line_1.intersection(line_2.intersection(line_3)))

            if letter.islower():
                priority = ord(letter) - 96
            elif letter.upper():
                priority = ord(letter) - 64 + 26

            priority_sum = priority_sum + priority

    return priority_sum



if __name__ == '__main__':
    print(day_03_1('data_03.txt'))
    print(with_sets('data_03.txt'))