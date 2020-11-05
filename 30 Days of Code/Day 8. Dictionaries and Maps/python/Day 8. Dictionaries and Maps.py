# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = dict()
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

name = input()
while name:
    try:
        print(f"{name}={phone_book[name]}")
    except:
        print("Not found")
        
    try:
        name = input()
    except EOFError:
        break
