import json

print("======Rhodes Island Operation Database======")
pswr=""
try:
    pswf="psw.json"
    with open(pswf,"r") as f_obj:
        pswr=json.load(f_obj)
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
except FileNotFoundError:
    print("Welcome,Blaze. Set your password at first.")
    pswr=input("New Password:")
    pswf="psw.json"
    with open(pswf,"w") as f_obj:
        json.dump(pswr,f_obj)
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
#3.更改密码(已完成)
    elif actionSelect=="3":
        pswn=input("Entry New Password:")
        with open(pswf,"w")as f_obj:
            json.dump(pswn,f_obj)
        print("Password have been changed successfully.")
    else:
        print("Error.Please try again.")
#0.退出程序(已完成)
exit(0)
