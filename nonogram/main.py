list_A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

solution = [[2, 2, 2, 2, 2, 2, 1, 1, 1, 2], [2, 2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 1, 2, 2, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 1, 1], [2, 2, 2, 2, 2, 2, 2, 1, 1, 1], [1, 1, 2, 1, 1, 2, 2, 2, 1, 1], [2, 1, 2, 2, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

list_B = [[3], [5] , [1,2], [2], [2], [3], [2, 2, 2], [1, 4], [9], [1, 1, 1, 1, 1]]

list_C = [[0, 1, 1], [0, 0, 4], [0, 0, 1], [0, 1, 2], [0, 0, 3], [0, 2, 3], [0, 2, 2], [2, 1, 3], [0, 7, 1], [0, 6, 1]]

# This loop finds the longest list
max_len = 0                
for i in list_B:
  if len(i) > max_len:
    max_len = len(i)

for j in list_C:
  if len(j) > max_len:
    max_len = len(j)

extra_space = " " * (max_len - 1)
row_size = 10
col_size = 10


def print_board():
  for i in range(len(list_C[0])):   
    list_C_row = "  " + (extra_space)
    for j in range(len(list_C)):   
            # j 0 1 2 3 4 5 6 7 8 9
            # i 0 1 2
      if (list_C[j][i] == 0):
        list_C_row += "  "
      else:
        list_C_row += str(list_C[j][i]) + " "

    print(list_C_row)


  for i in range(row_size):
    row = ""

  for i in range(len(list_B)):
    row = ""
    print(extra_space + "  - - - - - - - - - -")
    add_space = max_len - len(list_B[i])
    for j in range(add_space):
      row += " "    
    for b in list_B[i]:
      row += str(b)
    
    for j in range(col_size):
      if list_A[i][j] == 0:
        row += ("|" + " ")
      if list_A[i][j] == 1:
        row += ("|" + "x")
      if list_A[i][j] == 2:
        row += ("|" + "-")

    row += "|"
    print(row)

  print(extra_space + "  - - - - - - - - - - ")

def main():
  life = 3

  empty = 0
  filled = 1
  cross = 2
  while True:
    # Check if life is equal to 0
    if life == 0:
      print("You lost!")
      break

    # Check if list A is equal to solution
    if list_A == solution:
      print("You won!")
      break
    
    print_board()

    user_extra = input("Do you want to cross(C) or fill(F)? ")

    if user_extra == "C":
      user_row = int(input("Which row? ")) - 1
      user_col = int(input("Which column? ")) - 1
      if solution[user_row][user_col] == 2:
        list_A[user_row][user_col] = cross
      else:
        life -= 1
        print("You lost a life! ")
    elif user_extra == "F":
      user_row = int(input("Which row?")) - 1
      user_col = int(input("Which column?")) - 1
      if solution[user_row][user_col] == 1:
        list_A[user_row][user_col] = filled
      else:
        life -= 1
        print("You lost a life! ")

main()