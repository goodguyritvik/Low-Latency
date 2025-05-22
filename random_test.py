import random

# Simulate CPU Load (0 to 100%)
cpu_load = random.randint(10, 90)

# Simulate Network Speed (Mbps)
network_speed = random.uniform(1.0, 100.0)

# Simulate Task Priority (0 = Low, 1 = High)
task_priority = random.choice([0, 1])

print(f"Simulated Edge Device:")
print(f"CPU Load: {cpu_load}%")
print(f"Network Speed: {network_speed} Mbps")
print(f"Task Priority: {task_priority}")
