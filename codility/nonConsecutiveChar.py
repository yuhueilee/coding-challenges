def nonConsecutiveChar(riddle: str) -> str:
    """Replace '?' with a character (a-z) that is not the same as the characters next to it

    Example:
        "?acd?j?z?" -> "bacdejkza"
        "????" -> "abcd"

    Args:
        riddle (str): a string (a-z, ?)

    Returns:
        str: a string
    """
    n = len(riddle)
    string = [word for word in riddle] # make string into array
    ret_val = "" # return vaule
    start_code = ord("a") # starting ascii code
    total_chars = 26 # total number of characters

    prev_index = -1
    curr_index = prev_index + 1
    next_index = curr_index + 1

    res = []

    while next_index <= n:
        curr_char = string[curr_index]
        if curr_char == "?":
            # no characters in front
            if prev_index == -1 and next_index < n:
                if string[next_index] != "?":
                    next_char = string[next_index]
                    next_code = ord(next_char) - start_code
                    # calculate the current character code
                    curr_code = (next_code + 1) % total_chars + start_code
                    curr_char = chr(curr_code)
                # assign random character
                elif string[next_index] == "?":
                    curr_char = "a"
            # no characters at the back
            elif prev_index > -1 and next_index == n:
                prev_char = string[prev_index]
                prev_code = ord(prev_char) - start_code
                # calculate the current character code
                curr_code = (prev_code + 1) % total_chars + start_code
                curr_char = chr(curr_code)
            # have characters in front and at the back
            elif prev_index > -1 and next_index < n:
                prev_char = string[prev_index]
                prev_code = ord(prev_char) - start_code
                if string[next_index] != "?":
                    next_char = string[next_index]
                    next_code = ord(next_char) - start_code
                    hi = max(prev_code, next_code)
                    lo = min(prev_code, next_code)
                    # calculate the gap
                    if hi - lo <= 1:
                        # calculate the current character code
                        curr_code = (hi + 1) % total_chars + start_code
                        curr_char = chr(curr_code)
                    elif hi - lo > 1:
                        # calculate the current character code
                        curr_code = (lo + 1) % total_chars + start_code
                        curr_char = chr(curr_code)
                # use the previous character
                elif string[next_index] == "?":
                    prev_char = string[prev_index]
                    prev_code = ord(prev_char) - start_code
                    # calculate the current character code
                    curr_code = (prev_code + 1) % total_chars + start_code
                    curr_char = chr(curr_code)

        # append character
        res.append(curr_char)
        # update string
        string[curr_index] = curr_char
        # increment pointers
        prev_index += 1
        curr_index += 1
        next_index += 1

    ret_val = "".join(res)

    return ret_val


print(nonConsecutiveChar("?acd?j?z?"))