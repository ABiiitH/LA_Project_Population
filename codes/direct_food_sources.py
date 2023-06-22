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

v1=np.array([
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1]
])

v2=np.array([[1, 1, 1, 1, 1, 1, 1]])

A1v1=A1@v1
v2A1=v2@A1

print("A1v1:")
for i in range(len(species)):
    for j in range(1):
        print(A1v1[i, j], end=' ')
    print()

print()

print("v2A1:")
for i in range(1):
    for j in range(len(species)):
        print(v2A1[i, j], end=' ')
    print()

