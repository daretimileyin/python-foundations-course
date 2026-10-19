text = """the cat sat on the mat the dog sat on the log
the cat saw the dog and the dog saw the cat"""

counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word, 0) + 1

for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word}: {count}")
