import numpy as np
from model_updated import model

def predict(task_data):
    """Make prediction for task scheduling"""
    # Convert input to numpy array with correct dtype
    task_array = np.array(task_data, dtype=np.float32).reshape(1, -1)
    prediction = model.predict(task_array)
    return "Process Locally" if np.argmax(prediction) == 0 else "Offload to Cloud"

# Example usage
if __name__ == "__main__":
    # Example: New Task (CPU Load = 75%, Network Speed = 15 Mbps, Task Priority = High)
    new_task = np.array([[0.75, 0.15, 1]])  
    decision = predict(new_task)
    print(f"AI Decision: {decision}")
