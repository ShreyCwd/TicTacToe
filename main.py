import turtle

pen = turtle.Turtle ()
sc = turtle.Screen()
pen.speed (0)
numberlist = []
player1list = []
player2list = []

positionDict = {
    1:[-145,100],
    2:[0,100],
    3:[120,100],
    4:[-145,-25],
    5:[0,-25],
    6:[120,-25],
    7:[-145,-190],
    8:[0,-190],
    9:[120,-190]

}



def grid (pen):
    pen.penup ()
    pen.goto (-200, -200)
    pen.pendown ()

    for i in range (4):
        pen.forward (400)
        pen.left (90)


    pen.penup()
    pen.goto (-200, -65)
    pen.pendown ()
    pen.forward (400)

    pen.penup()
    pen.goto (-200, 75)
    pen.pendown ()
    pen.forward (400)

    pen.penup()
    pen.goto (-65, -200)
    pen.pendown ()
    pen.left (90)
    pen.forward (400)

    pen.penup()
    pen.goto (75, -200)
    pen.pendown ()
    pen.forward (400)


    pen.penup()
    pen.hideturtle()
    pen.goto (-195, 179)
    pen.write ('1', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (-60, 179)
    pen.write ('2', font = ('Arial', 15, ))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (80, 179)
    pen.write ('3', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (-195, 55)
    pen.write ('4', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (-60, 55)
    pen.write ('5', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (80, 55)
    pen.write ('6', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (-195, -85)
    pen.write ('7', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (-60, -85)
    pen.write ('8', font = ('Arial', 15))
    pen.penup()

    pen.penup()
    pen.hideturtle()
    pen.goto (80, -85)
    pen.write ('9', font = ('Arial', 15))
    pen.penup()

    pen.hideturtle()
    pen.penup()
    pen.goto (-200, -250)
    pen.write ('Player 1 - X', font = ('Arial', 20))

    pen.penup ()
    pen.goto (100, -250)
    pen.write ('Player 2 - O', font = ('Arial', 20))

def x (pen, position):
    if position == 1:
        pen.goto (positionDict[1][0], positionDict[1][1])
        pen.write ('X', font = ('Arial', 70, "bold"))

    elif position == 2:
        pen.goto (positionDict[2][0], positionDict[2][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

    elif position == 3:
        pen.goto (positionDict[3][0], positionDict[3][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

    elif position == 4:
        pen.goto (positionDict[4][0], positionDict[4][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

    elif position == 5:
        pen.goto (positionDict[5][0], positionDict[5][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

    elif position == 6:
        pen.goto (positionDict[6][0], positionDict[6][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

   

    elif position == 7:
        pen.goto (positionDict[7][0], positionDict[7][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))

    elif position == 8:
        pen.goto (positionDict[8][0], positionDict[8][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))


    elif position == 9:
        pen.goto (positionDict[9][0], positionDict[9][1])
        pen.write ("X", font = ('Arial', 70, 'bold'))


def o (pen, position):

    if position == 1:
        pen.goto (positionDict[1][0], positionDict[1][1])
        pen.write ("O", font = ('Arial', 70, "bold"))

    elif position == 2:
        pen.goto (positionDict[2][0], positionDict[2][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

    elif position == 3:
        pen.goto (positionDict[3][0], positionDict[3][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

    elif position == 4:
        pen.goto (positionDict[4][0], positionDict[4][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

    elif position == 5:
        pen.goto (positionDict[5][0], positionDict[5][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

    elif position == 6:
        pen.goto (positionDict[6][0], positionDict[6][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

   

    elif position == 7:
        pen.goto (positionDict[7][0], positionDict[7][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))

    elif position == 8:
        pen.goto (positionDict[8][0], positionDict[8][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))


    elif position == 9:
        pen.goto (positionDict[9][0], positionDict[9][1])
        pen.write ("O", font = ('Arial', 70, 'bold'))




grid (pen)

player1win = False
player2win = False

true = True
while True:
    if 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and 5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist: 
        break

    if player2win:
        print ('🎉 PLAYER-2 WON!! 🎉')
        break  

    elif player1win:
        print ('🎉 PLAYER-1 WON!! 🎉')
        break

    elif not player1win and not player2win  and 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and 5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist:
        print ('DRAW!')


    while True:
            position1 = input ('Player-1 (1-9): ')
            position1 = int (position1)
            if position1 >= 1 and position1 <= 9 and position1 not in numberlist:
                x (pen, position1)
                numberlist.append (position1)
                player1list.append(position1)

                if 1 in player1list and 2 in player1list and 3 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    player1win = True

                elif 2 in player1list and 5 in player1list and 8 in player1list:    
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[2][0]+20, positionDict[2][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[8][0]+20, positionDict[8][1]+20)
                    player1win = True

                elif 3 in player1list and 5 in player1list and 7 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    player1win = True

                elif 1 in player1list and 5 in player1list and 9 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player1win = True

                elif 4 in player1list and 5 in player1list and 6 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[4][0]+20, positionDict[4][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[6][0]+20, positionDict[6][1]+20)
                    player1win = True

                elif 7 in player1list and 8 in player1list and 9 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player1win = True

                elif 1 in player1list and 4 in player1list and 7 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    player1win = True

                elif 3 in player1list and 6 in player1list and 9 in player1list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player1win = True   

                break

        

    if 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and 5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist: 
        break            
    
    if player2win:
        print ('🎉 PLAYER-2 WON!! 🎉')
        break  

    elif player1win:
        print ('🎉 PLAYER-1 WON!! 🎉')
        break

    elif not player1win and not player2win  and 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and 5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist:
        print ('DRAW!')





    
  
    while True:
            position2 = input ('Player-2 (1-9): ')
            position2 = int (position2)
            if position2 >= 1 and position2 <= 9 and position2 not in numberlist:
                o (pen, position2)
                numberlist.append (position2)
                player2list.append(position2)

                if 1 in player2list and 2 in player2list and 3 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    player2win = True

                elif 2 in player2list and 5 in player2list and 8 in player2list:    
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[2][0]+20, positionDict[2][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[8][0]+20, positionDict[8][1]+20)
                    player2win = True

                elif 3 in player2list and 5 in player2list and 7 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    player2win = True

                elif 1 in player2list and 5 in player2list and 9 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player2win = True

                elif 4 in player2list and 5 in player2list and 6 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[4][0]+20, positionDict[4][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[6][0]+20, positionDict[6][1]+20)
                    player2win = True

                elif 7 in player2list and 8 in player2list and 9 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player2win = True

                elif 1 in player2list and 4 in player2list and 7 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[1][0]+20, positionDict[1][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[7][0]+20, positionDict[7][1]+20)
                    player2win = True

                elif 3 in player2list and 6 in player2list and 9 in player2list:
                    pen.penup()
                    pen.pensize (4)
                    pen.hideturtle()
                    pen.goto (positionDict[3][0]+20, positionDict[3][1]+20)
                    pen.pendown()
                    pen.color('red')
                    pen.goto (positionDict[9][0]+20, positionDict[9][1]+20)
                    player2win = True   

                break      
            
            


