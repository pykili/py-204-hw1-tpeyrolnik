for i in 's'*10:
 string = input ()
 tab_count = 0
 form = ''
 lemma = ''
 if string != '' and string[0] != '#':
  for a in string:
   if a == '\t':
    tab_count += 1
   if tab_count == 1:
    form += a
   if tab_count == 2:
    lemma += a
  if form != lemma:
   print (form, lemma)
  
