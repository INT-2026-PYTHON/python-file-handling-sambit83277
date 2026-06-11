## 3. Find All Palindrome Words 
def is_palindrome(word):
    return word == word[::-1]

count = 0

with open("sowpods.txt") as f:
    for word in f:
        word = word.strip().lower()

        if is_palindrome(word):
            print(word)
            count += 1

print(f"Total palindromes: {count}")