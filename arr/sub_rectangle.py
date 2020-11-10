class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row_idx in range(row1, row2+1):
            for col_idx in range(col1, col2+1):
                self.rectangle[row_idx][col_idx] = newValue


    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

rectangle = [
    [1,2,1],
    [4,3,4],
    [3,2,1],
    [1,1,1]
]

rectangleObj = SubrectangleQueries(rectangle)
print(rectangleObj.getValue(0, 2))
rectangleObj.updateSubrectangle(0, 0, 3, 2, 5)
rectangleObj.updateSubrectangle(3, 0, 3, 2, 10)
