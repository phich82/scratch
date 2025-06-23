# 1. String Type

t = "mai hack"
print(t)
print(type(t))
op = """kjdjkfjdkfjdfkdjfkdfjdkj
djfkdjfdkfjdkffdkfdjfdkj
djfkdfjkjfdkjfkdjk"""
print(op)

# 2. Numberic types (int, float, complex)
# 2.1 int
u = 9090909
print(u)
print('===> 2.1 int')
print(type(u))

# 2.2 float
lo = 9090909.99
print('===> 2.2 float')
print(lo)
print(type(lo))

# 2.3 complex
l = 9 + 9.8j
print('===> 2.3 complex')
print(l)
print(type(l))

# 3. Boolean type 
print("boolean=========>")
like = True #True/False
l = 9 < 7
print(like)
print(type(like))
print(l)
print(l == True)

# 4. Sequence types (list, tuple, range)
# 4.1 list
print('==========> list')
# Indexes    0          1           2     3  4
mylist = ['mumumu' , 'maimai' , 'jkjkkj', 3, 5]
print(mylist)
# Add new elements
mylist.append("new_element")
print(mylist)
# Total of elements in list
print(len(mylist))
# Print first element in list
print(mylist[0]) # 0: index of element (1st) in list
# Print middle element in list
print(mylist[1]) # 1: index of element (2nd) in list
# Print last element in list
last_element_index = len(mylist) - 1 # index of last belement in list
print(mylist[last_element_index]) # 0: index of element (last) in list
# Loop
for element in mylist:
  print(element)


# 4.2 tuple (no change of elements, no add new elements)
print('==========> tuple')
mytuples = ('mimimimimi' , 'mimimim' , 'ninin')
print(mytuples)
# Total of elements in tuples
print(len(mytuples))
# Print first element in tuples
print(mytuples[0]) # 0: index of element (1st) in tuples
# Print middle element in tuples
print(mytuples[1]) # 1: index of element (2nd) in tuples
# Print last element in tuples
last_element_index = len(mytuples) - 1 # index of last belement in tuples
print(mytuples[last_element_index]) # 0: index of element (last) in tuples
# Loop
for element in mytuples:
  print(element)

# 5. Set type (unchangable, no indexes, can add new element, delete element)
print('==========> set')

myset = {
  'cherry' ,
  'tuples' ,
  'complex'
}
print(myset)
# Add new elements
myset.add('apple')
myset.add('bromo')
print(myset)
# Delete element from set
myset.remove('bromo')
print(myset)
# Total of elements in set
print(len(myset))
# Loop
for element in myset:
  print(element)

# 6. dict (dictionary)
print('==========> dict')
thisdict =	{
  # <key>: <value>
  "brand": "nord",
  "model": "Mug",
  "year": 1909
}
print(thisdict)
# Print all keys in dict
print(thisdict.keys()) # list
# Print all values in dict
print(thisdict.values()) # list
# Print all elements in dict (list[tuple])
# thislist = [
#   ('brand', 'nord'), # tuple
#   ('model', 'Mug'), # tuple
#   ('year', 1909) # tuple
# ]
print(thisdict.items()) # list[tuple]
# Loop
for item in thisdict.items():
  # print(type(item)) # tuple
  key = item[0]
  value = item[1]
  # print(key, value)
  print(f"key: {key} - value: {value}")


# Access element in dict
print(thisdict['brand'])
print(thisdict['model'])

# Loop keys in dict
for key in thisdict.keys():
  print(f"key: {key} - value: {thisdict[key]}")


  










