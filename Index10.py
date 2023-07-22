def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x = 0
    if s[0].isdigit():
        x += int(s[0])
    if s[1].isdigit():
        x += int(s[1])
    if s[2].isdigit():
        x += int(s[2])
    if s[3].isdigit():
        x += int(s[3])
    if s[4].isdigit():
        x += int(s[4])
    return x

print(main("Asr12"))
print(main('10002'))