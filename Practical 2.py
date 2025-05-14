def pda_anbn(string):
    stack = []
    for char in string:
        if char == 'a':
            stack.append('A')  # Push a symbol for each 'a'
        elif char == 'b':
            if not stack:
                return False  # If there's no matching 'a' for this 'b', reject
            stack.pop()  # Pop the symbol for the matching 'a'
        else:
            return False  # Reject any other characters
    return len(stack) == 0  # Accepted if the stack is empty (all 'a's have been matched by 'b's)

# Test cases
test_strings = ["", "ab", "aabb", "aaabbb", "aabbb", "abab"]
for s in test_strings:
    print(f"{s} => {'Accepted' if pda_anbn(s) else 'Rejected'}")
