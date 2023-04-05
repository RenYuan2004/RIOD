#密码验证
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
#密码验证阶段结束，进入程序支选择
#测试代码块
actionSelect=""
while actionSelect !="0":
    print("=================Main  Menu=================")
    print("1.View all Operations(Under Contrast)")
    print("2.Add New Operations(Under Contrast)")
    print("3.Change Password")
    print("0.Exit R.I.O.D.")
    print("============================================")
    actionSelect=input("What do you want to?Entry a number:")
#1.建设中
    if actionSelect=="1":
        print("Under Contrast")
#2.建设中
    elif actionSelect=="2":
        print("Under Contrast")
#3.更改密码
    elif actionSelect=="3":
        pswn=input("Entry New Password:")
        pswf=open("psw.txt","w")
        pswf.write(pswn)
        pswf.close()
        print("Password have been changed.")
    else:
        print("Error.Please try again.")
#0.退出程序
exit(0)
