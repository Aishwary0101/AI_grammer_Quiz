from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Your DTO (Request/Response)
class QuizSubmission(BaseModel):
    question_id: int
    selected_option: str

# 1. Fetch Daily Lesson
@app.get("/api/grammar/daily")
def get_daily_lesson():
    # Fetch from database (e.g., using SQLAlchemy)
    return {"title": "Tenses", "content": "Keep practicing daily!"}

# 2. Submit Quiz
@app.post("/api/quiz/submit")
def submit_quiz(answers: List[QuizSubmission]):
    # Logic: Calculate score
    score = 0
    # Add your logic to compare answers against the database here
    return {"score": score, "message": "Quiz submitted successfully"}