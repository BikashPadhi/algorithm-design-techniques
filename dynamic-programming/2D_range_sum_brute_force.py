def range_sum(matrix, row1, col1, row2, col2):
	toal_sum = 0
	for i in range(row1, row2 + 1):
		for j in range(col1, col2 + 1):
			toal_sum += matrix[i][j]

	return toal_sum

matrix = [
  [3, 0, 1, 4, 2],
  [4, 6, 3, 2, 1],
  [1, 2, 9, 1, 5],
  [4, 1, 2, 1, 7],
  [1, 0, 3, 0, 5]
]

print range_sum(matrix, 1, 2, 3, 4)
