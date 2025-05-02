#!/usr/bin/env python3
import subprocess
import time
import sys

def time_command(command):
    """Run a command and return its execution time"""
    print(f"Running: {' '.join(command)}")
    
    start_time = time.time()
    # Run the command and stream output to console in real-time
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    # Print output in real-time
    # for line in process.stdout:
    #     print(line, end='')  # Output already contains newlines

    process.wait()
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
    
    print(f"Time: {execution_time:.2f} seconds")
    return execution_time

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python time_command.py <command> [args...]")
        sys.exit(1)
    
    time_command(sys.argv[1:])