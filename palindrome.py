import collections
import re

str = input("문자열을 입력하십시오")

def isPalindrome(s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            print("팰린드롬 문자열이 아닙니다")
            return False
    print("팰린드롬 문자열입니다")    
    return True

def isPalindrome2(s:str)->bool:
    # 자료형 데크로 선언
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            print("팰린드롬 문자열이 아닙니다")
            return False
        
    print("팰린드롬 문자열입니다")  
    return True

def isPalindrome3(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)  #정규화
    return s == s[::-1]      # 슬라이싱

isPalindrome3(str)