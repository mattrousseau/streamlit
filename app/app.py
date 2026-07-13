import streamlit as st

st.write('Welcome to my app')

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write("SECRETS")

st.write("spell")
st.write(spell)

st.write("key")
st.write(key)
