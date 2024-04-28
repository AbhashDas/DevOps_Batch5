import psutil  # Import the psutil module for system monitoring
import time  # Import the time module for time-related operations

def monitor_cpu(threshold):
    """
    Monitor CPU usage and print alerts if it exceeds the threshold.   
    Args:
        threshold (float): The threshold CPU usage percentage.
    """
    print("Monitoring CPU usage...")  # Print a message indicating that CPU monitoring has started
    try:
        while True:  # Loop indefinitely to continuously monitor CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)  # Get the CPU usage percentage for the last second
            if cpu_usage > threshold:  # If CPU usage exceeds the threshold
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")  # Print an alert message
            time.sleep(1)  # Wait for 1 second before checking CPU usage again
    except KeyboardInterrupt:  # Handle keyboard interrupt (Ctrl+C) to stop monitoring
        print("Monitoring stopped.")  # Print a message indicating that monitoring has stopped

if __name__ == "__main__":
    threshold = 80  # Set the threshold CPU usage percentage (change as needed)
    monitor_cpu(threshold)  # Start monitoring CPU usage with the specified threshold

