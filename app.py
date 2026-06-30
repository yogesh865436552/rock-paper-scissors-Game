import streamlit as st
import random
import pandas as pd

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

#keeps track  of every round played
if "match_history" not in st.session_state:
    st.session_state.match_history = []

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

    # save  each round to history
    st.session_state.match_history.append({
        "You": player_choice,
        "Computer": computer_choice,
        "Result": result
    })

    
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer choice: {computer_choice}")

st.markdown("---")   


score_col1, score_col2 = st.columns(2)
with score_col1:
    st.metric("Your Score", st.session_state.player_score)
with score_col2:
    st.metric("Computer Score", st.session_state.computer_score)

total = st.session_state.player_score + st.session_state.computer_score
if total > 0:
    win_pct = round((st.session_state.player_score / total) * 100)
    st.markdown(f"**Your win rate: {win_pct}%**")

if st.button("🔄 Reset Scores"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.rerun()

if st.session_state.match_history:
    st.markdown("### Last 5 Rounds")
    history_df = pd.DataFrame(st.session_state.match_history[-5:])
    st.dataframe(history_df, use_container_width=True)

st.markdown("---")
st.write("Made with by Yogesh Madhukumar 🚀")