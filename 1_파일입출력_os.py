
import os


########## 현재 작업 폴더와 파일 존재 여부 확인

# 현재 작업 폴더
print(os.getcwd())

# 파일 존재 여부
if os.path.exists("ranking.txt"):
    print("파일이 있습니다.")
else:
    print("파일이 없습니다.")





########## 