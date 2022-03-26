#exception handling

try:
    list=[2,0,3]
    listr=list[0]/list[3]
    print(listr)
except (ZeroDivisionError,IndexError):
    print("Division is invalid")

finally:
    print("successful")