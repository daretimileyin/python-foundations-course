# Module 05 – Strings in Depth

## 🎯 Learning objectives
By the end of this module you will be able to:
- Index and slice strings
- Use the most important string methods
- Split text into words and join lists into text
- Clean and validate user input
- Format output in tables using f-string alignment
- Understand that strings are **immutable**

---

## 📖 Concepts

### 1. Strings are sequences
```python
word = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5
#      -6 -5 -4 -3 -2 -1
word[0]      # 'P'
word[-1]     # 'n'
word[0:3]    # 'Pyt'
word[::-1]   # 'nohtyP'
len(word)    # 6
for char in word:
    print(char)
```

### 2. Strings are immutable
```python
word[0] = "J"           # ❌ TypeError
word = "J" + word[1:]   # ✅ create a NEW string: "Jython"
```
String methods always **return a new string**. They never change the original.

### 3. Changing case
```python
s = "hello World"
s.upper()        # 'HELLO WORLD'
s.lower()        # 'hello world'
s.title()        # 'Hello World'
s.capitalize()   # 'Hello world'
s.swapcase()     # 'HELLO wORLD'
```

### 4. Cleaning
```python
"   hi   ".strip()     # 'hi'
"   hi   ".lstrip()    # 'hi   '
"xxhixx".strip("x")    # 'hi'
"a-b-c".replace("-", " ")   # 'a b c'
```

### 5. Searching
```python
s = "I love Python. Python is great."
"Python" in s          # True
s.find("Python")       # 7  (index of first match, -1 if not found)
s.count("Python")      # 2
s.startswith("I")      # True
s.endswith(".")        # True
```

### 6. Checking content
```python
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
"Hello".isupper()    # False
```

### 7. Split and join ⭐ very common
```python
sentence = "the quick brown fox"
words = sentence.split()          # ['the', 'quick', 'brown', 'fox']
"a,b,c".split(",")                # ['a', 'b', 'c']
" ".join(words)                   # 'the quick brown fox'
"-".join(["2026", "10", "19"])    # '2026-10-19'
```

### 8. Multi-line strings
```python
poem = """Roses are red,
Violets are blue."""
lines = poem.splitlines()
```

### 9. Formatting tables with f-strings
```python
items = [("Apple", 0.5, 10), ("Watermelon", 3.25, 2)]
print(f"{'Item':<12}{'Price':>8}{'Qty':>5}")
for name, price, qty in items:
    print(f"{name:<12}{price:>8.2f}{qty:>5}")
```
```
Item           Price  Qty
Apple           0.50   10
Watermelon      3.25    2
```
`<` left, `>` right, `^` centre; the number is the width.

### 10. Characters and codes
```python
ord("A")    # 65
chr(66)     # 'B'
```
Useful for simple ciphers!

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_string_basics.py`](examples/01_string_basics.py) | Indexing, slicing, methods |
| [`02_split_join_format.py`](examples/02_split_join_format.py) | split/join, cleaning input, table formatting |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_initials.py` | ⭐ | Turn a full name into initials |
| 2 | `ex02_email_validator.py` | ⭐⭐ | Basic email checker |
| 3 | `ex03_caesar_cipher.py` | ⭐⭐ | Encrypt and decrypt text |
| 4 | `ex04_password_strength.py` | ⭐⭐ | Rate a password's strength |
| 5 | `ex05_acronyms_and_slugs.py` | ⭐⭐⭐ | Make acronyms and URL slugs |

---

## 🛠️ Mini-project: Word Counter
Create `exercises/word_counter.py`. The user pastes a paragraph and the program reports:
- number of characters (with and without spaces)
- number of words and sentences
- the average word length
- the 5 most common words (ignore case and punctuation)
- the longest word

**Bonus:** ignore common "stop words" (`the`, `a`, `and`, `is`…) in the top-5 list.

---

## ⚠️ Common mistakes
- Calling a method but not saving the result: `name.upper()` alone does nothing useful; use `name = name.upper()`.
- `"5" + 5` → `TypeError`.
- `.split()` with no argument splits on any whitespace; `.split(" ")` splits on single spaces only (and can create empty strings).
- Comparing user input without cleaning it: `"Yes " != "yes"`. Use `.strip().lower()`.

## 🔗 Resources
- [Python docs: String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python: Strings and Character Data](https://realpython.com/python-strings/)
- [Python docs: Format Specification](https://docs.python.org/3/library/string.html#format-specification-mini-language)

## ✅ Checklist
- [ ] I can slice any part of a string
- [ ] I know what "immutable" means
- [ ] I can use `split()` and `join()` confidently
- [ ] I can clean input with `.strip().lower()`
- [ ] I can print an aligned table
- [ ] I built the word counter
