import subprocess
import re
import signal
import sys
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    logger.info("Monitoring interrupted. Exiting.")
    sys.exit(0)

# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Function to monitor log file
def monitor_log_file(log_file):
    try:
        logger.info(f"Monitoring log file: {log_file}")
        # Open log file for reading
        with open(log_file, 'r') as f:
            # Move to the end of the file
            f.seek(0,2)
            while True:
                # Read new lines as they are written to the file
                line = f.readline()
                if line:
                    print(line.strip())  # Print the new log entry
                else:
                    time.sleep(0.1)  # Wait for new lines
    except FileNotFoundError:
        logger.error(f"Log file {log_file} not found.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error while monitoring log file: {str(e)}")
        sys.exit(1)

# Function to perform log analysis
def analyze_log(log_file):
    try:
        logger.info(f"Analyzing log file: {log_file}")
        # Open log file for reading
        with open(log_file, 'r') as f:
            log_content = f.read()

        # Count occurrences of specific keywords or patterns
        error_count = len(re.findall(r'ERROR', log_content))
        http_status_count = len(re.findall(r'HTTP status', log_content))

        # Generate summary reports
        logger.info(f"Number of ERROR occurrences: {error_count}")
        logger.info(f"Number of HTTP status occurrences: {http_status_count}")
    except FileNotFoundError:
        logger.error(f"Log file {log_file} not found.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error while analyzing log file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Specify the log file path
    log_file = "example.log"

    # Start log file monitoring
    monitor_log_file(log_file)

    # Perform log analysis
    analyze_log(log_file)

