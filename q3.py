first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Using %
print("Hey, %s %s!" % (first_name, last_name))

# Using str.format()
print("Hello, {} {}!".format(first_name, last_name))

# Using f-strings
print(f"Hi, {first_name} {last_name}!")