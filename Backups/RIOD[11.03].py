pswf=open("psw.txt","r")
pswr=pswf.read()
pswf.close()
print("======Rhodes Island Operation Database======")
pswright=0
while pswright==0:
    print("User:Blaze")
    pswin=input("Password:")
    if pswin==pswr:
        print("Welcome back,Elite Operator Blaze.")
        break
    else:
        print("Wrong Username or Password.Try Again.")
        print("============================================")

