#if else,while,for 
import turtle
madhu_turtle = turtle.Turtle()
#square
def square():
  madhu_turtle.forward(100)
  madhu_turtle.right(90)
  madhu_turtle.forward(100)
  madhu_turtle.right(90)
  madhu_turtle.forward(100)
  madhu_turtle.right(90)
  madhu_turtle.forward(100)
  madhu_turtle.right(90)
  
 
m1=1
m2=3
if m2>m1:
  square()
#runs infinite times
#while True:
#  square()

if m2<m1:
  square()
else:
  madhu_turtle.forward(100)
  

while(m1<m2):
  square()
  m1+=1

for i in range(10):
  square()

print(i)










#








  
 