keys1 = ('a', 'b', 'c', 'd')
keys2 = ('e', 'f', 'g', 'h')
values1 = [ 'smtp1', 'smtp2', 'smtp3']
values2 = [ 'smtp4', 'smtp5', 'smtp6']
stuff = { keys1:values1, keys2:values2} 

for email,smtp in stuff.items():
   print(email,smtp) 
