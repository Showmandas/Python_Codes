# Python Program for compound interest

p=int(input("Enter principle amount"))
t=int(input("Enter time"))
r=float(input("Enter rate"))

def compound_int(p,t,r):
    a=p*(pow((1+r/100),t))
    ci=a-p
    print("Compound Interest :",ci)

compound_int(p,t,r)
