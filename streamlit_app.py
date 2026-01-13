import streamlit as st

# Title of the application
st.title("Ma première application Streamlit 🎉")

# Header
st.header("Bienvenue!")

# Subheader
st.subheader("Ceci est une sous-section")

# Text
st.write("Voici ma première application Streamlit. C'est simple et puissant!")

# Input from user
name = st.text_input("Entrez votre nom:")

if name:
    st.write(f"Bonjour, {name}! Ravi de vous rencontrer! 👋")

# Button
if st.button("Cliquez-moi"):
    st.balloons()
    st.success("Bravo! Vous avez cliqué sur le bouton!")

# Slider
age = st.slider("Sélectionnez votre âge:", 0, 100, 25)
st.write(f"Vous avez {age} ans.")