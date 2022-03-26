#Python Program for cube sum of first n natural numbers
def sum_cube(n):
   x=(n * (n+1)/2)
   return int(x*x)

n=int(input("Enter limit: "))
cube_sum=sum_cube(n)
print(cube_sum)