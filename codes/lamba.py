import matplotlib.pyplot as plt

# Define the time-specific growth rates (λt) over time
growth_rates = [1.2, 1.3, 1.1, 0.9, 1.2, 0.8, 1.0]

# Calculate the cumulative growth rates (λ) over time
cumulative_growth = [1]
for rate in growth_rates:
    cumulative_growth.append(cumulative_growth[-1] * rate)

# Define the time steps
time_steps = list(range(len(growth_rates) + 1))

# Plot the time-specific growth rates
plt.plot(time_steps, growth_rates, marker='o')
plt.xlabel('Time')
plt.ylabel('Time-specific Growth Rate (λt)')
plt.title('Population Growth Rates over Time')
plt.show()

# Plot the cumulative growth rates
plt.plot(time_steps, cumulative_growth, marker='o')
plt.xlabel('Time')
plt.ylabel('Cumulative Growth Rate (λ)')
plt.title('Cumulative Population Growth over Time')
plt.show()
