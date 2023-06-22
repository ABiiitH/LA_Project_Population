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

A1_2=np.linalg.matrix_power(A1, 2)

v1=np.array([
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1]
])

A1v1=A1@v1
A1_2v1=A1_2@v1
total=A1v1+A1_2v1

print("A1_2:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A1_2[i, j], end=' ')
    print()

print()

print("A1_2v1:")
for i in range(len(species)):
    for j in range(1):
        print(A1_2v1[i, j], end=' ')
    print()

print()

print("A1v1 + A1_2v1:")
for i in range(len(species)):
    for j in range(1):
        print(total[i, j], end=' ')
    print()
