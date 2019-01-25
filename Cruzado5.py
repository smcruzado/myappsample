DNA = raw_input('Enter DNA: ')
RNA = " "
for i in DNA:
	if i == 'T':
		RNA += "U"
	else:
		RNA += i
print RNA
