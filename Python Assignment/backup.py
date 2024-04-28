import os
import sys
from datetime import datetime

def copy_files(src, dest):
    try:
        # Ensure destination directory exists
        if not os.path.exists(dest):
            os.makedirs(dest)

        # Iterate through files and directories in source
        for item in os.listdir(src):
            src_item = os.path.join(src, item)
            dest_item = os.path.join(dest, item)

            # If item is a directory, recursively copy it
            if os.path.isdir(src_item):
                copy_files(src_item, dest_item)
            else:
                # Copy file from source to destination
                with open(src_item, 'rb') as fsrc, open(dest_item, 'wb') as fdest:
                    # Copy file contents
                    for chunk in iter(lambda: fsrc.read(4096), b''):
                        fdest.write(chunk)
                print(f"Copied {src_item} to {dest_item}")

    except Exception as e:
        print(f"Error copying {src} to {dest}: {e}")

def backup_files(source_dir, dest_dir):
    try:
        # Call recursive function to copy files and directories
        copy_files(source_dir, dest_dir)

        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    # Check if correct number of command-line arguments provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    # Get source and destination directories from command-line arguments
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    # Call backup_files function with provided directories
    backup_files(source_dir, dest_dir)
