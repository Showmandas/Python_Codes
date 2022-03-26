# Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sublist= ["h", "i", "j"]
list1[2][1][2].extend(Sublist)
print(list1)