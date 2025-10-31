import numpy as np
from matplotlib import pyplot as plt

# Parameters (using Numpy -> look it up!)
velocity_initial = 5
acceleration = 2
time = np.linspace(0, 10, 100)

# Kinematic Equations (using Numpy -> look it up!)
position_eqn = (velocity_initial * time) + (0.5 * acceleration * (time**2))
velocity_eqn = velocity_initial + (acceleration * time)
a_values = acceleration * np.ones_like(time)
position_final = position_eqn[-1]
print(f"Displacement at t=10 seconds: {position_final:.2f} meters")

# Plotting Data with Matplotlib functions
plt.figure(figsize=(4, 4))

plt.subplot(3, 1, 1)
plt.plot(time, position_eqn, '--c')
plt.title('Position vs Time', fontsize=10)
plt.ylabel('Position (m)', fontsize=8)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time, velocity_eqn, ':r')
plt.title('Velocity vs Time', fontsize=10)
plt.ylabel('Velocity (m/s)', fontsize=8)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, a_values, '-.m', linewidth=2)
plt.title('Acceleration vs Time', fontsize=10)
plt.xlabel('Time (s)', fontsize=8)
plt.ylabel('Acceleration (m/s$^2$)', fontsize=8)
plt.grid(True)

plt.tight_layout()
plt.savefig('result.png', bbox_inches='tight')
