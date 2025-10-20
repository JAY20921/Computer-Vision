# print("a",5,True,sep='-', end =' ')
# print("2",2,sep=' ')
# a = 2 + 5j
# b = 3 + 2j
# A = a.real
# print ("mul = " ,a*b, "sum = " ,a + b, "conj =",A, sep='\n' )

     #Data types                              
# a = [[1,1,1],[1,4,2],[1,2,4]] #list 
# b = (1,1,1) #tuple
# c = {1,2,3} #sets
# d = ({"Name": "Jay", "Age" : 20,"DoB": "16/03/04"})
# a = input("email : ")
# print(type(a))

# a = int(input())
# b = int(input())
# c = complex(input())
# print(a+b+c)

#Literals
#numeric literals
# a = 0b100 #binary
# print(a) #4 in dec
# a = 100 #100 in dec
# c = 0o310 #octal
# print(c) #200 in dec
# d = 0x102 # hexadecimal
# print(d)#258 in dec

# #float
# float_1 = 10.5
# float_2 = 1.2e2
# float_3 = 1.53-4

# #complex 
# x = 1.12j

#String Literals
# string  = ' asda '
# string = " asda "
# char = "X"
# multiline_str = """This is multiline string with more than one line"""
# raw_string = r"Raw \n string"
# unicode  = u"\U0001f600" #emoji
# print(unicode)

#True = 1 , False = 0 , Special literal a = None
# a = True + 4 # out = 5
# b = False + 4 #out = 4

#operator 
# x,y = 5, 2
# print(x ** y) # x to the power y4
# print(x // y) # interger division 5/2=2.5 into int(2) 


# a= [11,1,1] 
# b = [11,1,1]
# print(a is b) / is not/ #both are identical but still it will return false as they are not in same memory location
# x = "DELHI"
# print("DEL" in x) / in / not in /#checks if DEL is in x


#intendation
# name = str(input())
# if name == 'sas' :
#     print("goood")
#     if name == "sass":
#         print("saasa")

# else:
#     print("not good")

#loops
# number = int(input("Enter a number"))
# i = 1
# while i < number:
#     print(number*i) 
#     i +=1
   
#Guessing game
# import random as rd

# a = rd.randint(1,99)
# ans = int(input())
# count = 1
# while a != ans:
   
#     if ans > a :
#         print("stay low")
      
#     elif ans < a :
#         print("stay high")
#     cont += 1
#     ans = int(input())  
# print("You found correct answer in " ,count , "attempts" )
        

#range function
# print(list(range(1,11))  ) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(13))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list(range(1,10,2))) #[1, 3, 5, 7, 9]


# data = ["AA0","BB!","CC"]
# for i in range(1,10):
#     print(i, end = " ")
#     for j in data:
#         if j == i :
#          print(j) 
        
# for i in range(5,1,-1):
#     for j in range(0,i):
#         print(" " , end = " ")
#     for k in range(i,6):
#          print("*" ,end = " ")
#     print(" ")

# matrix = [[1,2,3],[3,4,5],[6,7,8]]
# print(matrix.__sizeof__())


# for i in range(0,10):
#     if i==9:
#         break
#     elif i == 2:
#      continue
#     else:
#        pass #pass is just used when our logic is not sure it does not do anything #for i in range(1,10): pass
#     print(i)/


# #to find length of string 
# a = len("asda")
# b = 112
# min(b,11)
# print(a)

# import random as rd
# a = [1,2,34,1,1,2]
# b = "hghy"
# rd.shuffle(a)
# rd.randint(0,100)
# print(a)

# import time
# a = time.localtime()
# print(a.tm_hour,a.tm_min,a.tm_sec, sep =':')
# time.sleep(5.0) # waits 5 sec then execute lines below it
# b = time.ctime()
# print(b)
# c = time.time
