import streamlit as st

st.title("🎮 Rock Paper Scissors")
st.write("Choose your move!")


col1, col2, col3 = st.columns(3)
player_choice = None

# three buttons side by side
with col1:
    if  st.button("🪨 Rock"):
        player_choice = "Rock"
with col2:
    if st.button("📄 Paper"):
        player_choice = "Paper"
with col3:
    if st.button("✂️ Scissors"):
        player_choice = "Scissors"