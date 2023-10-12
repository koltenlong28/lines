# importing turtle module 
import turtle 
  
# size
n = 1000000


# creating instance of turtle 
pen = turtle.Turtle() 



pen.speed(0)
turtle.bgcolor("black")
pen.color("white")

# loop to draw a side 
for i in range(n * 5): 
    
    # drawing side of 
    # length i*10 
    pen.forward(i * 0.07) 
      
    # changing direction of pen 
    # by 120 degree in clockwise 
    pen.right(25)
      
# closing the instance 
turtle.done() 
