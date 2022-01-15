import requests  # this is to GET the javascript 
import re # this is to do regular expression and extract the list of words
import streamlit as st #web app development


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0000FF;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #FF0000;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)

# extract the wordle solution list from the source page javascript 

@st.cache
def extract_solution():

    wordle_js = requests.get("https://www.powerlanguage.co.uk/wordle/main.c1506a22.js")

    m = re.findall(r"var La=\[(.*?)\]", wordle_js.text, flags=re.S)

    word_list = m[0].split(",")

    return(word_list)

word_list = extract_solution()

st.title("👻 Wordle Spoiler 👿")

index = st.text_input(label = "Enter the Wordle Number for which you need solution")

st.error(" ⚠️ Do you really want to do this? I mean you can always play for fun!!!")

if st.button("Yes I just want to spoil the mood",):
    st.balloons()
    st.write(word_list[int(index)])