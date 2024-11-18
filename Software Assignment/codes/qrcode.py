dim = int(input("Enter the dimension of your square matrix: "))
A=[]
for i in range(dim):
    row = []
    for j in range(dim):
        element = float(input(f"Enter the element in ({i},{j})th position: "))
        row.append(element)
    A.append(row)

for x in range(100):
    Q = [[0] * dim for _ in range(dim)]
    R = [[0] * dim for _ in range(dim)]
    
    for j in range(dim):
        v = [A[k][j] for k in range(dim)]
        for i in range(j): 
            R[i][j] = sum(Q[k][i] * A[k][j] for k in range(dim))
            v = [v[k] - R[i][j] * Q[k][i] for k in range(dim)]
        R[j][j] = sum(v[k]*2 for k in range(dim))*0.5
        for k in range(dim):
            Q[k][j] = v[k] / R[j][j]

    A = [[sum(R[i][k] * Q[k][j] for k in range(dim)) for j in range(dim)] for i in range(dim)]
    
    extras = sum(A[i][j]**2 for i in range(dim) for j in range(dim) if i != j)
    if extras < 1e-10:
        break

print("The eigenvalues of the given matrix are:")
for i in range(dim):
    print(A[i][i], end = ' ')
print("\n")
