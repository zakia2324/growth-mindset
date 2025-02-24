
import streamlit as st
# Custom CSS for background color and other styles
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    .stApp {
        background-color: #f0f8ff;
    }
    .title {
        color: #ff6347;
        font-size: 3em;
        font-weight: bold;
    }
    .header {
        color: #4682b4;
        font-size: 2em;
        font-weight: bold;
    }
    .subheader {
        color: #8a2be2;
        font-size: 1.5em;
        font-weight: bold;
    }
    .write {
        color: #20b2aa;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Growth Mindset Challenge')
st.header('Welcome to the Growth Mindset Challenge')
st.write('This app is designed to help you cultivate a growth mindset.')

name = st.text_input('Enter your name:')
if st.button('Submit Name', key='submit_name'):
    st.write(f'Welcome, {name}! Let’s start the challenge.')

st.subheader('Challenges')
activities = [
    'Write about a challenge you faced today.',
    'Describe how you solved a problem.',
    'Share a new skill you learned this week.'
]

answers = []  # Jawabon ko save karne ke liye list

for i, activity in enumerate(activities):
    st.write(f'- {activity}')
    answer = st.text_input(f'Enter your answer for activity {i+1}:', key=f'answer_{i+1}')
    answers.append(answer)

if st.button('Submit All Answers', key='submit_all_answers'):
    for i, answer in enumerate(answers):
        st.write(f'Your answer for activity {i+1}: {answer}')
