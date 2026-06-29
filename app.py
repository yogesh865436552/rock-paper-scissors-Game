import streamlit as st
import random

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Rock Paper Scissors")
st.write("Choose your move!")

choices = ["Rock", "Paper", "Scissors"]

#cleaner than writing out every combination in if elif
wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

# session_state keeps score between clicks - resets on full page refresh
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

col1, col2, col3 = st.columns(3)
player_choice = None

with col1:
    if st.button("🪨 Rock", use_container_width=True):
        player_choice = "Rock"
with col2:
    if st.button("📄 Paper", use_container_width=True):
        player_choice = "Paper"
with col3:
    if st.button("✂️ Scissors", use_container_width=True):
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

# two columns for scores look cleaner than stacking them
score_col1, score_col2 = st.columns(2)
with score_col1:
    st.metric("Your Score", st.session_state.player_score)
with score_col2:
    st.metric("Computer Score", st.session_state.computer_score)

if st.button("🔄 Reset Scores"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.rerun()

st.markdown("---")
st.write("Made with by Yogesh Madhukumar 🚀")