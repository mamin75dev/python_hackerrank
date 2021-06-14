n = int(input())

result = ''
if n % 2 != 0:
    result = "Weird"
else:
    if n >= 2 and n <= 5:
        result = "Not Weird"
    elif n >= 6 and n <= 20:
        result = "Weird"
    else:
        result = "Not Weird"

print(result)
