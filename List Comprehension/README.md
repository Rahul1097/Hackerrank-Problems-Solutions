# List comprehension

Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, i lies between 0 and x,j lies between 0 and y,k lies between 0 and z .Please use list comprehensions rather than multiple loops, as a learning exercise.

Input Format

Four integers x,y,z and n , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0-

1

1

1

2

Sample Output 0-

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Sample Input 1-

2

2

2

2

Sample Output 1-

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
