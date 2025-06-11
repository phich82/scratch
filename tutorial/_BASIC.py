# Basic About Python Language

## 1. Declare a variable
y = 89
print(y)

## 2. Assign the value into variable
y = 100
print(y)

## 3. Comment in python

## 3. Data types
### 3.1 Integer (int): so nguyen
ty = 5768
print(ty)
print(type(ty))
### 3.2 Complex (complex): so phuc
io = 243570897250839574238j
print(io)
print(type(io)) #complex


### 3.3 Float (float) so thap phan

print(io)
print(type(io)) #float

## 4. Casting data (chuyen doi du lieu)
o = 90
n = 89.9
g = 78j

print(o)

oo = float(o)

print(oo)

## 5. Strings
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

## 6. Boolean
print(bool("Hello"))
print(bool(15))


## 7. Operators
print((6 + 3) - (6 + 3)) 

## 8. Basic data type
a = True
b = False
print(type(a))  # Output: <class 'bool'>
print(type(b))  # Output: <class 'bool'>


## 9.Condition statements
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

## 10. Loop

## 11. Functions 
def myFunction() :
  return True

print(myFunction()) 


## 12. Error Handler
try:
  print(x)
except:
  print("An exception occurred") 

## 13. Date
import datetime

x = datetime.datetime.now()
print(x) 

## 14. Math
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)






