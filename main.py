import time

# Function to perform a CPU-intensive task
def cpu_intensive_task():
    start_time = time.time()

    # Perform CPU-intensive computations
    result = 0
    for i in range(10**7):
        result += i

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

# Main function
def main():
    execution_time = cpu_intensive_task()
    print("CPU-Heavy Workload Execution Time:", execution_time, "seconds")

if __name__ == "__main__":
    main()
