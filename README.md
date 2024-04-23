# Log Analysis and Monitoring Script

This script automates the analysis and monitoring of log files.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

git clone <repository_link>
cd <repository_name>

2. Run the script:
python log-monitor.py


3. To stop the script, press Ctrl+C.

## Script Functionality

### Log File Monitoring

The script continuously monitors a specified log file for new entries using the `tail` command. New log entries are displayed in real-time.

### Log Analysis

The script performs basic analysis on log entries:

- Counts occurrences of specific keywords or patterns, such as "ERROR" and "HTTP status".
- Generates summary reports, including the number of ERROR occurrences and HTTP status occurrences.

## How to Interpret Results

- The script will display new log entries in real-time as they are written to the log file.
- After monitoring, the script will analyze the log file and provide summary reports on the occurrences of specific keywords or patterns.

## Additional Information

- Ensure that the specified log file exists and has appropriate permissions for reading.
- Customize the `log_file` variable in the script to point to the desired log file.
- For any issues or questions, please open an issue in the repository.





