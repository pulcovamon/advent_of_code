'''
Advent calendar day 6 task 1
'''



def day_06_1(file_name):
    with open(file_name) as my_input:
        text = my_input.readline()

        for i in range(3, len(text)):

            letters = set(text[i-3:i+1])

            if len(letters) == 4:
                index = i+1
                break

    return index

if __name__ == '__main__':
    print(day_06_1('data_06.txt'))