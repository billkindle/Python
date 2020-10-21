#!/usr/local/bin/python

# This is my first attempt at a working Python script

# Make some variables

file = 'file.txt'

print('What text would you like to type?')

text = input() # take input and write this text to the file.


# Here I'm going to create a new file that doesn't exist yet
with open(file, 'w') as write_file:
    write_file.write(text)

print(file + " will now be closed.") # here I'm combining a variable with a string that I'm printing to screen.

write_file.close() # close the file when done.

print('Now opening the file to read it back to you')

with open(file, 'r') as open_file:
    print(open_file.read())

print(file + " will now be closed again.")

open_file.close()