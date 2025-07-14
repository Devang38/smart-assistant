from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import qa_logic as ql

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(request: Request):
    body = await request.json()
    text = body.get("text", "")
    return {"summary": ql.summarize_text(text)}

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    text = body.get("text", "")
    question = body.get("question", "")
    answer, justification = ql.answer_question(text, question)
    return {"answer": answer, "justification": justification}

@app.post("/challenge/generate")
async def gen(request: Request):
    body = await request.json()
    text = body.get("text", "")
    return {"questions": ql.generate_questions(text)}
