import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")
st.write("Choose your move!")

choices = ["Rock", "Paper", "Scissors"]
wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

# session_state keeps score between button clicks
# took me a bit to figure this out - normal variables reset every click
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

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
        st.session_state.player_score += 1
    else:
        result = "💻 Computer Wins!"
        st.session_state.computer_score += 1

    st.subheader(result)
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer choice: {computer_choice}")

st.markdown("---")
st.metric("Your Score", st.session_state.player_score)
st.metric("Computer Score", st.session_state.computer_score)

