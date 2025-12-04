import math

def SubString(string, stringSize):
    n = int(math.pow(2, stringSize))
    all_subsets = []

    for outer in range(0, n):
        substring = ""

        for inner in range(0, stringSize):
            if ((outer & (1 << inner)) > 0):
                substring += string[inner]
        if substring:  # Only add non-empty substrings
            all_subsets.append(substring)
    
    print(all_subsets)

string = input("Enter a string: ")
SubString(string, len(string))