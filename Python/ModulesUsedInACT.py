# Find all modules used in all scripts in a directory

import os
import re
import sys
"""
def find_modules(directory):
    modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.ipynb'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        match = re.match(r'^import\s+(\S+)', line)
                        if match:
                            modules.add(match.group(1))
                        match = re.match(r'^from\s+(\S+)\s+import', line)
                        if match:
                            modules.add(match.group(1))
    return modules

# Call the function with the specified directory
modules_used = find_modules("/Users/kshitijhalder/Desktop/ACT/Python")

# Print the result
print("Modules used:", modules_used)

#Number of modules used
print("Number of modules used:", len(modules_used))

"""

def find_modules(directory):
    modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.ipynb'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        match = re.search(r'import\s+(\S+)', line)
                        if match:
                            modules.add(match.group(1))
                        match = re.search(r'from\s+(\S+)\s+import', line)
                        if match:
                            modules.add(match.group(1))
                        match = re.search(r'%matplotlib inline; from (\S+) import \*', line, re.IGNORECASE)
                        if match:
                            modules.add(match.group(1))
    return modules

# Call the function with the specified directory
modules_used = find_modules("/Users/kshitijhalder/Desktop/ACT/Python")

# Print the result
print("Modules used:", modules_used)

#Number of modules used
print("Number of modules used:", len(modules_used))

# Save the result to a file
with open("modules_used.txt", "w") as f:
    for module in modules_used:
        f.write(module + "\n")
