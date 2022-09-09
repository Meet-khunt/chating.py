#type of input

a="hallo"
b="meet"
 
print(a,b)

print("---------------------\n")

print(type(1))
print(type(1.1))
print(type(()))
print(type({}))
print(type("hi"))

print("---------------------\n")

#input , if...else

name= input("what is your name ?")

if name== "milan": #true
    
    print(a+" "+name + " you are not abel  to see")
    exit()
else: #false
  
 print(a+" "+name + " you are abel to see")
 
 


print("---------------------\n")

#maths

print(20+50*10)


print("---------------------\n")

#creat object


class BigCar:
    pass

Obj1=BigCar

print(type(Obj1))

print("---------------------\n")

print(type(str(1)))  #int in to str

print("---------------------\n")

#mod.string


print('''
     MMM
    |o o|
      -
     vvv
''') 

print("---------------------\n")

weather="it\'s kaind\'of cold "  # \t for tabs

print(weather)

print("---------------------\n")

#formatted string

age=input("what is your age ?\n  ")

print(f"hallo!! {name}. you are {age} year old")


print("---------------------\n")

#list

list="dog pen kali leptop python"
    # 0123456789......

print(list[0:11]) #start froe 012345....


print("---------------------\n")


list2="dog pen kali leptop python"
    # 0123456789......

print(list2[::1]) #revears the strings



# [start:stop:jump]



print("---------------------\n")

#bool


year =input("what is your born year ? \n")

age2=2022-int(year)

print(age2)

print("---------------------\n")

#password checker

passwd=input("what is your password ? \n")

passwd_len=len(passwd)

hidden="*" * int(passwd_len)



print(f"{name} your password is {hidden} {passwd_len} lettr long ")

print("---------------------\n")


#list methodes


basket=['a','b','c','d',"x","m"]

print("a \n" in basket  )

print (basket.count ("a"))

basket.sort()

print(basket)

basket.reverse()

print(basket)

print(list(range (1,101)))

basket2=" $ "

join_list=basket2.join([ 'hy','my','name','is','meet.' ])

print(join_list)


print(list(range(100)))


print("---------------------\n")

