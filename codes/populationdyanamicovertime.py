import numpy as np
import matplotlib.pyplot as plt

# Transition matrix
T = np.array([[0.8, 0.1, 0.0, 0.0, 0.0],
              [0.2, 0.7, 0.3, 0.0, 0.0],
              [0.0, 0.2, 0.6, 0.4, 0.0],
              [0.0, 0.0, 0.1, 0.5, 0.3],
              [0.0, 0.0, 0.0, 0.1, 0.7]])

# Initial population distribution vector
P0 = np.array([100, 200, 150, 50, 300])

# Number of time steps
num_steps = 10

# Initialize an array to store population distributions over time
populations = np.zeros((num_steps+1, len(P0)))
populations[0] = P0

# Calculate population distributions for each time step
for t in range(num_steps):
    populations[t+1] = populations[t] @ T

# Plot the population dynamics over time
plt.figure()
time_steps = np.arange(num_steps+1)
states = np.arange(len(P0))
for state in states:
    plt.plot(time_steps, populations[:, state], label=f"State {state+1}")
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Dynamics over Time')
plt.legend()
plt.show()