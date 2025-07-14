from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def summarize_text(text):
    prompt = f"Summarize the following text:\n\n{text}"
    return call_gpt(prompt)


def answer_question(text, question):
    prompt = f"Given the following content:\n\n{text}\n\nAnswer this question: {question}"
    answer = call_gpt(prompt)
    
    justification_prompt = (
        f"Based on the above content, explain why the following is the correct answer:\n\n"
        f"Question: {question}\nAnswer: {answer}"
    )
    justification = call_gpt(justification_prompt)
    return answer, justification


def generate_questions(text):
    prompt = (
        f"Read the following text and generate 3 thought-provoking questions "
        f"that test understanding:\n\n{text}\n\n"
        f"List them on separate lines."
    )
    questions = call_gpt(prompt)
    return questions.strip().split("\n")[:3]
