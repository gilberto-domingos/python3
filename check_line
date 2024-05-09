import re

def check_line_endings(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()

    if b'\r\n' in file_content:
        print(f"Error: Found Windows-style line endings (CRLF) in {filename}.")
        return 1
    else:
        return 0

def print_precommit_message():
    print("O PRE-COMMIT ESTÁ FUNCIONANDO!")

if __name__ == "__main__":
    print_precommit_message()  # Call the new function before checking line endings
    exit(check_line_endings('my_code.py'))
