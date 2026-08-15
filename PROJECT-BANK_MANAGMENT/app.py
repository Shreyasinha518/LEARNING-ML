import streamlit as st
from hello import Bank

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(
    page_title="🏦 Simple Bank App",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Simple Bank Management System")
st.write("Manage your bank account securely and easily.")

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio(
    "📌 Select an Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Account Details",
        "Update Account",
        "Delete Account",
    ],
)

# ------------------ CREATE ACCOUNT ------------------
if menu == "Create Account":

    st.header("🆕 Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-Digit PIN", type="password")

    if st.button("Create Account", use_container_width=True):

        if not name or not email or not pin:
            st.warning("Please fill all fields.")

        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")

        else:
            user, msg = Bank.create_account(
                name,
                int(age),
                email,
                int(pin)
            )

            if user:
                st.success(msg)

                st.info(
                    f"🎉 Your Account Number is: **{user['accountNo.']}**"
                )

            else:
                st.error(msg)

# ------------------ DEPOSIT ------------------
elif menu == "Deposit Money":

    st.header("💰 Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Deposit Amount", min_value=1)

    if st.button("Deposit", use_container_width=True):

        if not acc or not pin:
            st.warning("Enter account number and PIN.")

        else:
            success, msg = Bank.deposit(
                acc,
                int(pin),
                int(amount)
            )

            if success:
                st.success(msg)
            else:
                st.error(msg)

# ------------------ WITHDRAW ------------------
elif menu == "Withdraw Money":

    st.header("💸 Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Withdrawal Amount", min_value=1)

    if st.button("Withdraw", use_container_width=True):

        if not acc or not pin:
            st.warning("Enter account number and PIN.")

        else:
            success, msg = Bank.withdraw(
                acc,
                int(pin),
                int(amount)
            )

            if success:
                st.success(msg)
            else:
                st.error(msg)

# ------------------ SHOW DETAILS ------------------
elif menu == "Show Account Details":

    st.header("📄 Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details", use_container_width=True):

        user = Bank.find_user(acc, int(pin))

        if user:

            st.success("Account Found")

            st.markdown("### 👤 Customer Information")

            st.write(f"**Name:** {user['name']}")
            st.write(f"**Age:** {user['age']}")
            st.write(f"**Email:** {user['email']}")
            st.write(f"**Account Number:** {user['accountNo.']}")
            st.write(f"**Balance:** ₹ {user['balance']}")

        else:
            st.error("Account not found.")

# ------------------ UPDATE ------------------
elif menu == "Update Account":

    st.header("✏️ Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    new_pin = st.text_input("New PIN")

    if st.button("Update Account", use_container_width=True):

        success, msg = Bank.update_user(
            acc,
            int(pin),
            name,
            email,
            new_pin
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)

# ------------------ DELETE ------------------
elif menu == "Delete Account":

    st.header("🗑 Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    st.warning("⚠ This action cannot be undone.")

    if st.button("Delete Account", use_container_width=True):

        success, msg = Bank.delete_user(acc, int(pin))

        if success:
            st.success(msg)
        else:
            st.error(msg)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("🏦 Bank Management System | Built using Python & Streamlit")