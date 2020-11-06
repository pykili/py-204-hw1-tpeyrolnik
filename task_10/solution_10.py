s = input()
i = 0
n = len(s) - 1
while i < n:
 if s[i] == s[n]:
  is_palindrom = 'true'
 else:
  is_palindrom = 'false'
 i += 1
 n -= 1
print (is_palindrom)
