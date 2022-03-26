#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call

def calculation(a,b):
    add=a+b;
    sub=a-b;
    return add,sub;

print(calculation(40,10))