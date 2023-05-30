
## Check given number is special or not??

n=int(input("Enter n value: "))
num=n
sum=0
while num>0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
    num=num//10
if sum == n:
    print(f'{n} is a special number')
else:
    print(f'{n} is not a special number')

