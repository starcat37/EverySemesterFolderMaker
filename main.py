#path = C:\Users\User\Desktop\학교\강의

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory): os.makedirs(directory)
    except OSError: print("Error")

#과목명이 공백일 경우 오류 반환 필요 -> 용도별 함수 나눠야 하나?   

def createweekFolder(num, directory):
    for i in range(1, int(num)+1): os.makedirs(directory+'\\'+str(i)+'주차')

print("""
    *** 매 학기 학습 폴더 생성 ***

""")

path = input("최초 경로 입력 : ")
date_name = input("학년-학기 입력(ex. 2학년 1학기일 경우 2-1) : ")

createFolder(path+'\\'+date_name)
new_path = path + '\\' + date_name

course_list = []

course_num = int(input("과목수 입력 : "))
for i in range(course_num):
    course = input("과목명(폴더명) 입력: ")
    course_list.append(course)
    createFolder(new_path+'\\'+course)
    print(course +" 폴더 생성 완료")

answer = input("매 주차 폴더를 생성하시겠습니까?(Y/N) : ")
if answer == "Y":
    num = (input("몇 주차만큼 생성하시겠습니까?(숫자 입력) : "))
    for i in course_list: createweekFolder(num, new_path+'\\'+i)

print("생성 완료")