import re

def lengthOfLastWord(s: str) -> int:
    s1 = s.strip()
    return len(re.split("\s+", s1)[len(re.split("\s+", s1)) - 1])