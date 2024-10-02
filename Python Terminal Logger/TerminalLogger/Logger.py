import io
import sys
import time

class DualOutput(io.TextIOBase):
    def __init__(self, file:str, terminalOutput = False):
        super().__init__()
        self.file = open(file, 'w')
        self.txt:str = ""
        self.terminalOutput:bool = terminalOutput

    def write(self, text):
        time_stamp = time.ctime(time.time())
        if self.terminalOutput:
            sys.__stdout__.write(text)  # Output to the console
        self.txt += text
        while "\n" in self.txt:
            index = self.txt.index("\n")
            self.file.write(time_stamp + " -> " + self.txt[:index + 1])   # Write to the file if newline is found
            self.file.flush()       # Ensure data is written to the file
            self.txt = self.txt[index + 1:]

    def close(self):
        time_stamp = time.ctime(time.time())
        self.file.write(time_stamp + " -> " + self.txt + "\n")   # Write to the file if newline is found
        self.file.close()           # Close the file when done