"""
Find the occurrance of keywords in a file (py) and write the occurrance to a file (txt).
Date: 17-04-2024
import os
import keyword

os.system('clear')

with open("Python/April/#Acc.Creation.py", "r") as file:
    lines = file.readlines()

# Initialize a dictionary to store keyword counts
keyword_counts = {kw: 0 for kw in keyword.kwlist}

for line in lines:
    # Split the line into words
    words = line.split()
    for word in words:
        # If the word is a keyword, increment its count
        if word in keyword_counts:
            keyword_counts[word] += 1

# Print the counts of each keyword
with open("Python/April/Keyword_Occ.txt", "w") as file:
    for kw, count in keyword_counts.items():
        if count > 0:
            print(f"{kw}: {count}")
            file.write(f"{kw}: {count}\n")

            """
import os
import keyword

def count_keywords(file_path):
    # Initialize a dictionary to store keyword counts
    keyword_counts = {kw: 0 for kw in keyword.kwlist}

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        # Split the line into words
        words = line.split()
        for word in words:
            # If the word is a keyword, increment its count
            if word in keyword_counts:
                keyword_counts[word] += 1

    return keyword_counts


os.system('clear')

keyword_counts = count_keywords("Python/April/#Acc.Creation.py")
#write_counts_to_file(keyword_counts, "Python/April/Keyword_Occ.txt")
