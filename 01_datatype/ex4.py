# 문자열(str)
# "", ''

a = "python"  # 큰 따옴표 권장
print(a, type(a))

print("I'll be back")
# print('I\'ll be back') -> 그냥 저장하면'' -> ""로 수정돼서,.,.. 주석처리합니다

# 여러줄 문자열
a = """
Life is short
You need Python
"""
print(a)


# docstring
def func():
    """
    func 함수에 대한 설명 작성
    """
    # 꼭 첫번째에 있어야 출력됨
    pass


print(func.__doc__)

# 문자열 연결
print("Hello" + " Python")

# 문자열 반복
print("Hello" * 10)
print("-" * 50)

# 문자열 연산 시 주의사항
# print("Hello" + 10) -> x. +연산은 같은 자료형끼리 ex) 문자열, 문자열
print("Hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포멧팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:15,d}")
print(f"{num:<15,d}")
print(f"{num:015,d}")
