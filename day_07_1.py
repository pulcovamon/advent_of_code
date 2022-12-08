'''
Advent calendar day 07 task 1 (does not work)
'''

def day_07_1(file_name):
    with open(file_name) as txt_file:
        lines = txt_file.readlines()

        directories = {}
        file_system = []
        ls = False

        for i in range(len(lines)):
            if lines[i].strip() == '$ ls':
                ls = True
            elif lines[i][0:4].strip() == '$ cd':
                ls = False
                if lines[i][5:-1] != '..':
                    name_dir = ''.join(lines[i][5:-1]).strip()
                    file_system.append(name_dir)
                    directories[name_dir] = []
                else:
                    file_system.pop()
            elif ls:
                name = lines[i].strip()
                directories[name_dir].append(name)

        del directories['/']
            

        sizes = {}
        complete = False

        while not complete:
            complete = True
            for directory in directories:
                sizes[directory] = 0
                for item in directories[directory]:
                    if item[0:3] == 'dir':
                        if item[4] in sizes:
                            print(item[4])
                            sizes[directory] += sizes[item[4]]
                        else:
                            complete = False
                    else:
                        size = int(''.join([char for char in item if char.isdigit()]))
                        sizes[directory] += size


    return sizes




if __name__ == '__main__':
    print(day_07_1('data_07.txt'))
