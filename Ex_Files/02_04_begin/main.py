NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

# Iterate through 2 collections at once
# This is done using "zip". It doesn't 
# create a new list in memory
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# Iterate collection in reverse
for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate is used to know 
# what index on when printing through
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
