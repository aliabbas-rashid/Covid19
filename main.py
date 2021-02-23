import ukcovidstats
import ukgdp
import pakistancovid
import engmeantemp
import ukgvaavg
import checkpw
import streamlit as st
from PIL import Image
from base64 import b64encode

def main():

    menu_login()

def menu_login():

    # Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid19/pictures/3000.png')
    st.image(image, caption='', use_column_width=True)

    st.markdown("<h1 style='text-align: center; color: black;'>COVID 19: Ramifications on the climate and environment and how these have impacted the economy in various countries</h1>", unsafe_allow_html=True)

    menu = ["Home", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to my final year project web application! Please select login from the left hand side (menu) and enter a valid login. Tick the login box once you're ready.")
    elif choice == "Login":
        st.subheader("Login")
        st.write("Welcome to my final year project web application! Please select login from the left hand side (menu) and enter a valid login. Tick the login box once you're ready.")
        username = st.sidebar.text_input("Username: ")
        password = st.sidebar.text_input("Password: ", type='password')

        if st.sidebar.checkbox("Login"):
            if username == "admin" and checkpw.checkpass(password):
                st.success(f"Logged in as {username}")

                task = st.selectbox("Options", ["UK Covid statistics", "UK GDP", "UK Gross Value Added", "England Mean Temp", "Pakistan Covid Profile"])
                if task == "UK Covid statistics":
                    ukcovidstats.main()
                if task == "UK GDP":
                    ukgdp.main()
                if task == "UK Gross Value Added":
                    ukgvaavg.main()
                if task == "England Mean Temp":
                    engmeantemp.main()
                if task == "Pakistan Covid Profile":
                    pakistancovid.main()
            else:
                st.warning("Incorrect Username or Password")



if __name__ == '__main__':
    main()