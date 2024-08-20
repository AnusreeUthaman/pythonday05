# break

i=1
while i<=10:
    print(i)
    if i == 5:
        break #control statement(exit)
    i+=1
print("end")
#iteration-loop cycle

#continue

i=0
while i<=10:
    i+=1
    if i == 5:
        continue #control statement
    print(i)
print("end")    

#while True

while True:
    password=input("Enter your password")
    if password == "codeme12##":
        break
    else:
        print("invalid password")
print("End")

count=1
while True:
    if count<=3:
        password=input("Enter your password")
        if password == "codeme12##":
            print("succcessfully Logged in")
            break
        else:
            print("invalid password")
            count+=1
    else:
        print("oops limit reached")
        break
print("End")


i=1
num=int(input("Enter your number: "))
while i<=10:
    print(f" {i} X {num} = {i*num}")
    i+=1
print("End")


#even numbers
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
print("End")


num=1
while num<=5:
    i=1
    while i<=10:
      n=i*num
      print(f"{i} * {num}={n}")
      if(num==i):
         break
      i+=1
    num+=1
   
        
