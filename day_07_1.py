'''
Advent calendar day 07 task 1 try 2
'''
from collections import defaultdict


def file_system(file_name):
    with open(file_name) as throught_dir:
        steps = throught_dir.readlines()

        dir_dict = {}
        current_path = []
        

        for line in steps:
            line = line.strip().split()
            if line[1] == 'cd':
                if line[2] == '..':
                    current_path.pop()
                elif line[2] == '/':
                    name = 'root'
                    current_path = [name]
                    if name not in dir_dict:
                        dir_dict[name] = 0
                else:
                    name = '/'.join(current_path) + line[2]
                    current_path.append(name)
                    if name not in dir_dict:
                        dir_dict[name] = 0
            elif line[0].isdigit():
                file_size = int(line[0])
                for item in current_path:
                    dir_dict[item] += file_size

    keys = [key for key in dir_dict if dir_dict[key] <= 100000]
    sizes = [dir_dict[key] for key in keys]

    sum_sizes = sum(sizes)


    return sum_sizes




if __name__ == '__main__':
    print(file_system('data_07.txt'))