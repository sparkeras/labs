import time
print(time.ctime())
x = 10.5
print(f"x is equal to {x} but watch this!")
print(type(x))
for y in range(6):
    if type(x) == int:
        x = float(x)
        print(f"x = {x} and its data type is {type(x)}")
        time.sleep(2)
    elif type(x) == float:
        x = int(x)
        print(f"x = {x} and its data type is {type(x)}")
        time.sleep(2)
