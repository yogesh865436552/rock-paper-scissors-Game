import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")
st.write("Choose your move!")

choices = ["Rock", "Paper", "Scissors"]

col1, col2, col3 = st.columns(3)
player_choice = None

with col1:
    if st.button("🪨 Rock"):
        player_choice = "Rock"
with col2:
    if st.button("📄 Paper"):
        player_choice = "Paper"
with col3:
    if st.button("✂️ Scissors"):
        player_choice = "Scissors"

# computer picks randomly each round
if player_choice:
    computer_choice = random.choice(choices)
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer choice: {computer_choice}")