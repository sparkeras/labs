int_input = (input("enter a whole number please uwu ^_^ "))
negative = False
if type(int_input) == int:
    if int_input < 0:
        negative = True
elif type(int_input) == float:
    print("oh no its not an integer ouch owie")
converted_input = str(int_input)
if negative == True:
    print(converted_input[0:2])
else:
    print(converted_input[0])
