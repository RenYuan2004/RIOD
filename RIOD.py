import json

print("======Rhodes Island Operation Database======")
username=input("User:")
pswf="Userdata/"+username+".json"
try:
    with open(pswf,"r") as f_obj:
        pswr=json.load(f_obj)
    while pswr!=0:
        pswin=input("Password:")
        if pswin==pswr:
            print("Welcome back,"+username+".")
            break
        else:
            print("Wrong Username or Password.Try Again.")
            print("============================================")
except FileNotFoundError:
    print("Welcome,"+username+". Set your password at first.")
    pswr=input("New Password:")
    pswf="Userdata/"+username+".json"
    with open(pswf,"w") as f_obj:
        json.dump(pswr,f_obj)

#密码验证阶段结束，进入程序支选择
#测试代码块
actionSelect=""
while actionSelect !="0":
    print("=================Main  Menu=================")
    print("1.Add New Operations(Under Contrast)")
    print("2.View all Operations(Under Contrast)")
    print("3.Change Password")
    print("0.Exit R.I.O.D.")
    print("============================================")
    actionSelect=input("What do you want to?Entry a number:")
#1.建设中
    if actionSelect=="1":
        print("Under Contrast")
#2.读取（建设中）
    elif actionSelect=="2":
        print("===============Operation List===============")
        contentfile="Data/Content.txt"
        with open(contentfile)as file_object:
            content=file_object.readlines()
        contentlen=len(content)
        for i in range(0,contentlen):
            print(i,".",content[i])#列表可读，有空行
        print("============================================")
        viewfileno=input("Which Operation do you want to view?")
        viewfilenoint=int(viewfileno)
        viewfile=("Data/"+content[viewfilenoint]+".txt")
        print("============================================")
        with open(viewfile)as file_object:
            filedetials=file_object.read()
            print(filedetials.rstrip())
            print("============================================")
#3.更改密码(已完成)
    elif actionSelect=="3":
        pswn=input("Entry New Password:")
        with open(pswf,"w")as f_obj:
            json.dump(pswn,f_obj)
        print("Password have been changed successfully.")
#Sp.无效操作(已完成)
    else:
        print("Invaild operation.Please try again.")
#0.退出程序(已完成)
exit(0)
