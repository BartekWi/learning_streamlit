import streamlit as st
conditions={'Password must be atleast 8 characters long':lambda pw:len(pw)>8,
            'Password must include 1 big letter':lambda pw:any(char.isupper() for char in pw)}
st.title("Password checker")
password=st.text_input("Enter your password",type="password")
if st.button("Check password"):
    if password:
        for cond,check in conditions.items():
            if(check(password)):
                st.success(f'{cond},Passed')
            else:
                st.error(f'{cond},Failed')
    else:
        st.write("Please enter your password")