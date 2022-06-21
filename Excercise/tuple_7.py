#Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
def sort_by_second_item(tuple1):
    return (sorted(tuple1,key=lambda x:x[1]))

print(sort_by_second_item(tuple1))