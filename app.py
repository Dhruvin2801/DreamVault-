import streamlit as st
from transcribe import transcribe_audio
from cluster import cluster_ideas

st.set_page_config(page_title="DreamVault MVP", page_icon="🌙")
st.title("🌙 DreamVault")
st.write("Capture your fleeting thoughts, dreams, and creative sparks.")

# Store collected ideas
if "ideas" not in st.session_state:
    st.session_state.ideas = []

uploaded_file = st.file_uploader("Upload a short voice note", type=["mp3","wav","m4a"])
if uploaded_file is not None:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    text = transcribe_audio("temp.wav")
    st.success("Transcribed: " + text)
    st.session_state.ideas.append(text)

typed = st.text_input("Or type an idea here")
if typed:
    st.session_state.ideas.append(typed)

if st.button("Show My Idea Map") and st.session_state.ideas:
    fig = cluster_ideas(st.session_state.ideas)
    st.plotly_chart(fig, use_container_width=True)

if st.button("Clear All Ideas"):
    st.session_state.ideas = []
