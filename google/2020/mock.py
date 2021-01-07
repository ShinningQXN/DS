You are given a 2d rectangular array of positive integers representing the height map of a continent. The "Pacific ocean" touches the left and 
top edges of the array and the "Atlantic ocean" touches the right and bottom edges.
  - Find the "continental divide". That is, the list of grid points where water can flow either to the Pacific or the Atlantic.
Water can only flow from a cell to another one with height equal or lower.

Example:

Pacific ~ ~ ~ ~ ~ |__
 ~ 1 2 2 3 (5) ~
 ~ 3 2 3 (4)(4) ~
 ~
Example:

Pacific ~ ~ ~ ~ ~ |__
 ~ 1 2 2 3 (5) ~
 ~ 3 2 3 (4)(4) ~
 ~ 2 4 (5) 3 1 ~
 ~ (6)(7) 1 4 5 ~
__ (5) 1 1 2 4 ~
  |~ ~ ~ ~ ~ Atlantic

The answer would be the list containing the coordinates of all circled cells:
[(4,0), (3,1), (4,1), (2,2), (0,3), (1,3), (0,4)]


def find_continent_divide(self, matrix: List[List[int]])->List[tuple]:
	if not matrix:
		return []

	m, n = len(matrix), len(matrix[0])
	q_pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
	q_atlantic = [(m-1, j) for j in range(n)] + [(i, n - 1) for i in range(m)]
	pacific = set(q_pacific)
	atlantic = set(q_atlantic)
	# for i in range(m):
	# 	matrix[m][0] *= -1
	# 	matrix[m][n-1] *= -1

	# for i, j in q_pacific:
	# 	for ii, jj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
	# 		if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] >= matrix[ii][jj] and (ii, jj) not in pacific:
	# 			pacific.add(i, j)
	# 			q_pacific.append((ii, jj))
	def flow(queue, visited):
		for i, j in queue:
			for ii, jj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
				if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] >= matrix[i][j] and (ii, jj) not in visited:
					visited.add(ii, jj)
					queue.append((ii, jj))
	flow(q_pacific, pacific)
	flow(q_atlantic, atlantic)

	return list(pacific.intersect(atlantic))


1 2 3
2 2 4
1 2 1

02,02,21,22,20,30,31

[01,02,10,20,11]
[02,12,22,20,21]




				


