# 불리언(bool)
# True, False

a = True
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("apple" > "banana")  # False

# bool()
print(bool(3))  # True
print(bool(0))  # False
# 0이 아닌 모든 정수 -> True, 0 -> False
print(bool("hello"))  # True
print(bool(""))  # False
print(bool([10]))  # True
print(bool([]))  # False

# None 자료형
a = None
print(a, type(a))
print(bool(a))  # False

if a is None:
    print("값이 없습니다.")
