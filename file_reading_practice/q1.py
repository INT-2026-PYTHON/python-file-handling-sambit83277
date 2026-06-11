##1. Alphabets That Never Appear Back-to-Back 
seen = set()
doubled = set()
with open("sowpods.txt") as f:
    for word in f:
        word = word.strip().lower()

        # Record every letter seen
        seen.update(word)

        # Record letters that appear twice in a row
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                doubled.add(word[i])
answer = sorted(seen - doubled)
print("Letters that never appear back-to-back:")
print(answer)