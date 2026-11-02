# Python DSA Basics - Day 1 (2026-11-02)
# Lessons: list, dict, set + the "go through items one by one, remember something" pattern


# ---------- Lesson 1: list ----------
# A list is a row of numbered boxes. Index starts at 0.
marks = [70, 85, 60, 90, 75]

# Find the biggest mark without max()
biggest = marks[0]
for m in marks:
    if m > biggest:
        biggest = m
print("Biggest:", biggest)    # 90

# Find the smallest mark (flip > to <)
smallest = marks[0]
for m in marks:
    if m < smallest:
        smallest = m
print("Smallest:", smallest)  # 60


# ---------- Lesson 2: dict ----------
# A dict looks things up by key (like a contact list). Lookup is instant.
nums = [4, 7, 4, 2, 7, 4]     # [ ] = list. { } with values only = set (removes duplicates!)
count = {}
for n in nums:
    if n in count:
        count[n] = count[n] + 1
    else:
        count[n] = 1
print("Counts:", count)       # {4: 3, 7: 2, 2: 1}

# Number that appears the most (same idea as "find the biggest")
best_num = None
best_count = 0
for n in count:
    if count[n] > best_count:
        best_count = count[n]
        best_num = n
print("Most frequent:", best_num)  # 4


# ---------- Lesson 3: set ----------
# A set is a bag of unique items: "have I seen this before?"
# Contains duplicate? (LeetCode 217, solved in C in Arrays/0217-contains-duplicate.c)
nums = [3, 1, 4, 1, 5]
seen = set()
found = False
for n in nums:
    if n in seen:
        found = True
    else:
        seen.add(n)
print("Has duplicate:", found)  # True
