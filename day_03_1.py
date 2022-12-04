'''
Advent calendar day 01 task 02
'''

def day_03_1(file_name):

    with open(file_name) as txt_file:
        lines = txt_file.readlines()
        letters = []
        priority_sum = 0

        for line in lines:
            length = int(len(line) / 2)
            compartment_1 = line[0:length]
            compartment_2 = line[length:-1]
            
            for letter in compartment_1:
                if letter in compartment_2:
                    letters.append(letter)

                    if letter.islower():
                        priority = ord(letter) - 96
                    elif letter.upper():
                        priority = ord(letter) - 64 + 26

                    priority_sum = priority_sum + priority
                    break

    print(len(letters), len(lines))

    return priority_sum



if __name__ == '__main__':
    print(day_03_1('data_03.txt'))