def solution(S):
    """Return 1 if input string is properly nested

    "(()(())())" -> 1
    "())" -> 0

    Args:
        S (str): string ("(" and/or ")")

    Returns:
        int: whether the input string is properly nested

    Time complexity:
        Best and Worst O(N)
        where N is the length of the input string

    Space complexity:
        Best and Worst O(N)
        where N is the length of the input string
    """
    stack = []

    i = 0
    n = len(S)
    notMatched = False

    while not notMatched and i < n:
        # Push to stack for opening paranthesis
        if S[i] == "(":
            stack.append("(")
        # Pop from stack (if not empty) for closing paranthesis
        elif S[i] == ")" and len(stack) != 0:
            stack.pop()
        # Unmatched pair found
        else:
            notMatched = True
        i += 1
    
    # Edge case: only contain opening paranthesis
    if len(stack) != 0:
        notMatched = True

    if notMatched:
        return 0

    return 1
