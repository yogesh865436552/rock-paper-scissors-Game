import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")
st.write("Choose your move!")

choices = ["Rock", "Paper", "Scissors"]

# dictionary is cleaner than a big if elif block - learned this the hard way
wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

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

if player_choice:
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "🤝 Tie!"
    elif wins[player_choice] == computer_choice:
        result = "🎉 You Win!"
    else:
        result = "💻 Computer Wins!"

    st.subheader(result)
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer choice: {computer_choice}")