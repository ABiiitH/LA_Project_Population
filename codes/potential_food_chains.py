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

A1_5 = np.linalg.matrix_power(A1, 5)
no_food_chain=A1_5[len(species)-1,0]

print("A1_5:")
for i in range(len(species)):
    for j in range(len(species)):
        print(A1_5[i, j], end=' ')
    print()

print()

print(f"No. of possible food chains: {no_food_chain}")

