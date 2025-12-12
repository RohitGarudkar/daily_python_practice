import logging

# Configure the log file
logging.basicConfig(filename="file_errors.log",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print("Error: File not found!")
    except PermissionError:
        logging.error(f"Permission denied: {filename}")
        print("Error: Permission denied!")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred!")

# Example usage
filename = input("Enter the filename: ")
read_file(filename)
