# app.py
import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="📘 Smart Document Assistant")
st.title("📘 Smart Document Assistant")

uploaded_file = st.file_uploader("Upload PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    files = {"doc_bytes": (uploaded_file.name, file_bytes)}

    st.subheader("📄 Document Summary")
    with st.spinner("Generating summary..."):
        res = requests.post(f"{API_BASE}/summarize", files=files)
        if res.status_code == 200:
            summary = res.json().get("summary", "No summary returned.")
            st.success(summary)
        else:
            st.error(f"Error {res.status_code}: {res.text}")

    st.subheader("💬 Ask Anything")
    user_q = st.text_input("Ask a question based on the document:")
    if st.button("Ask") and user_q:
        data = {"question": user_q}
        res = requests.post(f"{API_BASE}/ask", files=files, data=data)
        if res.status_code == 200:
            result = res.json()
            st.markdown(f"**Answer:** {result.get('answer', 'N/A')}")
            st.markdown(f"**Justification:** {result.get('justification', 'N/A')}")
        else:
            st.error(f"Error {res.status_code}: {res.text}")

    st.subheader("🎯 Challenge Me")
    if st.button("Generate 3 Questions"):
        res = requests.post(f"{API_BASE}/challenge/generate", files=files)
        if res.status_code == 200:
            questions = res.json().get("questions", [])
            answers = []
            for i, q in enumerate(questions):
                answers.append(st.text_input(f"Q{i+1}: {q}", key=f"q_{i}"))

            if st.button("Submit Answers"):
                json_payload = {
                    "questions": questions,
                    "answers": answers
                }
                res = requests.post(f"{API_BASE}/challenge/evaluate", files=files, json=json_payload)
                if res.status_code == 200:
                    feedback = res.json().get("feedback", [])
                    for i, (fb, just) in enumerate(feedback):
                        st.markdown(f"**Feedback for Q{i+1}:** {fb}")
                        st.markdown(f"**Justification:** {just}")
                else:
                    st.error(f"Evaluation Error {res.status_code}: {res.text}")
        else:
            st.error(f"Question Generation Error {res.status_code}: {res.text}")