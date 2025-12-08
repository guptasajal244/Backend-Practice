def count_vowels(sentence):
    count = 0
    for i in sentence:
        if i.lower() in "aeiou":
            count += 1
    return count
    
    
print(count_vowels("My name is sajal gupta"))
