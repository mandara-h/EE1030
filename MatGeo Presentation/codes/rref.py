import numpy as np

def rref(A):
    A = A.astype(float)
    rows, cols = A.shape
    r = 0
    
    for c in range(cols):
        if r >= rows:
            break
        
        max_row = np.argmax(np.abs(A[r:rows, c])) + r
        if A[max_row, c] == 0:
            continue
        
        A[[r, max_row]] = A[[max_row, r]]
        
        A[r] = A[r] / A[r, c]
        
        for i in range(rows):
            if i != r:
                A[i] -= A[i, c] * A[r]
        
        r += 1
    
    return A

A = np.array([[-2, 3, 5],
              [1, 2, 3],
              [7, 0, -1]])

rref_matrix = rref(A)
print(rref_matrix)

