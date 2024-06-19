NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

#This is using a "slice"
JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
# start an end are the colons
# And step back one at a time
REVERSE = NAMES[::-1]
# No start or stop, but step by 2
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
