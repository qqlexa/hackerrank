# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    user_input = input()
    even_output = "".join([c for i, c in enumerate(user_input) if not i % 2])
    odd_output = "".join([c for i, c in enumerate(user_input) if i % 2])
    print(f"{even_output} {odd_output}")
