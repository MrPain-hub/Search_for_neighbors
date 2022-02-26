import numpy as np

p1 = [1, 2, 3]
p2 = [5, 5, 5]
point_1 = np.array(p1)
point_2 = np.array(p2)
# Get the square of the difference of the 2 vectors
square = np.square(point_1 - point_2)
# Get the sum of the square
sum_square = np.sum(square)
print(square)
print(sum_square)
out = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

print(out)
