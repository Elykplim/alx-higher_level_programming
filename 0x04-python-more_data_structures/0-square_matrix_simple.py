#!/usr/bin/python3

#def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
   # squared_matrix = []

    # Iterate over each row in the input matrix
    #for row in matrix:
        # Create a new row for the squared_matrix
     #   squared_row = []

        # Iterate over each element in the row and square it
       # for value in row:
           # squared_row.append(value ** 2)

        # Add the squared row to the squared_matrix
      #  squared_matrix.append(squared_row)

  #  return squared_matrix

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)


