import ukcovidstats
import ukgdp
import pakistancovid
import streamlit as st
from PIL import Image

def main():

    menu_login()

def menu_login():

    # Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid/3000.png')
    st.image(image, caption='', use_column_width=True)

    st.markdown("<h1 style='text-align: center; color: black;'>COVID 19: Ramifications on the climate and environment and how these have impacted the economy in various countries</h1>", unsafe_allow_html=True)

    menu = ["Home", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login: ")
        username = st.sidebar.text_input("Username: ")
        password = st.sidebar.text_input("Password: ", type='password')

        if st.sidebar.checkbox("Login"):
            if password == "admin":
                st.success(f"Logged in as {username}")

                task = st.selectbox("Options", ["UK Covid statistics", "UK GDP", "Pakistan Covid Profile"])
                if task == "UK Covid statistics":
                    ukcovidstats.main()
                if task == "UK GDP":
                    ukgdp.main()
                if task == "Pakistan Covid Profile":
                    pakistancovid.main()
            else:
                st.warning("Incorrect Username or Password")



if __name__ == '__main__':
    main()