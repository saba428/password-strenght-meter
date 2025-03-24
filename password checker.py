import streamlit as st 
import re 

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker! 👋
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you helpful tips to create a *strong Password* 🔒
""")

st.markdown('<h1 style="color:green">SABA NAZ AI Student</h1>', unsafe_allow_html=True)

password = st.text_input("Enter your password", type="password")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    common_passwords = ["password", "123456", "12345678", "qwerty", "abc123", "password1"]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.") 

    if len(password) >= 12:
        score += 1  # Extra point for long passwords

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include both uppercase (A-Z) and lowercase (a-z) letters.")
     
    if re.search(r"[0-9]", password):  
        score += 1
    else:
        feedback.append("❌ Password should include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*()_+=\-[\]{}|:;\"'<>,.?/~]", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one special character (!@#$%^&*).")

    if " " in password:
        feedback.append("❌ Password should not contain spaces.")

    if password.lower() in common_passwords:
        feedback.append("❌ Your password is too common. Choose a more unique password.")

    return score, feedback

# Button to check password strength
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score >= 5:
            st.success("✅ Very Strong Password - Your password is highly secure.")
        elif score == 4:
            st.success("✅ Strong Password - Your password is secure.")
        elif score == 3:
            st.info("⚠ Moderate Password - Consider improving security by adding more features.")
        else:
            st.error("❌ Weak Password - Follow the suggestions below to strengthen it.")

        if feedback:
            with st.expander("🔎 Improve Your Password:"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠ Please enter a password first.")
