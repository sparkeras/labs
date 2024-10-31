total = 0
for x in range(0,101):
    if x % 2 == 0:
        if x % 3 != 0:
            print(x)
            total = total + x
        else:
            continue
    else:
        continue
print(total)
