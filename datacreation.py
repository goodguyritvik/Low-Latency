import numpy as np
import pandas as pd 

# Generate 1000 simulated tasks
num_samples = 1000
cpu_load = np.random.randint(10, 100, num_samples)  # CPU load between 10% to 100%
memory_usage = np.random.randint(10, 90, num_samples)  # Memory between 10% to 90%
network_speed = np.random.uniform(1.0, 100.0, num_samples)  # Network speed in Mbps
task_size = np.random.uniform(0.1, 50.0, num_samples)  # Task size in MB
task_priority = np.random.choice([0, 1], num_samples)  # 0 = Low, 1 = High

# Label (Scheduling Decision): If CPU > 70% OR network speed < 10 Mbps, Offload to Cloud (1), else Process Locally (0)
labels = [1 if cpu_load[i] > 70 or network_speed[i] < 10 else 0 for i in range(num_samples)]

# Create DataFrame
df = pd.DataFrame({
    "CPU Load (%)": cpu_load,
    "Memory Usage (%)": memory_usage,
    "Network Speed (Mbps)": network_speed,
    "Task Size (MB)": task_size,
    "Task Priority": task_priority,
    "Scheduling Decision (0 = Local, 1 = Cloud)": labels
})

# Save dataset as CSV
df.to_csv("simulated_edge_computing_data.csv", index=False)
print("Dataset saved successfully!")
