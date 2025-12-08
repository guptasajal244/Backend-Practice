def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

l = list(map(int, input("Enter a list").split()))

print(f"The sum of the entered list is {sum_list(l)}")
