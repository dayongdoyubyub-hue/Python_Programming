# 반복문 : while문, for문

# while문
# 1~10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
a = 0
while a <= 4:
    if nums[a] == target:
        print("found")
        break
    a += 1
else:
    print("not found")

# 1~10까지의 합
i = 1
tot = 0

while i <= 10:
    tot += i
    i += 1
else:
    print(f"합: {tot}")


i = 2
tot = 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
else:
    print(f"합: {tot}")

i = 1
tot = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i
else:
    print(f"합: {tot}")
