"""Mini-project solution – Word Counter."""

STOP_WORDS = {"the", "a", "an", "and", "is", "are", "of", "to", "in", "it", "on", "for"}


def clean_word(word):
    return "".join(ch for ch in word.lower() if ch.isalnum() or ch == "'")


def analyse(text):
    words = [clean_word(w) for w in text.split()]
    words = [w for w in words if w]
    sentences = sum(text.count(mark) for mark in ".!?")

    counts = {}
    for w in words:
        if w not in STOP_WORDS:
            counts[w] = counts.get(w, 0) + 1
    top5 = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:5]

    print(f"Characters (with spaces):    {len(text)}")
    print(f"Characters (without spaces): {len(text.replace(' ', ''))}")
    print(f"Words:                       {len(words)}")
    print(f"Sentences:                   {sentences}")
    if words:
        print(f"Average word length:         {sum(len(w) for w in words) / len(words):.1f}")
        print(f"Longest word:                {max(words, key=len)}")
    print("Top 5 words:")
    for word, count in top5:
        print(f"  {word:<15}{count}")


def main():
    text = input("Paste your text:\n")
    analyse(text)


if __name__ == "__main__":
    main()
