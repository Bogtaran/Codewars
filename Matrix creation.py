'''
Создайте идентификационную матрицу указанного размера ( >= 0).

Несколько примеров:

(1)  =>  [[1]]

(2) => [ [1,0],
         [0,1] ]

       [ [1,0,0,0,0],
         [0,1,0,0,0],
(5) =>   [0,0,1,0,0],
         [0,0,0,1,0],
         [0,0,0,0,1] ]
'''

def get_matrix(n):
    a_list = [0] * n
    for i in range(n):
        a_list[i] = [0] * n
    for i in range(len(a_list)):
        j = i
        a_list[i][j] = 1
    return a_list

if __name__ == '__main__':
    print(get_matrix(4))
