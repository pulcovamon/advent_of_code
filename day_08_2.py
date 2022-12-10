'''
Advent calendar day 08 task 2
'''
import numpy as np


def visible_trees(file_name):
    with open(file_name) as tree_file:
        trees = tree_file.readlines()
        trees = [[int(j) for j in i if j.isdigit()] for i in trees]
        trees = np.array(trees, dtype=int)

        score = 0

    for i in range(1, trees.shape[0]-1):
        for j in range(1, trees.shape[1]-1):

            right = 0
            left = 0
            top = 0
            down = 0

            k = i+1
            while k < trees.shape[0]:
                down += 1
                if trees[k, j] >= trees[i, j]:
                    break
                k += 1

            k = i-1
            while k >= 0:
                top += 1
                if trees[k, j] >= trees[i, j]:
                    break
                k -= 1

            k = j-1
            while k >= 0:
                left += 1
                if trees[i, k] >= trees[i, j]:
                    break
                k -= 1
            
            k = j+1
            while k < trees.shape[1]:
                right += 1
                if trees[i, k] >= trees[i, j]:
                    break
                k += 1


            current_score =  right * left * top * down
            #print('i' ,i, 'j' ,j, 'tree' ,trees[i, j], 'r' ,right, 'l' ,left, 't' ,top, 'd' ,down, 'score' ,current_score)

            if current_score > score:
                score = current_score


    return score






if __name__ == '__main__':
    print(visible_trees('data_08.txt'))