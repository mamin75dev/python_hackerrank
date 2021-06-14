'''
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
123...n
'''

n = int(input())
result = ''
for i in range(1, n+1):
  result = f'{result}{i}'

print(result)


