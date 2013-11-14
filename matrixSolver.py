#Reduces a matrix to reduced row echelon form
def matrixSolver(height, width, matrix):
    from fractions import *

    #Solves row by row
    for row in range(height):
        operatingTerm = row *(width + 1)
        
        #Iterates through each row
        for layer in range(row, height):
            index = layer * width + row
            leadingCoefficient = matrix[index]
            if leadingCoefficient != 0:
                #Devides each column of a row by the leading coefficient
                for column in range(width - row):
                    currentIndex = index + column
                    matrix[currentIndex] = Fraction(matrix[currentIndex], leadingCoefficient)
            
        #Combines each row for row reduction
        for layer in range(height):
            index = layer * width
            if operatingTerm not in range(index, index + width - 1):
                commonMultiple = matrix[index + row]
                for column in range(width - row):
                    matrix[row + index + column] = (matrix[row + index + column] - commonMultiple * matrix[row *(width + 1)+ column])

    #Checks to see if there are no solutions to the system of equations
    for row in range(height):
        for column in range(width - 1):
            if row * width + column == row * width + width - 2 and matrix[row * width + column] == 0:
                if matrix[row * width + width-1] != 0:
                    matrix = []
                    return matrix
                break
            elif matrix[row * width + column] == 0:
                continue
            break
    for entry in range(len(matrix)):
        if matrix[entry].numerator % matrix[entry].denominator ==0:
            matrix[entry] = str(int(matrix[entry].numerator / matrix[entry].denominator))
        else:
            matrix[entry] = str(matrix[entry].numerator) + ("/") + str((matrix[entry].denominator))
        continue
    return matrix
