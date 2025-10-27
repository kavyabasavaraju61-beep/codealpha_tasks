import streamlit as st
import random
import datetime

st.set_page_config(page_title="Interactive Chatbot", page_icon="🤖", layout="centered")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "input" not in st.session_state:
    st.session_state.input = ""

# CSS
st.markdown("""
<style>
body {background-color: #f4f6f8;}
.chat-container {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 15px;
    max-height: 450px;
    overflow-y: auto;
    border: 1px solid #ddd;
}
.user-bubble {
    background-color: #DCF8C6;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: right;
}
.bot-bubble {
    background-color: #E4E6EB;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    how_are_you = ["how are you", "how are you doing"]
    bye = ["bye", "goodbye", "see you", "exit"]
    sad = ["sad", "unhappy", "depressed", "upset"]
    bored = ["bored", "nothing to do", "tired"]

    if user_input in greetings:
        return random.choice([
            "Hi there! 😊 How are you doing?",
            "Hey! 👋 Nice to see you!",
            "Hello! Ready to chat?"
        ])

    elif user_input in how_are_you:
        return random.choice([
            "I'm doing great! Thanks for asking. What about you?",
            "I’m awesome, as always 😄 How are you feeling today?",
            "Feeling chatty! What’s new with you?"
        ])

    elif user_input in bye:
        return random.choice([
            "Goodbye! Take care 👋",
            "Bye-bye! Hope to chat again soon 😊",
            "See you later! Have a great day 🌟"
        ])

    elif any(word in user_input for word in sad):
        return random.choice([
            "Oh no 😢 I’m here for you. Want to talk about it?",
            "I’m sorry you feel that way. Maybe listening to music could help?",
            "Cheer up! 🌈 Better days are coming 💪"
        ])

    elif any(word in user_input for word in bored):
        return random.choice([
            "Bored? Hmm… how about trying a new hobby or watching a fun movie? 🎬",
            "Let's play a quick riddle! What has to be broken before you can use it? (Hint: It’s in your kitchen!) 🥚",
            "Maybe I can tell you a joke! Want to hear one? 😄"
        ])

    elif "your name" in user_input:
        return "I'm Chatty 🤖, your friendly Streamlit chatbot!"

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"

    elif "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today} 📅"

    elif "joke" in user_input:
        return random.choice([
            "Why don’t robots have brothers? Because they all share the same motherboard! 🤖😂",
            "What do you call a fake noodle? An *impasta*! 🍝",
            "Why did the computer show up late to work? It had a hard drive! 💻",
            "What’s a data scientist’s favorite kind of music? Algo-rhythm! 🎶",
            "Why was the computer cold? Because it left its Windows open!",
            "What’s a computer’s favorite snack? Microchips;)"

        ])

    elif "thank" in user_input:
        return random.choice([
            "You’re welcome! 😊",
            "No problem at all! 😄",
            "Always happy to help! 💫"
        ])

    else:
        return random.choice([
            "Hmm, that’s interesting! Tell me more.",
            "I’m not sure I understand, but I’d love to learn!",
            "Could you explain that a bit more?"
        ])

# Title
st.title("🤖 Interactive Chatbot")
st.write("Chat with the bot! (Try: hello, time, date, joke, bye etc.)")

user_input = st.text_input("You:", key="input")

# Process input
if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f'<div class="user-bubble"><b>You:</b> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble"><b>Bot:</b> {message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
