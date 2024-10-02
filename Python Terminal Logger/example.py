import sys
from TerminalLogger import DualOutput

# Redirect sys.stdout to both console and file
output_file = "output.txt"
sys.stdout = DualOutput(output_file, terminalOutput=False)

# Example output to demonstrate functionality
print("This will be shown in the terminal and written to the file.\n\
      This will be shown in the terminal and written to the file in a new line\
      \n\n")
print("Another line, saved after this line.")
print("no newline", end="")
print("no newline", end="")

# Close the custom stdout handler
sys.stdout.close()

# Restore default stdout
sys.stdout = sys.__stdout__

print("Back to normal terminal output.")