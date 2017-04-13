import sys

if sys.argv.__len__() != 2:
    print("Usage: python transpiler.py <brainfuck_filename>")
    sys.exit()

"""
    A brainfuck transpiler to C written in Python.
"""

# Global values (Configurable in the future)
MAX_FILE_SIZE = 30000

# Helper variable
code_ptr = 0                            # Current location of the code pointer
program_ptr = 0                         # Current location of the program pointer
# code = []                             # Memory map where the code will be stored
storage = 0                             # The variable that will serve as storage
program = [0] * MAX_FILE_SIZE           # The memory that will be edited by the code
bracer_ptr = 0                          # Current location of the stack pointer
bracer_stack = []                       # Locations of unmatched '[' and ']'
bracer_target = [0] * MAX_FILE_SIZE     # Locations of matching '[' and ']'

# Load the code to memory
with open(sys.argv[1]) as bf_file:
    code = bf_file.read()

# Transpiling
with open('output.c', 'w') as c_file:
    # Prepare common code
    c_file.write("#include <stdio.h>\n")
    c_file.write("int main(){\n")
    c_file.write("int file[" + str(MAX_FILE_SIZE) + "];\n")
    c_file.write("int ptr = 0;\n")

    # Run through the code
    for char in code:
        if char is '+':
            c_file.write("file[ptr]++;\n")
        elif char is '-':
            c_file.write("file[ptr]--;\n")
        elif char is '>':
            c_file.write("ptr++;\n")
        elif char is '<':
            c_file.write("ptr--;\n")
        elif char is '.':
            c_file.write("printf(\"%c\", file[ptr]);\n")
        elif char is ',':
            c_file.write("scanf(\"%c\", &(file[ptr]));\n")
        elif char is '[':
            c_file.write("while(file[ptr]){\n")
        elif char is ']':
            c_file.write("}\n")

    # End the code
    c_file.write("}\n")
