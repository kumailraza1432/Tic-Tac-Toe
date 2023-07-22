import random
number = 0
while number != 2:
    point1 = 1
    point2 = 2
    point3 = 3
    point4 = 4
    point5 = 5
    point6 = 6
    point7 = 7
    point8 = 8
    point9 = 9
    print("WELCOME TO THE TIC-TAK TOE GAME")
    print ("",point1,"|",point2,"|",point3
      ,"\n","-","|","-","|","-\n"
      ,point4,"|",point5,"|",point6
      ,"\n","-","|","-","|","-\n"
      ,point7,"|",point8,"|",point9,"")
    level = eval(input("ENTER THE MODE TYPE, PRESS 1 FOR SINGLE PLAYER AND 2 FOR MULTIPLAYER: "))
    if level == 2:
           print("YOU HAVE ENTER MULTIPLAYER MODE")
           name1 = input("ENTER PLAYER 1 NAME= ")
           name2 = input("ENTER PLAYER 2 NAME= ")
           sign = eval(input("PLAYER 1 SELECT THE SYMBOL, 1 FOR X AND 2 FOR O: "))
           if sign == 1:
               name1 = "x"
               name2 = "o"
           else:
               name1 = "o"
               name2 = "x"
           toss = random.randint(1,2)
           if toss == 1:
               print(name1, "HAVE WON THE TOSS")
               k = 1
           elif toss == 2:
               print(name2, "HAVE WON THE TOSS")
               k =2

           counter = 0
           while counter < 9:
               if k == 1:
                   value1 = eval(input("Enter a number between 1 to 9 "))
                   if value1 == 1 and point1 != name1 and point1 != name2 :
                       point1 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 2 and point2 != name1 and point2 != name2 :
                       point2 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif value1 == 3 and point3 != name1 and point3 != name2 :
                       point3 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 4 and point4 != name1 and point4 != name2 :
                       point4 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif   value1 == 5 and point5 != name1 and point5 != name2 :
                       point5 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 6 and point6 != name1 and point6 != name2 :
                       point6 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 7 and point7 != name1 and point7 != name2 :
                       point7 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 8 and point8 != name1 and point8 != name2 :
                       point8 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 9 and point9 != name1 and point9 != name2 :
                       point9 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")    
                   elif value1 != 1 and value1 != 2 and value1 != 3 and value1 != 4 and value1 != 5 \
                        and value1 != 6 and value1 != 7 and value1 != 8 and value1 != 9 :
                        print("Invalid input!Try again!")
                        continue
                   else:
                        print("The spot is already taken!Enter again!")
                        continue
                   k = 2
                   counter += 1
                   if (point1 == point2 == point3 or point4 == point5 == point6 or point7 == point8 == point9 or point2 == point4 == point6 or point1 == point5 == point9 or point3 == point6 == point9 or point2 == point5 == point8 or point3 == point6 == point9):
                        print(name1 , " wins the game")
                        break
                   if counter == 9:
                        print("Oops its a draw!")
                        break
            

               elif k ==2 :
                   value2 = eval(input("Enter a number between 1 to 9: "))
                   if value2 == 1 and point1 != name1 and point1 != name2 :
                       point1 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 2 and point2 != name1 and point2 != name2 :
                       point2 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif value2 == 3 and point3 != name1 and point3 != name2 :
                       point3 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 4 and point4 != name1 and point4 != name2 :
                       point4 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif   value2 == 5 and point5 != name1 and point5 != name2 :
                       point5 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 6 and point6 != name1 and point6 != name2 :
                       point6 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 7 and point7 != name1 and point7 != name2 :
                       point7 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 8 and point8 != name1 and point8 != name2 :
                       point8 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 9 and point9 != name1 and point9 != name2 :
                       point9 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")    
                   elif value2 != 1 and value2 != 2 and value2 != 3 and value2 != 4 and value2 != 5 \
                        and value2 != 6 and value2 != 7 and value2 != 8 and value2 != 9 :
                        print("Invalid input!Try again!")
                        continue
                   else:
                        print("The spot is already taken!Enter again!")
                        continue
                   k = 1
                   counter += 1
                   if (point1 == point2 == point3 or point4 == point5 == point6 or point7 == point8 == point9 or point2 == point4 == point6 or point1 == point5 == point9 or point3 == point6 == point9 or point2 == point5 == point8 or point3 == point6 == point9):
                        print(name2 , " wins the game")
                        break
                   if counter == 9:
                        print("Oops its a draw!")
                        break
    elif level == 1:
           print("YOU HAVE ENTER SINGLE PLAYER MODE")
           name1 = input("ENTER PLAYER 1 NAME= ")

           sign = eval(input("PLAYER 1 SELECT THE SYMBOL, 1 FOR X AND 2 FOR O: "))
           if sign == 1:
               name1 = "x"
               name2 = "o"
           else:
               name1 = "o"
               name2 = "x"
           toss = random.randint(1,2)
           if toss == 1:
               print(name1, "HAVE WON THE TOSS")
               k = 1
           elif toss == 2:
               print(name2, "HAVE WON THE TOSS")
               k =2

           counter = 0
           while counter < 9:
               if k == 1:
                   value1 = eval(input("Enter a number between 1 to 9: "))
                   if value1 == 1 and point1 != name1 and point1 != name2 :
                       point1 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 2 and point2 != name1 and point2 != name2 :
                       point2 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif value1 == 3 and point3 != name1 and point3 != name2 :
                       point3 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 4 and point4 != name1 and point4 != name2 :
                       point4 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif   value1 == 5 and point5 != name1 and point5 != name2 :
                       point5 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 6 and point6 != name1 and point6 != name2 :
                       point6 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 7 and point7 != name1 and point7 != name2 :
                       point7 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 8 and point8 != name1 and point8 != name2 :
                       point8 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value1 == 9 and point9 != name1 and point9 != name2 :
                       point9 = name1
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")    
                   elif value1 != 1 and value1 != 2 and value1 != 3 and value1 != 4 and value1 != 5 \
                        and value1 != 6 and value1 != 7 and value1 != 8 and value1 != 9 :
                        print("Invalid input!Try again!")
                        continue
                   else:
                        print("The spot is already taken!Enter again!")
                        continue
                   k = 2
                   counter += 1
                   if (point1 == point2 == point3 or point4 == point5 == point6 or point7 == point8 == point9 or point2 == point4 == point6 or point1 == point5 == point9 or point3 == point6 == point9 or point2 == point5 == point8 or point3 == point6 == point9):
                        print(name1 , " wins the game")
                        break
                   if counter == 9:
                        print("Oops its a draw!")
                        break
            

               elif k ==2 :
                   print("It is computer's turn")
                   #computer winning conditions
                   if(name2 == point2 and name2 == point3 and name2 != point1 and name1 != point1) or (name2 == point4 and name2 == point7 and name1 != point1 and name2 != point1) or (name2 == point5 and name2 == point7 and name1 != point1 and name2 != point):
                       value2 = point1
                   elif(name2 == point1 and name2 == point3 and name2 != point2 and name1 != point2) or (name2 == point5 and name2 == point8 and name1 != point2 and name2 != point2):
                       value2 = point2
                   elif(name2 == point1 and name2 == point2 and name2 != point3 and name1 != point3) or (name2 == point5 and name2 == point7 and name1 != point3 and name2 != point3) or (name2 == point6 and name2 == point9 and name1 != point3 and name2 != point3):
                       value2 = point3
                   elif(name2 == point1 and name2 == point7 and name2 != point4 and name1 != point4) or (name2 == point5 and name2 == point6 and name1 != point4 and name2 != point4):
                       value2 = point4
                   elif(name2 == point2 and name2 == point8 and name2 != point5 and name1 != point5) or (name2 == point3 and name2 == point7 and name1 != point5 and name2 != point5) or (name2 == point4 and name2 == point6 and name1 != point5 and name2 != point5):
                       value2 = point5
                   elif(name2 == point3 and name2 == point9 and name2 != point6 and name1 != point6) or (name2 == point4 and name2 == point5 and name1 != point6 and name2 != point6):
                       value2 = point6
                   elif(name2 == point1 and name2 == point4 and name2 != point7 and name1 != point7) or (name2 == point8 and name2 == point9 and name1 != point7 and name2 != point7) or (name2 == point5 and name2 == point3 and name1 != point7 and name2 != point7):
                       value2 = point7
                   elif(name2 == point2 and name2 == point5 and name2 != point8 and name1 != point8) or (name2 == point7 and name2 == point9 and name1 != point8 and name2 != point8):
                       value2 = point8
                   elif(name2 == point7 and name2 == point8 and name2 != point9 and name1 != point9) or (name2 == point3 and name2 == point6 and name1 != point9 and name2 != point9) or (name2 == point5 and name2 == point1 and name1 != point9 and name2 != point9):
                       value2 = point9
                   #computer defending conditions
                   if(name1 == point2 and name1 == point3 and name2 != point1 and name1 != point1) or (name1 == point4 and name1 == point7 and name1 != point1 and name2 != point1) or (name1 == point5 and name1 == point7 and name1 != point1 and name2 != point):
                       value2 = point1
                   elif(name1 == point1 and name1 == point3 and name2 != point2 and name1 != point2) or (name1 == point5 and name1 == point8 and name1 != point2 and name2 != point2):
                       value2 = point2
                   elif(name1 == point1 and name1 == point2 and name2 != point3 and name1 != point3) or (name1 == point5 and name1 == point7 and name1 != point3 and name2 != point3) or (name1 == point6 and name1 == point9 and name1 != point3 and name2 != point3):
                       value2 = point3
                   elif(name1 == point1 and name1 == point7 and name2 != point4 and name1 != point4) or (name1 == point5 and name1 == point6 and name1 != point4 and name2 != point4):
                       value2 = point4
                   elif(name1 == point2 and name1 == point8 and name2 != point5 and name1 != point5) or (name1 == point3 and name1 == point7 and name1 != point5 and name2 != point5) or (name1 == point4 and name1 == point6 and name1 != point5 and name2 != point5):
                       value2 = point5
                   elif(name1 == point3 and name1 == point9 and name2 != point6 and name1 != point6) or (name1 == point4 and name1 == point5 and name1 != point6 and name2 != point6):
                       value2 = point6
                   elif(name1 == point1 and name1 == point4 and name2 != point7 and name1 != point7) or (name1 == point8 and name1 == point9 and name1 != point7 and name2 != point7) or (name1 == point5 and name1 == point3 and name1 != point7 and name2 != point7):
                       value2 = point7
                   elif(name1 == point2 and name1 == point5 and name2 != point8 and name1 != point8) or (name1 == point7 and name1 == point9 and name1 != point8 and name2 != point8):
                       value2 = point8
                   elif(name1 == point7 and name1 == point8 and name2 != point9 and name1 != point9) or (name1 == point3 and name1 == point6 and name1 != point9 and name2 != point9) or (name1 == point5 and name1 == point1 and name1 != point9 and name2 != point9):
                       value2 = point9
                    #difficult time hard go
                   elif point5 == name1 and counter == 1:
                    value2 = 1
                   elif counter == 1 and value1 != 5:
                    value2 = 5
                   elif (counter == 3) and (point2 == name1 and  point4 == name1) :
                    value2 = 1
                   elif (counter == 3) and (point2 == name1 and point5 == name1):
                    value2 = 3
                   elif (counter == 3) and (point8 == name1 and point6 == name1):
                    value2 = 9
                   elif (counter == 3) and (point8 == name1 and point4 == name1):
                    value2 = 7
                   elif counter == 0 :
                    value2 = 5
                   elif counter == 3 and (point1 == name1 and point9 == name1):
                    value2 = 6
                   elif counter == 3 and (point3 == name1 and point7 == name1):
                    value2 = 6
                   elif counter == 3 and (point4 == name1 and point9 == name1):
                    value2 = 7
                   elif counter == 3 and (point4 == name1 and point3 == name1):
                    value2 = 1
                   elif counter == 3 and (point2 == name1 and point9 == name1):
                    value2 = 3
                   elif counter == 3 and (point2 == name1 and point7 == name1):
                    value2 = 1
                   elif counter == 3 and (point5 == name1 and point1 == name1):
                    value2 = 3
                   elif counter == 3 and (point6 == name1 and point6 == name1):
                    value2 = 9
                   elif counter == 3 and (point8 == name1 and point3 == name1):
                    value2 = 9
                   elif counter == 3 and (point8 == name1 and point1 == name1):
                    value2 = 7
                   elif (counter == 5 or counter == 6 or counter == 7 or counter == 8 or counter == 9) and (point3 == name2 and point5 == name2):
                    value2 = 7
                   else:
                       value2 = random.randint(1,9)
                   if value2 == 1 and point1 != name1 and point1 != name2 :
                       point1 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 2 and point2 != name1 and point2 != name2 :
                       point2 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif value2 == 3 and point3 != name1 and point3 != name2 :
                       point3 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 4 and point4 != name1 and point4 != name2 :
                       point4 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif   value2 == 5 and point5 != name1 and point5 != name2 :
                       point5 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 6 and point6 != name1 and point6 != name2 :
                       point6 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 7 and point7 != name1 and point7 != name2 :
                       point7 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 8 and point8 != name1 and point8 != name2 :
                       point8 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")
                   elif  value2 == 9 and point9 != name1 and point9 != name2 :
                       point9 = name2
                       print ("",point1,"|",point2,"|",point3
                        ,"\n","-","|","-","|","-\n"
                       ,point4,"|",point5,"|",point6
                      ,"\n","-","|","-","|","-\n"
                      ,point7,"|",point8,"|",point9,"")    
                   elif value2 != 1 and value2 != 2 and value2 != 3 and value2 != 4 and value2 != 5 \
                        and value2 != 6 and value2 != 7 and value2 != 8 and value2 != 9 :
                        print("Invalid input!Try again!")
                        continue
                   else:
                        print("The spot is already taken!Enter again!")
                        continue
                   k = 1
                   counter += 1
                   if (point1 == point2 == point3 or point4 == point5 == point6 or point7 == point8 == point9 or point2 == point4 == point6 or point1 == point5 == point9 or point3 == point6 == point9 or point2 == point5 == point8 or point3 == point6 == point9):
                        print(name2 , " wins the game")
                        break
                   if counter == 9:
                        print("Oops its a draw!")

    play = input("Press y to play a new game otherwise n to exit: ")
    if play == "N" or play == "n":
        number = 2
        print(" Thanks for playing our game")
        break
    elif play == "Y" or start == "y":
        number = 1
                 
