from predict import predict

def process_task(task_data):
    """Process task data"""
    try:
        # Pass raw values directly to predict()
        decision = predict([
            task_data['cpu_load'],
            task_data['network_speed'],
            task_data['priority']
        ])
        return decision
    except Exception as e:
        print(f"Error processing task: {e}")
        return None

if __name__ == "__main__":
    print("Scheduler running in standalone mode")
    
    # Test task data
    test_task = {
        'cpu_load': 0.75,
        'network_speed': 0.15, 
        'priority': 1
    }
    
    # Process and display prediction
    decision = process_task(test_task)
    print(f"Prediction: {decision}")
