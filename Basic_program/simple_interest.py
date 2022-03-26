# Python Program for simple interest

p=int(input("Enter Principle amount: "))
t=int(input("Enter Time: "))
r=float(input("Enter Rate: "))

# s_i=(p*t*r)/100
#
# print("Simple interest :",sep=" ")
# print(s_i)

def simple_interest(p,t,r):
    s_i = (p * t * r) / 100
    return s_i

sim=simple_interest(p,t,r)
print(sim)
