import os

# Prompt the user for a directory path
directory = input("Enter the directory path: ")

# Check if the directory exists
if os.path.isdir(directory):
    print(f"Contents of '{directory}':")
    # List all files and folders in the directory
    for item in os.listdir(directory):
        print(item)
else:
    print(f"Directory '{directory}' does not exist.")