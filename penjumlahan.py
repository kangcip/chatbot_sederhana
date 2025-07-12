import streamlit as st
import random

st.title("Game Penjumlahan Sederhana")

if "score" not in st.session_state:
    st.session_state.score = 0
if "question" not in st.session_state:
    a, b = random.randint(1, 20), random.randint(1, 20)
    st.session_state.question = (a, b)

a, b = st.session_state.question
st.write(f"Berapakah hasil dari {a} + {b}?")

answer = st.text_input("Jawaban Anda:", key="answer")

if st.button("Cek Jawaban"):
    if answer.isdigit() and int(answer) == a + b:
        st.success("Benar!")
        st.session_state.score += 1
        a, b = random.randint(1, 20), random.randint(1, 20)
        st.session_state.question = (a, b)
        st.session_state.answer = ""
    else:
        st.error("Salah, coba lagi!")

st.write(f"Skor Anda: {st.session_state.score}")