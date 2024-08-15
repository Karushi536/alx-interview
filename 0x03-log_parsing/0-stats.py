#!/usr/bin/python3
import sys
import signal

# Initialize counters and metrics
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """ Print the collected statistics. """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """ Handle the keyboard interruption (CTRL + C). """
    print_statistics()
    sys.exit(0)

# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from standard input
for line in sys.stdin:
    # Check if the line matches the expected format
    parts = line.split()
    if len(parts) < 7 or parts[5] != '"GET' or parts[6] != '/projects/260' or not parts[8].isdigit():
        continue
    
    # Extract status code and file size
    status_code = int(parts[8])
    file_size = int(parts[9])
    
    # Update metrics
    total_file_size += file_size
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1
    
    line_count += 1
    
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()

# Print final statistics if loop ends naturally
print_statistics()
