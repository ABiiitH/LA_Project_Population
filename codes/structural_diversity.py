import numpy as np

species = ['Environment', 'Phytoplankton', 'Cyanobacteria', 'Brine Shrimp',
           'Brine Fly', 'Corixidae', 'Birds']

A1 = np.array([
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0]
])

A2 = np.array([
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 10, 1, 10, 0]
])

A3 = np.array([
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
])

eig_val_A1=np.linalg.eigvals(A1)
eig_val_A2=np.linalg.eigvals(A2)
eig_val_A3=np.linalg.eigvals(A3)

print("A1:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A1[i, j], end=' ')
    print()

print()

print("Eigenvalues of A1")
for eig in eig_val_A1:
    print(eig)

print()

print("A2:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A2[i, j], end=' ')
    print()

print()

print("Eigenvalues of A2")
for eig in eig_val_A2:
    print(eig)

print()

print("A3:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A3[i, j], end=' ')
    print()

print()

print("Eigenvalues of A3")
for eig in eig_val_A3:
    print(eig)