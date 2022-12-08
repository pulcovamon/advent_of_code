'''
Advent calendar day 07 task 1 try 2
'''

class directory:
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.parent = None

    def add_directory(self, name_dir):
        directory.parent = self
        self.directories.append(name_dir)

    def print_directories(self):
        print(self.name)
        for name_dir in self.directories:
            name_dir.print_directories()


def file_system(file_name):
    with open(file_name) as throught_dir:
        steps = throught_dir.readlines()

        
    root = directory('Root')

    directory_1 = directory('directory 1')
    root.add_directory(directory_1)

    directory2 = directory('directory 2')
    directory_1.add_directory(directory2)

    return root


if __name__ == '__main__':
    root = file_system('data_07_1.py')
    root.print_directories()