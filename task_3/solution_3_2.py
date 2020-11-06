string = input()
alphabet = "" 
for i in string:
 if i not in alphabet:
  alphabet+=i
for s in range (1, 9):
 string = input()
 for k in string:
  if k not in alphabet:
   alphabet+=k
print (alphabet)
