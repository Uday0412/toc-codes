def ndfa(input_string):
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0':
            if char == 'a':
                current_state = 'q1'
            else:
                return False
        elif current_state == 'q1':
            if char == 'b':
                current_state = 'q2'
            else:
                return False
        elif current_state == 'q2':
            if char == 'a' or char == 'b':
                current_state = 'q3'
            else:
                return False
        elif current_state == 'q3':
            if char == 'a' or char == 'b':
                current_state = 'q3'
            else:
                return False

    # Check if the final state is q4
    if current_state == 'q3' or current_state == 'q4':
        return True
    else:
        return False

# Test cases
strings_to_test = [
    "abba",   # Starts with ab, ends with ba
    "ababab", # Starts with ab, contains intermediate 'a' and 'b'
    "ab",     # Starts with ab, ends with nothing
    "abab",   # Starts with ab, but doesn't end with ba
    "ba",     # Doesn't start with ab
    "abbaa",  # Starts with ab, ends with ba but has extra characters
    "abbaab"  # Starts with ab, ends with ba with additional characters
]

for string in strings_to_test:
    if ndfa(string):
        print(f"String '{string}' is accepted.")
    else:
        print(f"String '{string}' is not accepted.")
