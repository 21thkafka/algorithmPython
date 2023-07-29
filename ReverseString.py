from typing import List

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s) 

def reverseString2(s: List[str]) -> None:
    s.reverse()
    print(s)

reverseString(['s','f','g','a'])
reverseString2(['s','f','g','a'])