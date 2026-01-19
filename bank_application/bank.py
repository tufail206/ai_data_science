import streamlit as st
import random
accounts=[]
st.title("Simple banking  App")
st.write("enjoy you day by serving")
def openAcount(holdername:str,cnic:str,initialDeposite:int):
     if len(cnic)<0 or len(cnic)>18:
        return "invalid cnic"
     else:
        account={"holdername":holdername,"cnic":cnic,"balance":initialDeposite,"pin":random.randint(999,10000),"acount_number":random.randint(999,10000)}
        accounts.append(account)
        return f"{holdername} your account is created successfully"


menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw"]
)

if menu=="Open Account":
    st.header("open your account")
    openAcount("tufail","1234123412341234",1000)
    st.success("you have created account")
if menu=="Check Balance":
    print("helo")


