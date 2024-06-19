greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"
extened_grt2 = greet + "You are amazing!"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))