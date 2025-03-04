# break => Terminates loop
# continue => Jumps to next loop

num = 100
while num > 0:
    num -= 1
    if num % 5 == 0:
        if num == 20:
            break
        continue
    print(num)
else:
    print("while loop ended")
