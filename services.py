# services.py

import qa_logic as ql
from document_loader import load_text

def summarize_document(raw_bytes, file_type='pdf'):
    text = load_text(raw_bytes, file_type)
    return ql.summarize_text(text)

def ask_question(raw_bytes, question, file_type='pdf'):
    text = load_text(raw_bytes, file_type)
    return ql.answer_question(text, question)

def generate_questions(raw_bytes, file_type='pdf'):
    text = load_text(raw_bytes, file_type)
    return ql.generate_questions(text)

def evaluate_answers(raw_bytes, questions, user_answers, file_type='pdf'):
    text = load_text(raw_bytes, file_type)
    return ql.evaluate_responses(text, questions, user_answers)
