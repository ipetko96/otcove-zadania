import re

a = "ivaan"
pattern = r"a"


def checkString(pattern: str, string: str) -> bool:
    if len(re.findall(pattern, string)) >= 2:
        return True
    else:
        return False


print(checkString(pattern, a))
