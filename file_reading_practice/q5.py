##5. Words in sonnet_words.txt but NOT in sowpods.txt
# Read all SOWPODS words into a set
with open("sowpods.txt") as f:
    sowpods = {word.strip().lower() for word in f}

with open("sonnet_words.txt") as f:
    sonnet_words = {word.strip().lower() for word in f}

unique_words = sorted(sonnet_words - sowpods)

print("Words in sonnet but not in sowpods:")
print(unique_words)
print(f"Total: {len(unique_words)}")