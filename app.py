import streamlit as st

# Page config
st.set_page_config(page_title="Smart Bank", page_icon="🏦", layout="wide")

# Custom CSS
st.markdown("""
<style>

.main {
background: linear-gradient(to right,#1e3c72,#2a5298);
color:white;
}

.title{
font-size:40px;
font-weight:bold;
text-align:center;
padding:10px;
}

.card{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0px 4px 15px rgba(0,0,0,0.2);
color:black;
}

button[kind="primary"]{
background-color:#2a5298;
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)


# Bank Class
class BankApplication:

    def __init__(self, name, acc, mobile, balance):
        self.name = name
        self.acc = acc
        self.mobile = mobile
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return "Deposit Successful"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return "Withdraw Successful"
        else:
            return "Insufficient Balance"


# Title
st.markdown('<p class="title">🏦 Smart Banking Dashboard</p>', unsafe_allow_html=True)


# Sidebar
menu = st.sidebar.selectbox(
    "Navigation",
    ["Create Account","Deposit","Withdraw","Check Balance","Update Mobile"]
)


# Create Account
if menu == "Create Account":

    st.markdown("### 🧾 Create Your Account")

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        acc = st.text_input("Account Number")

    with col2:
        mobile = st.text_input("Mobile Number")
        balance = st.number_input("Initial Balance",min_value=0)

    if st.button("Create Account"):

        st.session_state.account = BankApplication(name,acc,mobile,balance)

        st.success("✅ Account Created Successfully")


# Deposit
elif menu == "Deposit":

    st.markdown("### 💰 Deposit Money")

    amount = st.number_input("Enter Amount",min_value=1)

    if st.button("Deposit"):

        result = st.session_state.account.deposit(amount)

        st.success(result)


# Withdraw
elif menu == "Withdraw":

    st.markdown("### 💸 Withdraw Money")

    amount = st.number_input("Enter Amount",min_value=1)

    if st.button("Withdraw"):

        result = st.session_state.account.withdraw(amount)

        st.success(result)


# Balance
elif menu == "Check Balance":

    st.markdown("### 📊 Account Balance")

    st.metric("Current Balance", f"₹ {st.session_state.account.balance}")


# Update Mobile
elif menu == "Update Mobile":

    st.markdown("### 📱 Update Mobile Number")

    new_mobile = st.text_input("Enter New Number")

    if st.button("Update"):

        st.session_state.account.mobile = new_mobile

        st.success("Mobile Updated Successfully")