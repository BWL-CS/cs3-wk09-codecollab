import numpy as np
from matplotlib import pyplot as plt

# Parameters
u = 5
a = 2
t = np.linspace(0, 10, 100)

# Kinematic Equations
s = (u * t) + (0.5 * a * t**2)
v = u + (a * t)
a_values = a * np.ones_like(t)
s_final = s[-1]
print(f"Displacement at t=10 seconds: {s_final:.2f} meters")

# Plotting Data
plt.figure(figsize=(4, 4))

plt.subplot(3, 1, 1)
plt.plot(t, s, '--c')
plt.title('Position vs Time', fontsize=10)
plt.ylabel('Position (m)', fontsize=8)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, ':r')
plt.title('Velocity vs Time', fontsize=10)
plt.ylabel('Velocity (m/s)', fontsize=8)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a_values, '-.m', linewidth=2)
plt.title('Acceleration vs Time', fontsize=10)
plt.xlabel('Time (s)', fontsize=8)
plt.ylabel('Acceleration (m/s$^2$)', fontsize=8)
plt.grid(True)

plt.tight_layout()
plt.savefig('result.png', bbox_inches='tight')
