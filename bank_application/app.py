# pyright: ignore[reportMissingImports]
import random
import streamlit as st

st.title("Simple Banking App 👥")
st.write("This is a simple banking app using Streamlit")

# Store accounts
if "accounts" not in st.session_state:
    st.session_state.accounts = []

# ---------------- FUNCTIONS ---------------- #

def open_account(name, cnic, initial_deposit):
    if len(cnic) >= 12 and initial_deposit > 0:
        account = {
            "name": name,
            "cnic": cnic,
            "balance": initial_deposit,
            "pin": random.randint(1001, 9999),
            "account_number": random.randint(10000, 99999)
        }
        st.session_state.accounts.append(account)
        return account
    return None


def find_account(account_number):
    for acc in st.session_state.accounts:
        if acc["account_number"] == account_number:
            return acc
    return None


# ---------------- MENU ---------------- #

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw"]
)

# ---------------- OPEN ACCOUNT ---------------- #

if menu == "Open Account":
    st.subheader("Open New Account")

    name = st.text_input("Account Holder Name")
    cnic = st.text_input("CNIC")
    deposit = st.number_input("Initial Deposit", min_value=0, step=500)

    if st.button("Create Account"):
        account = open_account(name, cnic, deposit)
        if account:
            st.success("Account created successfully!")
            st.write("Account Number:", account["account_number"])
            st.write("PIN:", account["pin"])
        else:
            st.error("Invalid CNIC or deposit amount")

# ---------------- CHECK BALANCE ---------------- #

elif menu == "Check Balance":
    st.subheader("Check Balance")

    acc_no = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)

    if st.button("Check"):
        account = find_account(acc_no)
        if account and account["pin"] == pin:
            st.success(f"Balance: {account['balance']}")
        else:
            st.error("Invalid account number or PIN")

# ---------------- DEPOSIT ---------------- #

elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc_no = st.number_input("Account Number", step=1)
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        account = find_account(acc_no)
        if account:
            account["balance"] += amount
            st.success(f"New Balance: {account['balance']}")
        else:
            st.error("Account not found")

# ---------------- WITHDRAW ---------------- #

elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc_no = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        account = find_account(acc_no)
        if account and account["pin"] == pin:
            if account["balance"] >= amount:
                account["balance"] -= amount
                st.success(f"Withdrawal successful. Balance: {account['balance']}")
            else:
                st.error("Insufficient balance")
        else:
            st.error("Invalid account or PIN")
