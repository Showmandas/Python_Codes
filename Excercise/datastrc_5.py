#Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
First_List  =[2, 3, 4, 5, 6, 7, 8]
Second_List  =[4, 9, 16, 25, 36, 49, 64]
result=zip(First_List,Second_List)
result_set=set(result)
print(set(result_set))

squarenum=[x**2 for x in range(0,10) if x%2==0]
print(squarenum)