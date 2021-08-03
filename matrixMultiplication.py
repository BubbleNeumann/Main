class Matrix:

    def __init__(self, row = 2, col = 2, userInteractions = False):
        self.__row = row
        self.__col = col
        self.__content = []

        # filling the matrix
        if (userInteractions):
            for i in range(self.__row):
                strRow = input("Row no." + str(i) + ": ")
                intRow = strRow.split()
                self.__content.append(intRow);
        else:
            for i in range(self.__row):
                self.__content.append([])
                for j in range(self.__col):
                    self.__content[i].append(i + j)

    def multiply(self, multiplicand):

        # check if it is possible to multiply
        if (self.__col != multiplicand.__row): return 0

        product = Matrix(row = self.__row, col = multiplicand.__col)

        for i in range(product.__row):
            for j in range(product.__col):
                product.__content[i][j] = 0
                for k in range(self.__col):
                    product.__content[i][j] += self.__content[i][k] * multiplicand.__content[k][j]

        return product

    def printMatrix(self):
        for i in range(self.__row):
            print(self.__content[i])
            
first = Matrix()
second = Matrix()

result = first.multiply(second)

# print the result if possible
if (type(result) == type(first)):
    result.printMatrix()
else:
    print("Matrixes cannot be multiplied")
    
