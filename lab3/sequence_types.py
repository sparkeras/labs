my_list = [100, 30, "programming", 3 + 4, "lab 3"]
print(len(my_list))
my_list.append(2.5)
print(len(my_list))
print(type(my_list[-1]))
my_list.insert(0, "bleh")
print(my_list)
my_list.remove(2.5)
print(my_list)
print(len(my_list))
print(my_list[0])
my_list[1] = 50
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple[0])
print(len(my_tuple))
try:
    my_tuple[0] = "pfft"
except:
    print("you cant edit tuples")
tuple2 = (4, 12, 25)
joined_tuple = my_tuple + tuple2
print(joined_tuple)
my_list = list(joined_tuple)
print(type(my_list))
my_set = set(my_list)
print(len(my_set))
my_set.add(32)
print(my_set)
my_set.add(12)
print(my_set)
set2 = {2, 4, 6}
new_set = my_set & set2
print(new_set)
