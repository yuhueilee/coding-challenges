def palindrome(S: str) -> str:
    """Return the one of the possible palindrome of the input string or "NO" if not possible

    Example:
        "?ab??" -> "aabaa"
        "????" -> "aaaa"
        "ab?b" -> "NO"

    Args:
        S (str): a string (a-z, ?)

    Returns:
        str: palindrome
    """
    start = 0 # start index of the string
    end = len(S) - 1 # end index of the string
    ret_val = "" # return value
    res = [] # store the characters

    # Edge case: string of length 1
    if start == end:
        if S == "?":
            return "a"
        else:
            return S

    # Keep iteratiing the string from two end points 
    # while both characters are the same or is a question mark
    # and start and end has not yet collided
    while start < end and (S[start] == "?" or S[end] == "?" or S[start] == S[end]):
        if S[start] == "?" and S[end] == "?":
            res.append("a")
        elif S[start] != "?":
            res.append(S[start])
        elif S[end] != "?":
            res.append(S[end])
        # increment start
        start += 1
        # decrement end
        end -= 1
    
    # Loop is terminated due to difference of characters
    if start < end:
        return "NO"
    
    # Form the string
    front = "".join(res)
    back = "".join(reversed(res))

    # Edge case: odd length string
    if len(S) % 2 == 1:
        middle = S[len(S) // 2]
        if middle == "?":
            middle = "z"
        ret_val = front + middle + back
    else:
        ret_val = front + back
    
    return ret_val


print(palindrome("?ab??"))