import numpy as np
import sympy as sp
import math
#points 
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

#sides
bc=C-B
ca=A-C
ab=B-A

#transpose of sides
bc_t=np.transpose(bc)
ca_t=np.transpose(ca)
ab_t=np.transpose(ab)

#length of sides
a1=math.sqrt(np.dot(bc,bc_t))
b1=math.sqrt(np.dot(ca,ca_t))
c1=math.sqrt(np.dot(ab,ab_t))


matrix= np.array([0,1,1,1,0,1,1,1,0]).reshape(3,3)
m2=np.array([a1,b1,c1]).reshape(3,1)


def scale_row(matrix, row_index, scalar):
    matrix[row_index] *= scalar

def add_rows(matrix, source_row, target_row, scalar=1):
    matrix[target_row] += scalar * matrix[source_row]

def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def divide_row_by_scalar(matrix, row_index, scalar):
    matrix[row_index] /= scalar

def add3rows(matrix, target,row1, row2 , row3, scalar1, scalar2, scalar3):
    matrix[target]=scalar1*matrix[row1] +scalar2*matrix[row2] +scalar3*matrix[row3]
    
    
if __name__ == "_main_":
    print("Original Matrix:")
    print(matrix)
    
    # swapping R1 AND R3
    swap_rows(matrix, 0, 2)
    swap_rows(m2, 0, 2)
        
    #step2 R1=R1+R2+R3
    add_rows(matrix, 1, 0, 1)
    add_rows(matrix, 2, 0, 1)
    
    add_rows(m2, 1, 0, 1)
    add_rows(m2, 2, 0, 1)
    
    #R1=R1/2
    x=matrix[0]/2
    matrix[0]=x
    
    y=m2[0]/2
    m2[0]=y
    
    #step4 R1=R1-R3
    add_rows(matrix, 2, 0, -1)
    add_rows(m2, 2, 0, -1)
    
    #step5 R2=R1+R3-R2
    add3rows(matrix, 1,0,2,1, 1, 1, -1)
    add3rows(m2, 1,0,2,1, 1, 1, -1)
    
    #step6 R3=R3-R2
    add_rows(matrix, 1, 2, -1)
    add_rows(m2, 1, 2, -1)
    
    print("\nReduced Matrix:")
    print(matrix)
       

m,n,p =sp.symbols('m n p')
m3=np.array([m,n,p]).reshape(3,1)
z=np.dot(matrix,m3)

a,b,c=sp.symbols('a b c')
m=np.array([a,b,c]).reshape(3,1)
swap_rows(m, 0, 2)
add_rows(m, 1, 0, 1)
add_rows(m, 2, 0, 1)
y=m[0]/2
m[0]=y
add_rows(m, 2, 0, -1)
add3rows(m, 1,0,2,1, 1, 1, -1)
add_rows(m, 1, 2, -1)

print("\nFinal solution:")
print(f"{matrix}{m3}={m}")
print("\nNumerical solution:")
print(f"{matrix}{m2}={m}")
