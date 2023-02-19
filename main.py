from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i + 1))
        elif char in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack.pop().char, char):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

def main():
    text = input().strip()
    if text.startswith("I"):
        mismatch = find_mismatch(text[1:])
        print(mismatch)
        
if __name__ == "__main__":
    main()
