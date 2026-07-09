import os

# --------------------------------------------------
# Log Analyzer
# Author: Sakshi Devda
# Description: Analyze a log file and count
#              Errors, Warnings, and Information.
# --------------------------------------------------

print("=" * 40)
print("         LOG ANALYZER")
print("=" * 40)

# Get log file name
file_name = input("Enter log file name: ")

# Check if file exists
if not os.path.exists(file_name):
    print("\nError: File not found!")

else:

    error_count = 0
    warning_count = 0
    info_count = 0

    # Read the log file
    with open(file_name, "r") as file:

        for line in file:

            line = line.upper()

            if "ERROR" in line:
                error_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "INFO" in line:
                info_count += 1

    # Display results
    print("\nLog Analysis Report")
    print("-" * 40)
    print("Errors   :", error_count)
    print("Warnings :", warning_count)
    print("Info     :", info_count)
    print("-" * 40)

print("\nLog analysis completed successfully!")
