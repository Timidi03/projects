arr = []
matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 1, 1, 2, 1, 3, 1, 4, 1],
          [5, 1, 6, 1, 7, 1, 8, 1, 9]]

print('Добро пожаловать в игру "19 - чиселки"  !')

def print_matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def add_to_arr():
    arr.clear()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '*':
                arr.append(matrix[i][j])

def check_coordinates():
    if coordinate1[0] > len(matrix) or coordinate1[1] > len(matrix[coordinate1[0]]) or \
            coordinate2[0] > len(matrix) or coordinate2[1] > len(matrix[coordinate2[0]]):
        print('Неверно указаны номер строки или столбца. Повторите ввод:')
    else:
        if (matrix[coordinate1[0] - 1][coordinate1[1] - 1] == matrix[coordinate2[0] - 1][coordinate2[1] - 1] or (
             matrix[coordinate1[0] - 1][coordinate1[1] - 1] + matrix[coordinate2[0] - 1][coordinate2[1] - 1]) == 10) and \
                coordinate1 != coordinate2:
            matrix[coordinate1[0] - 1][coordinate1[1] - 1] = '*'
            matrix[coordinate2[0] - 1][coordinate2[1] - 1] = '*'
            print_matrix()
        else:
            print('Неверные координаты! Повторите ввод:')

print_matrix()
print("Если в матрице не осталось больше подходящих цифр по условию нажмите 2 раза Enter")
while True:
    while True:
        coordinate1 = [int(i) for i in input("Введите координаты первого числа через пробел (сначала номер строки, затем номер столбца)").split()]
        coordinate2 = [int(i) for i in input("Введите координаты второго числа через пробел (сначала номер строки, затем номер столбца)").split()]

        if coordinate2 and coordinate1 != []:
            check_coordinates()
        else:
            break
    add_to_arr()
    count = 0
    for i in arr:
        if i != '*':
            count += 1
    if count > 9:
        if len(matrix[-1]) < 9:
            matrix[-1] += [arr[a] for a in range(9-len(matrix[-1]))]
            if count % 9 != 0:
                for _ in range(count//9):
                    matrix += [[arr[a] for a in range(9)]]
                    del arr[:9]
                matrix += [[arr[a] for a in range(count % 9)]]
            else:
                for _ in range(count//9):
                    matrix += [[arr[a] for a in range(9)]]
                    del arr[:9]
        else:
            if count % 9 != 0:
                for _ in range(count//9):
                    matrix += [[arr[a] for a in range(9)]]
                    del arr[:9]
                matrix += [[arr[a] for a in range(count % 9)]]
            else:
                for _ in range(count//9):
                    matrix += [[arr[a] for a in range(9)]]
                    del arr[:9]
        for i in range(len(matrix)):
            if matrix[i] == ['*'] * 9:
                del matrix[i]
    print_matrix()
