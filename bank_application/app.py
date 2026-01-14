import random
all_account=[]
def open_account(name:str,cnic:str,initial_deposit:int):
    if len(cnic)>=1:
         all_account.append({'name':name,'cnic':cnic,'balance':initial_deposit,'pin':random.randint(1001,9999),'account_number':random.randint(10111,90111)})
         return f"{name} your account is created successfully"
    else:
         return "invalid cnic"
    
open_account("adnan","123123123123123",5000)