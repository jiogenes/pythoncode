f = open("./basic/quiz/test.txt", "w", encoding='utf-8')

context = [
    "김말이","선생님","대한민국","능지처참","파이썬","프로그래밍",
    "빅파이","컴퓨터","마우스","아파트","산울림","햄버거","다이어리",
    "바밤바","세종실록지리지","6월민주항쟁","민주주의","자본주의",
    "양자역학","소고기","타로카드","대구광역시","서울특별시","타자게임",
    ]

for s in context:
    f.write(s)
    f.write("\n")

f.close()

f = open("./basic/quiz/test.txt", "r", encoding='utf-8')

for s in f.readlines():
    print(s, end='')

f.close()