## 2. Words Containing All Five Vowels 
VOWELS = set("aeiou")

count = 0

with open("sowpods.txt") as f:
    for word in f:
        word = word.strip()

        if VOWELS.issubset(set(word.lower())):
            print(word)
            count += 1

print(f"Total words with all vowels: {count}")

