import turtle

t = turtle.Turtle()



leaf = turtle.Turtle()
leaf.shape("turtle")
leaf.speed(0)


def draw_leaf():
    leaf.color("#1257a5")
    leaf.begin_fill()
    leaf.circle(180, 90) 
    leaf.left(90)
    leaf.circle(180, 90) 
    leaf.left(90)
    leaf.end_fill()


leaf.goto(-50, 0)
leaf.pendown()
draw_leaf()

leaf.lt(180)
leaf.pu()
leaf.fd(25)  
leaf.pd()
leaf.rt(135)  


leaf.begin_fill()
leaf.circle(180, 90)
leaf.left(90)
leaf.circle(180, 90)
leaf.left(90)
leaf.end_fill()


leaf.lt(120)
leaf.pu()
leaf.fd(25)  
leaf.pd()
leaf.rt(72)  


leaf.begin_fill()
leaf.circle(180, 90)
leaf.left(90)
leaf.circle(180, 90)
leaf.left(90)
leaf.end_fill()

leaf.width(15)

leaf.pu()
leaf.color("white")
leaf.fd(85)
leaf.rt(92.79)
leaf.pd()
leaf.bk(300)
leaf.fd(550)




leaf.rt(90)
leaf.fd(30)
leaf.rt(90)
leaf.fd(700)


leaf.lt(90)
leaf.fd(30)
leaf.lt(90)
leaf.fd(700)


leaf.pu()


leaf.color("#1257a5")
leaf.rt(90)
leaf.fd(90)
leaf.rt(90)
leaf.fd(400)
leaf.pd()


leaf.circle(30)
leaf.rt(180)
leaf.pu()
leaf.fd(35)
leaf.rt(90)
leaf.pd()
leaf.fd(60)
leaf.lt(90)
leaf.pu()
leaf.fd(45)


leaf.pd()

leaf.circle(30)
leaf.pu()
leaf.fd(38)
leaf.lt(89)
leaf.pd()
leaf.fd(80)
leaf.bk(80)
leaf.pu()
leaf.rt(90)
leaf.fd(25)
leaf.pd()

leaf.lt(91)
leaf.fd(45)
leaf.pu()
leaf.fd(20)
leaf.pd()

leaf.circle(1)
leaf.pu()
leaf.bk(65)


leaf.rt(90)
leaf.fd(48)
leaf.pd()



leaf.circle(30)
leaf.pu()
leaf.fd(38)
leaf.lt(89)
leaf.pd()
leaf.fd(80)
leaf.bk(80)
leaf.pu()
leaf.rt(90)
leaf.fd(45)
leaf.pd()

leaf.circle(30)
leaf.pu()
leaf.lt(180)
leaf.bk(35)
leaf.rt(90+90)
leaf.pd()

leaf.lt(90)
leaf.fd(61)
leaf.bk(61)

leaf.pu()
leaf.rt(90)
leaf.pu()
leaf.fd(28)
leaf.pd()





leaf.circle(20, 152)
leaf.rt(170)
leaf.circle(20, -152)



