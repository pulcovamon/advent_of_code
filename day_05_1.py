'''
Advent calendar day 05 task 1
'''


def day_05_1(stacks_file, moves_file):
    with open(stacks_file) as stacks_txt:
        lines = stacks_txt.readlines()

        stacks = []

        for i in range(len(lines)-1, -1, -1):
            for j in range(len(lines[-1])):
                if lines[i][j].isdigit():
                    stacks.append([lines[i][j]])
                elif lines[i][j].isalpha():
                    my_index = [char for sublist in stacks
                        for char in sublist if char == lines[-1][j]]
                    my_index = int(my_index[0]) - 1
                    stacks[my_index].append(lines[i][j])

    with open(moves_file) as moves_txt:
        lines = moves_txt.readlines()

        for line in lines:
            indices = [int(char) for char in line.split() if char.isdigit()]
            index_1 = indices[1] - 1
            index_2 = indices[2] - 1
            number = indices[0]

            for i in range(number):
                item = stacks[index_1].pop()
                stacks[index_2].append(item)

    mess = ''

    for sublist in stacks:
        mess += sublist.pop()


    return(mess)



if __name__ == '__main__':
    print(day_05_1('data_05_1.txt', 'data_05_2.txt'))