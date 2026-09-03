# for문

# for(int i=0; i<=10; i++)
# for i in iterable객체:

# 0 ~ 4
for i in range(5):
    print(i, end="")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end="")
print()

# 0 2 4 6 8
for i in range(0, 11, 2):
    print(i, end="")
print()

# 5 4 3 2 1
for i in range(5, 0, -1):
    print(i, end="")
print()

# 1~10까지의 합
tot = 0
for i in range(11):
    tot += i
else:
    print(f"sum = {tot}")

print(sum(range(1, 11)))

# sum = 0
# for i in range(11):
#     sum += i
# else:
#     print(f"sum = {sum}")
# print(sum(range(1, 11)))
# 위에 sum 변수후에 for문은 ㄱㅊ은데, sum 함수 없어짐 처리 한거여서 그럼!!, 아래 sum(range)->오류

s = "hi12!@안녕❤️👋"

for c in s:
    print(c, end="")
print()

print(len(s))

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<5d}", end="\t")
    print()
else:
    print("End")
