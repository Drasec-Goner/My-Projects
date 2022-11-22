def table(num,i):
    if i>10:
        return
    print(f"{num} * {i} = {num*i}")
    return table(num,i+1)

n = int(input("Enter a range: "))

for x in range(1,n+1):
    print(f"The multiplication Table of {x} is:")
    table(x,1)
    print()