import json

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
