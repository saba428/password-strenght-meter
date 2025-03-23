# project 2: password strength meter
import streamlit as st 
import re 

st.set_page_config(page_title="password Strenght cheaker",page_icon="🔒")

st.title("🔐 password Strenght cheaker")
st.markdown("""
## welcome to the unlimate password strenght cheaker!👋
use this simple tool to check the strenght of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a *strong Password* 🔒""")
st.markdown('<h1 style="color:green">SABA NAZ AI Student</h1>' , unsafe_allow_html=True)
password = st.text_input("enter your passord", type="password")

feedback =[]

score= 0

if password:   
    if len(password) >= 8:
        score += 1 
    else:
      feedback.append("❌ Password should be at least 8 character long.") 

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
         feedback.append("❌ Password should include both upper case (A-Z) and lower case (a-z) letters.")
     
    if re.search(r"0-9]", password):
            score += 1
    else:
         feedback.append("❌ Password should include at least one digit (0-9).")
        
     #special characters
    if re.search(r"[!@#$%^&*]", password):
         score =+ 1
    else:
         feedback.append("❌ Password include at least one special character (!@#$%^&*).")
         
         score, feedback
    
     #user input
    Password = st.text_input("Enter Your Password:", type="Password", help="Enter Password here to check Strength")

     #Button to check strength Password =
    if st.button("check strength"):
         
        if password:
         score, feedback = check_password_strength(password) # type: ignore
     
     #Display result
    if score == 4:
              st.success("✅ strong password - your Password is secure.")
    elif score == 3 :
         st.info("⚠ Moderate Password - consider improving security by adding more features")
    else:
         st.error("❌ Week Password - follow the suggestion below to strenghten it. ")

     #show feedback if any
    if feedback:
         with st.expander("🔎 Improve Your Password:"):
              for item in feedback:
                   st.write(item)
    else:
        st.warning("⚠ Please enter a Password first.")
if feedback:
     st.markdown("## Improvments sugggentions")
     for tip in feedback:
          st.write(tip)
else:
     st.info("please enter your password to get strated.")
