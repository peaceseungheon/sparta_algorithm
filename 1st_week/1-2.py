def solution(num):
    if num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

num = int(input("숫자를 입력하세요:"))
solution(num)