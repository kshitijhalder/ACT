"""
File Methods:
1. read(): Reads the entire file.
2. read(n): Reads n characters from the file.
3. readline(): Reads a single line from the file.
4. readlines(): Reads all lines from the file and returns a list of lines.
5. write(s): Writes the string s to the file.
6. writelines(lines): Writes a list of lines to the file.
7. close(): Closes the file.
8. seek(offset): Moves the file pointer to the specified offset.
9. tell(): Returns the current position of the file pointer.
10. dump(): Writes the contents of the file to the buffer.      # import pickle
11. load(): Loads the contents of the buffer into the file.     # import pickle

File Attributes:
1. name: The name of the file.
2. mode: The mode in which the file was opened.
3. closed: A boolean indicating whether the file is closed.
4. readable(): Returns True if the file is readable.
5. writable(): Returns True if the file is writable.

Date : 18-04-2024
"""
import os

os.system('clear')
files = open("Python/April/file3.txt", "a+")
print(files)
print(files.tell())
files.read()
print(files.tell())
files.write("Het")
print(files.tell())
files.close()
# use a+ , r+ and w+ and find difference using tell()

def write_counts_to_file(keyword_counts, output_file_path):
    with open(output_file_path, "w") as file:
        for kw, count in keyword_counts.items():
            if count > 0:
                print(f"{kw}: {count}")
                file.write(f"{kw}: {count}\n")
                
import pickle

pickle.dump([1, 2, 3, 4, 5], open("Python/April/file4.txt", "wb"))
print(pickle.load(open("Python/April/file4.txt", "rb")))
