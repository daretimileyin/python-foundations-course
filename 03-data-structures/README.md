# Module 03 – Data Structures

## 🎯 Learning objectives
By the end of this module you will be able to:
- Store collections of data in **lists**, **tuples**, **dictionaries** and **sets**
- Access items by index and by key, and slice lists
- Add, remove, sort and search items
- Loop over collections (including with `enumerate()` and `.items()`)
- Choose the right data structure for the job
- Write simple list and dictionary comprehensions

---

## 📖 Concepts

### 1. Lists: ordered, changeable collections
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])      # apple   (indexes start at 0!)
print(fruits[-1])     # cherry  (negative = from the end)
print(len(fruits))    # 3

fruits[1] = "blueberry"     # change an item
fruits.append("date")       # add to the end
fruits.insert(0, "avocado") # add at a position
fruits.remove("cherry")     # remove by value
last = fruits.pop()         # remove and return the last item
print("apple" in fruits)    # True (membership test)
```

**Slicing** `list[start:stop:step]` (stop is not included):
```python
nums = [0, 1, 2, 3, 4, 5, 6]
nums[1:4]    # [1, 2, 3]
nums[:3]     # [0, 1, 2]
nums[4:]     # [4, 5, 6]
nums[::2]    # [0, 2, 4, 6]
nums[::-1]   # [6, 5, 4, 3, 2, 1, 0]  (reversed)
```

**Useful list tools:**
```python
scores = [70, 95, 82, 61]
scores.sort()                 # sorts in place → [61, 70, 82, 95]
scores.sort(reverse=True)
sorted(scores)                # returns a NEW sorted list
sum(scores), min(scores), max(scores)
scores.count(70), scores.index(95)
```

### 2. Looping over lists
```python
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### 3. Tuples: ordered, **unchangeable**
```python
point = (3, 4)
x, y = point            # unpacking
print(point[0])         # 3
point[0] = 10           # ❌ TypeError: tuples can't be changed
```
Use tuples for data that shouldn't change: coordinates, RGB colours, dates.

### 4. Dictionaries: key → value pairs
```python
person = {
    "name": "Ada",
    "age": 36,
    "languages": ["English", "French"],
}

print(person["name"])              # Ada
print(person.get("email"))         # None (no error if missing)
print(person.get("email", "N/A"))  # N/A  (default value)

person["email"] = "ada@example.com"   # add or update
del person["age"]                     # delete
print("name" in person)               # True (checks keys)

for key, value in person.items():
    print(f"{key}: {value}")

person.keys()     # all keys
person.values()   # all values
```

### 5. Sets: unordered, **unique** items
```python
tags = {"python", "code", "python"}
print(tags)           # {'python', 'code'} (duplicates removed)
tags.add("fun")

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # union        {1, 2, 3, 4}
a & b    # intersection {2, 3}
a - b    # difference   {1}

unique = list(set([1, 1, 2, 3, 3]))   # remove duplicates from a list
```

### 6. Which one should I use?
| Need | Use |
|------|-----|
| An ordered list of things that may change | `list` |
| A fixed group of values | `tuple` |
| Look things up by a name/key | `dict` |
| Unique items / fast "is it in here?" checks | `set` |

### 7. Nesting
```python
students = [
    {"name": "Ada", "grades": [90, 85]},
    {"name": "Alan", "grades": [78, 88]},
]
print(students[1]["grades"][0])   # 78
```

### 8. Comprehensions: build collections in one line
```python
squares = [n ** 2 for n in range(1, 6)]           # [1, 4, 9, 16, 25]
evens = [n for n in range(20) if n % 2 == 0]
upper = [word.upper() for word in ["hi", "yo"]]   # ['HI', 'YO']
lengths = {word: len(word) for word in ["cat", "horse"]}  # {'cat': 3, 'horse': 5}
```
These are the same as a `for` loop with `.append()`, just shorter.

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_lists.py`](examples/01_lists.py) | Creating, changing, slicing, sorting lists |
| [`02_dictionaries.py`](examples/02_dictionaries.py) | Dictionaries and nesting |
| [`03_tuples_sets_comprehensions.py`](examples/03_tuples_sets_comprehensions.py) | Tuples, sets, comprehensions |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_list_stats.py` | ⭐ | Sum, average, min and max of a list |
| 2 | `ex02_shopping_list.py` | ⭐ | Interactive add/remove/show shopping list |
| 3 | `ex03_word_frequency.py` | ⭐⭐ | Count how often each word appears |
| 4 | `ex04_remove_duplicates.py` | ⭐⭐ | Remove duplicates while keeping order |
| 5 | `ex05_student_grades.py` | ⭐⭐ | Average grade per student from nested data |
| 6 | `ex06_comprehensions.py` | ⭐⭐⭐ | Rewrite loops as comprehensions |

---

## 🛠️ Mini-project: Contact Book
Create `exercises/contact_book.py`, a menu-driven program that stores contacts in a dictionary:
```
1. Add contact
2. View all contacts
3. Search contact
4. Delete contact
5. Quit
```
Each contact: `{"phone": "...", "email": "..."}` stored under the contact's name.

**Bonus:** list contacts in alphabetical order; let the user update an existing contact; search by partial name.

---

## ⚠️ Common mistakes
- `IndexError: list index out of range`: the last index is `len(lst) - 1`.
- `KeyError`: the key doesn't exist. Use `.get()` or check with `in` first.
- `sorted_list = my_list.sort()` ❌ `.sort()` returns `None`! Use `sorted(my_list)` for a new list.
- Changing a list while looping over it skips items. Loop over a copy: `for x in my_list[:]:`
- `b = a` doesn't copy a list, both names point to the **same** list. Use `b = a.copy()`.

## 🔗 Resources
- [Python docs: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python: Dictionaries](https://realpython.com/python-dicts/)

## ✅ Checklist
- [ ] I know which structure to use and why
- [ ] I can slice a list and reverse it
- [ ] I can loop over a dictionary's keys and values
- [ ] I can write a list comprehension with a condition
- [ ] I built the contact book
