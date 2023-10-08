def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26

    for i in s:
        count[ord(i) - ord('a')] += 1

    for i in t:
        count[ord(i) - ord('a')] -= 1

    for value in count:
        if value != 0:
            return False

    return True