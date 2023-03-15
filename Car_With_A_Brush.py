# possible improvement: if movement_coefficient > n, program gives wrong output. It can be solved using a third if condition contains "if movement_coefficient > n: ..." under if b == 1 section under str_list_input[str_list_input_index] == 5 or 6 sections

string_input = input("<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3. VEHICLE ROTATES RIGHT\n4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEV THE MATRIX\n0. EXIT\nPlease enter the commands with a plus sign (+) between them.\n")

str_list_input = string_input.split("+")

integer_map = map(int, str_list_input)
int_list_input = list(integer_map)

n = int_list_input[0]
arr = [['+' for i in range(n+2)] for j in range(n+2)]
emptyness = [' ' for k in range(n)]
for x in range(1,n+1):
    arr[x][1:-1] = emptyness
arr3 =arr.copy() #since I replaced some part of the list "arr" with the list "emptyness", if I didn't get a copy of the list "arr", I coldn't make operations with the list "arr", I would have to make operations with the list "emptyness" instead and that would make operations even more complex.
# arr3[3][2] = '*' #first [] indicates row, second [] indicates column

row = 1 #initial condition for array
column = 1 #initial condition for array
direction = 0 #initial condition for direction of the car(0-->right, 1-->below, 2-->left, 3-->above(mod4))
b = 2 # #initial condition for position of the brush

for str_list_input_index in range(1, len(str_list_input)):
    if str_list_input[str_list_input_index] == '1':
        b = 1
        old_row = (row)
        a = ['*' for k in range(1)]
        for x in range(old_row, old_row + 1):
            arr3[x][column:column + 1] = a
        arr4 = arr3.copy()
        arr3 = arr4.copy()
    elif str_list_input[str_list_input_index] == '2':
        b = 2
    elif str_list_input[str_list_input_index] == '3':
        direction = (direction + 1) % 4  # since there are 4 directions
    elif str_list_input[str_list_input_index] == '4':
        direction = (direction - 1) % 4  # since there are 4 directions
    elif str_list_input[str_list_input_index].startswith('5') == True:
        list_for_moving = str_list_input[str_list_input_index].split('_')
        moving_coefficient = int(list_for_moving[1])
        if direction == 0:
            old_column = (column + 1)
            if (column + moving_coefficient) == n:
                column = (column + moving_coefficient)
            else:
                column = (column + moving_coefficient) % n
            if b == 1:  # printing
                a = ['*' for k in range(1, moving_coefficient + 1)]
                if (n - old_column+1) > (moving_coefficient):
                    for x in range(row, row + 1):
                        arr3[x][old_column:column + 1] = a
                else:
                    for x in range(row, row + 1):
                        arr3[x][old_column:n + 1] = a[0:n - old_column + 1]
                        arr3[x][1:moving_coefficient - (n - old_column)] = a[n - old_column + 1:moving_coefficient-(n-old_column)+1]
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        elif direction == 1:
            old_row = (row+1)
            if (row + moving_coefficient) == n:
                row = (row + moving_coefficient)
            else:
                row = (row + moving_coefficient) % n
            if b == 1:  # printing
                a = ['*' for k in range(1)]
                if (n - old_row+2) > moving_coefficient:
                    for x in range(old_row, old_row + moving_coefficient):
                        arr3[x][column:column + 1] = a
                else:
                    for x in range(old_row, n + 1):
                        arr3[x][column:column + 1] = a
                    for x in range(1, moving_coefficient - (n - old_row)):
                        arr3[x][column:column + 1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        elif direction == 2:
            old_column = (column-1)
            if (column - moving_coefficient) == n:
                column = (column - moving_coefficient)
            else:
                column = (column - moving_coefficient) % n
            if b == 1:  # printing
                a = ['*' for k in range(1, moving_coefficient +1 )]
                if (old_column) > (moving_coefficient):
                    for x in range(row, row + 1):
                        arr3[x][column:old_column+1] = a
                else:
                    for x in range(row, row + 1):
                        arr3[x][1:old_column + 1] = a[0:old_column]
                        arr3[x][n - (moving_coefficient - old_column) + 1:n + 1] = a[old_column:moving_coefficient]
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        else:  # direction == 3 condition
            old_row = (row)
            if (row - moving_coefficient) == n:
                row = (row - moving_coefficient)
            else:
                row = (row - moving_coefficient) % n
            if b == 1:  # printing
                a = ['*' for k in range(1)]

                if (old_row - 1) > moving_coefficient:
                    for x in range(row, old_row):
                        arr3[x][column:column + 1] = a
                else:
                    for x in range(1, old_row):
                        arr3[x][column:column + 1] = a
                    for x in range(n - (moving_coefficient - old_row + 1) + 1,
                                   n + 1):
                        arr3[x][column:column + 1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
    elif str_list_input[str_list_input_index] == '6': #jumping
        if direction == 0:
            old_column = (column+1)
            column = (column + 3 ) % n  # since 3 is the constant jumping distance
            if b == 7:
                a = ['*' for k in range(1, 3 + 1)]
                for x in range(row, row + 1):
                    arr3[x][old_column:column+1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        elif direction == 1:
            old_row = (row +1)
            row = (row + 3 ) % n  # since 3 is the constant jumping distance
            if b == 7:
                a = ['*' for k in range(1)]
                for x in range(old_row, row+1):
                    arr3[x][column:column + 1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        elif direction == 2:
            old_column = (column-1)
            column = (column - 3) % n  # since 3 is the constant jumping distance
            if b == 7:
                a = ['*' for k in range(1, 3 + 1 )]
                for x in range(row, row + 1):
                    arr3[x][column:old_column+1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        else:  # direction == 3 condition
            old_row = (row)
            row = (row - 3) % n  # since 3 is the constant jumping distance
            if b == 7:
                a = ['*' for k in range(1)]
                for x in range(row, old_row):
                    arr3[x][column:column + 1] = a
                arr4 = arr3.copy()
                arr3 = arr4.copy()
        b = 2
    elif str_list_input[str_list_input_index] == '7':
        direction = (direction + 2) % 4  # since there are 4 directions
    elif str_list_input[str_list_input_index] == '8':
        for row in arr3:
            print(*row)
    elif str_list_input[str_list_input_index] == '0':
        break
    else:
        print("You entered an incorrect command. Please try again!")
        break