a = int(input("Enter a Number = "))

if a == 0:
    print(f"{a} is neither even nor odd")
elif a%2 == 0:
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")
    
    