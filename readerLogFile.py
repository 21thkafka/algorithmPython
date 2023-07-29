from typing import List

def readerLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
            print("digits : " + str(digits))
        else:
            letters.append(log)
            print("letters : " + str(letters))
    
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
logs = ["digi1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit idg", "let3 art zero"]
readerLogFiles(logs)