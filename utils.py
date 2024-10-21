import os

def flush() -> None:
    """Flushes the output screen works best with os.system() or cmd"""
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def log(file: str, count: int, base: str, log_index: int) -> None:
    """Log the content in a file to the initializer. May Log in the error if any"""
    try:
        with open(file, "r") as read_file:
            lines = read_file.readlines()
            if log_index < len(lines):
                line_content = lines[log_index].strip()
                print(f"Line {log_index}: {line_content}")
            else:
                raise IndexError("Log index is out of range.")
    except Exception as e:
        with open(base, "a") as base_file:
            count += 1
            base_file.write(f"{count}. {str(e)}\n")
