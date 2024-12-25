def add():
  result=0
  for i in range(0,len(num)):
    result+=num[i]
  print("Result of addition",result)

def subb():
  result=num[0]
  for i in range(1,len(num)):
    result-=num[i]
  print("Result of Subtraction",result)

def mult():
  result=num[0]
  for i in range(1,len(num)):
    result*=num[i]
  print("Result for mutiplication",result)

def div():
  result=num[0]
  for i in range(1,len(num)):
    if num[i]==0:
      print("division with zero is not possible")
      break
  
    result/=num[i]
    print("Result for division",result)

n=int(input("enter the no of terms to perform the calculation"))
num=[]
for i in range(0,n):
  a=int(input("enter the number"))
  num.append(a)
print("1-add,2-subtraction,3-multiplication,4-division")
choice=int(input("enter your choice"))
if choice==1:
  add()
elif choice==2:
  subb()
elif choice==3:
  mult()
elif choice==4:
  div()
else:
  print("1-add,2-subtraction,3-multiplication,4-division")
