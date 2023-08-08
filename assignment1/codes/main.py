import numpy as np

# Given vertices
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

#function to find norm
def norm_vec(a, b):
    return np.array([-1*(b[1]-a[1]), b[0]-a[0]])

#function to find distance
def distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])*2 + (point2[1] - point1[1])*2)


k1 = 1
k2 = 1

p = np.zeros(2)
t = norm_vec(B, C)
n1 = t / np.linalg.norm(t)
t = norm_vec(C, A)
n2 = t / np.linalg.norm(t)
t = norm_vec(A, B)
n3 = t / np.linalg.norm(t)

p[0] = n1 @ B - k1 * n2 @ C
p[1] = n2 @ C - k2 * n3 @ A

N = np.vstack((n1 - k1 * n2, n2 - k2 * n3))
I = np.matmul(np.linalg.inv(N), p)
r = n1 @ (I - B)

print("Coordinates of point I:", I)
print("Distance r:", r)
