import time
import os 
width = os.get_terminal_size().columns #To get the width of the terminal and use them to print in center of the terminal

# Function to calculate the time elapsed between start and stop of the stopwatch
def stop_watch():
    print("..........STOP WATCH..........".center(width))
    input("Press Enter to start the stop watch ".center(width))
    start_time = time.time()
    print("..........STOP WATCH STARTED..........".center(width))
    input("Press Enter to stop the stop watch ".center(width))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

#Printing the total time elapsed
print(f"Total time elapsed is {stop_watch():.2f} seconds".center(width))
