data = [1, 2, 'a', 3.5,7,12,3,5,4,'10', 6, 'hello', 8]
even_numbers = []

for item in data:
    try:
        if isinstance(item, int) and item % 2 == 0:
            even_numbers.append(item)
    except TypeError:
        pass  

print(even_numbers)