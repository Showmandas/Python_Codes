#Reverse an Integer

rev=0;
n=1234;
while n != 0:
    remainder = n % 10;
    rev = rev * 10 + remainder;
    n=n // 10;
print("Reversed number ",rev);