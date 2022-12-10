'''
Advent calendar day 08 task 1
'''
import numpy as np


def visible_trees(file_name):
    with open(file_name) as tree_file:
        trees = tree_file.readlines()
        trees = [[int(j) for j in i if j.isdigit()] for i in trees]
        trees = np.array(trees, dtype=int)

        number = 0
    
    for i in range(1, trees.shape[0]-1):
        for j in range(1, trees.shape[1]-1):
            if max(trees[:i, j]) < trees[i, j]:
                number += 1
            elif max(trees[i, :j]) < trees[i, j]:
                number += 1
            elif max(trees[i+1:, j]) < trees[i, j]:
                number += 1
            elif max(trees[i, j+1:]) < trees[i, j]:
                number += 1

    number += 2*trees.shape[0] + 2*trees.shape[1]-4

    return number






if __name__ == '__main__':
    print(visible_trees('data_08.txt'))