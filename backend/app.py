from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qa_model import answer_question

app = FastAPI()

# Enable CORS for communication with Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define expected JSON schema
class QARequest(BaseModel):
    question: str
    context: str

@app.post("/ask")
async def ask_question(payload: QARequest):
    answer = answer_question(payload.question, payload.context)
    return {"answer": answer}
