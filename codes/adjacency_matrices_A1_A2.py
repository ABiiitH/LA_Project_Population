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
    [0, 0, 0, 10, 10, 1, 0]
])

print("Adjacency Matrix A1:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A1[i, j], end=' ')
    print()

print()

print("Adjacency Matrix A2:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A2[i, j], end=' ')
    print()

