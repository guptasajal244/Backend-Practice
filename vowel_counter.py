input = "My name is sajal gupta"

count = 0
for i in input:
    if i.lower() in "aeiou":
        count += 1
    
print(f"Vowel count is {count}.")

