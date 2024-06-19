# Request user input for the original string and the method to apply
a = input("Enter a String: ").strip()  # Trim whitespace from the input string
print(f"Original String: {a}")
method = input("Enter the string method: ").lower().strip()  # Trim whitespace from the method input

# Split the method input into individual methods
methods = method.split(" ")

# Initialize a dictionary to hold replacement strings for each method
replacement_strings = {}

# Request additional input based on the method specified
for m in methods:
    if m in ["replace", "partition", "rpartition", "startswith", "endswith", "rfind", "count", "find"]:
        if m not in replacement_strings:  # Check if the method is not already in the dictionary
            replacement_strings[m] = []  # Initialize an empty list for the method
        replacement_string = input(f"Enter the replacement string for {m}: ").strip()  # Ask for the replacement string specifically for this method
        replacement_strings[m].append(replacement_string)  # Add the replacement string to the list for this method
        if m == "replace" and len(replacement_strings[m]) < 2:  # If it's the replace method and we don't have two strings yet
            replacement_string_2 = input("Enter the second replacement string: ").strip()  # Ask for the second replacement string
            replacement_strings[m].append(replacement_string_2)  # Add the second replacement string to the list for this method



# Define a dictionary mapping string methods to their results
results = {
    "capitalize": a.capitalize(),
    "title": a.title(),
    "upper": a.upper(),
    "lower": a.lower(),
    "swapcase": a.swapcase(),
    "isalnum": a.isalnum(),
    "isalpha": a.isalpha(),
    "isdigit": a.isdigit(),
    "isnumeric": a.isnumeric(),
    "center": a.center(50),
    "isupper": a.isupper(),
    "islower": a.islower(),
    "istitle": a.istitle(),
    "strip": a.strip(),
    "lstrip": a.lstrip(),
    "rstrip": a.rstrip(),
    "split": a.split(" "),
    "rsplit": a.rsplit(" "),
    "join": ", ".join(["sample", "list"]),
    "encode": a.encode(),
    "decode": a.encode().decode(),
    "isspace": a.isspace(),
    "isdecimal": a.isdecimal(),
    "isascii": a.isascii(),
    "splitlines": a.splitlines(),
    "partition": a.partition(replacement_strings["partition"][0]) if "partition" in replacement_strings else "Replacement string not provided",
    "rpartition": a.rpartition(replacement_strings["rpartition"][0]) if "rpartition" in replacement_strings else "Replacement string not provided",
    "startswith": a.startswith(replacement_strings["startswith"][0]) if "startswith" in replacement_strings else "Replacement string not provided",
    "endswith": a.endswith(replacement_strings["endswith"][0]) if "endswith" in replacement_strings else "Replacement string not provided",
    "rfind": a.rfind(replacement_strings["rfind"][0]) if "rfind" in replacement_strings else "Replacement string not provided",
    "count": a.count(replacement_strings["count"][0]) if "count" in replacement_strings else "Replacement string not provided",
    "find": a.find(replacement_strings["find"][0]) if "find" in replacement_strings else "Replacement string not provided",
    "replace": a.replace(replacement_strings["replace"][0], replacement_strings["replace"][1]) if "replace" in replacement_strings and len(replacement_strings["replace"]) > 1 else "Replacement strings not provided"
}

for m in methods:
    if m in results:
        print(f"{m}: {results[m]}")
        
    else:
        print(f"{m} is not a valid string method.")