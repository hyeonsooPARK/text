

# file=open("test.txt","w",encoding="utf-8")   # "w" : 파일을 쓰겠다(생성)
# file.write("안녕하세요")    # 파일에 "안녕하세요"라고 써라
# file.close()              # close를 뒤에 안쓰는 경우도 있음


# with open("test.txt","w",encoding="utf-8")as file:     # with open을 쓰면 자동으로 닫아줌.
# 	file.write("안녕하세요")                            # close 안써도 됨


# 특정 폴더를 지정하여 저장하고 싶은데 폴더가 없을 시 자동으로 만들려면 import os 사용





########## 내용 변경
# file=open("test.txt","a",encoding="utf-8")
# file.write("좋은 아침")
# file.close()

# with open("memo.txt","w",encoding="utf-8")as file:
# 	file.write("1일차 학습\n")
# 	file.write("2일차 학습\n")
# 	file.write("3일차 학습\n")

# with open("memo.txt","r",encoding="utf-8")as file:
# 	content=file.read()    # 전체를 하나의 문자열로 읽음
# print(content)             # 1일차 학습
#                            # 2일차 학습
#                            # 3일차 학습





# with open("memo.txt","r",encoding="utf-8")as file:
# 	line1=file.readline()  # 한 줄씩 읽음
# 	line2=file.readline()
# print(line1)   # 1일차 학습
# print(line2)   # 2일차 학습


# with open("memo.txt","r",encoding="utf-8")as file:
# 	lines=file.readlines()  # 여러 줄 읽음
# print(lines)                #  ['1일차 학습\n', '2일차 학습\n', '3일차 학습\n']

# for line in lines:          # 이스케이프문자 빼고 내용만 가져오기
# 	print(line.strip()) 


# with open("memo.txt","a",encoding="utf-8")as file:
# 	file.write("4일차 학습\n")





# memo=input("메모를 입력하세요: ")

# with open("memo.txt","a",encoding="utf-8")as file:
# 	file.write(memo)





# 학생 점수 txt 파일 저장하기
students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n")   # 이렇게 저장된 값은 모두 "문자"


# 학생 점수 txt 파일 읽기
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)  # ['민수,85\n', '지수,92\n', '영희,55\n']

for line in lines:
    data = line.strip().split(",")   # data = ["민수", "85"]

    student = {                      # { "name":"민수", "score":85 }
        "name": data[0],
        "score": int(data[1])
    }

    students.append(student)
print(students)              # [{'name': '민수', 'score': 85}, {'name': '지수', 'score': 92}, {'name': '영희', 'score': 55}]





########## 예외처리와 연결하기

# 파일이 없는 경우
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    print(content)

# 숫자 변환 실패 처리
line = "민수,팔십오"
try:
    data = line.strip().split(",")
    name = data[0]
    score = int(data[1])
except ValueError:
    print("점수는 숫자로 입력해야 합니다.")
else:
    print(name, score)





########## 파일 입출력 함수로 묶기
def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)
