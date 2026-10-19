def count_vowels(text):
    count = 0
    for char in text.lower():          # BUG 1: uppercase vowels weren't counted
        if char in "aeiou":
            count += 1
    return count


def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))   # BUG 2: list.reverse() returns None


def grade(score):
    if score >= 90:                    # BUG 3: > excluded the boundary (90 should be A)
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"


def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):      # BUG 4: started at 1, skipping the first item
        total += numbers[i]
    return total


assert count_vowels("HELLO world") == 3
assert reverse_words("one two three") == "three two one"
assert grade(90) == "A"
assert grade(80) == "B"
assert sum_list([1, 2, 3]) == 6
print("✅ All bugs fixed!")
