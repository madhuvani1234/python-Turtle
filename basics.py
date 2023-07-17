#Data types
#4 premitive:integers,float,strings,booleans
#1,2,3 -integers
for i in range(10):
  print(i)

#1.23, -0.3778
print(1.23)
#"heyyyyyy"
m1 = "hii"
print(m1)

# True, False(yes,no)
print(m1.isupper())

#Cascading
#u can only print string in python print buildin automatically converts anyhting u give to string
#example
#err----------->print(1+"hii")
#so convert it to str and add
print(str(1) + "hii")
i = 1
print(type(i))
print(str(i))
print(float(i))
#printing ascii
print(chr(97))  #-->a
print(chr(33))  #-->!
print(ord('A'))  #-->65

#-----------STRINGS------------------------#
m1 = "hello"  #can also use ' '
print(m1[0])
print(m1.count('l'))
print(m1.capitalize())  #1st letter caps
print(m1.endswith('o'))
print(m1.replace('h', 'm'))
print('ello' in m1)
print(m1.find('ello'))
print(m1.isalnum())
print(m1.upper())
print(m1.split())  #retruns list
m2 = "hi my,name"
print(m2.split(','))  #['hi my','name']
#so many bulitin functions

#ARITHEMATIC OPERATORS:

print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10**3)

#-----------------list-----------------#
l1 = [1, 2, 3]
#bunch any data type elements
print(l1[0])
#-----function in lists-----#
names = ['madhu', 'mn', 1]
names.append('j1')  #adds at last
print(names)
names.insert(3, 'ram')
print(names)
names.remove('j1')
print(names)
names.reverse()
print(names)
print(names[0:])
print(names[1:3])  #prints index 1,2
print(names[::2])
print(names[::-2])


#input from console
l1=eval(input("enter list:"))
#give list at run time like this ['mad',1]
print(l1[0])
#prints mad
