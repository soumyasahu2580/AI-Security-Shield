from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI(title="AI Phishing Shield API")

class TextRequest(BaseModel):
    message: str

# Basic heuristic + keyword matching model mock for hackathon speed
PHISHING_KEYWORDS = ["urgent", "verify account", "bank alert", "click here", "win lottery", "password reset"]

@app.post("/detect/text")
async def detect_phishing(data: TextRequest):
    text = data.message.lower()
    score = 0
    detected_flags = []
    
    for word in PHISHING_KEYWORDS:
        if word in text:
            score += 20
            detected_flags.append(word)
            
    # URL check
    urls = re.findall(r'https?://[^\s]+', text)
    if urls:
        score += 30
        detected_flags.append("Suspicious URL detected")

    is_threat = score > 30
    risk_level = "High" if score > 50 else ("Medium" if score > 20 else "Safe")

    return {
        "status": "success",
        "is_threat": is_threat,
        "risk_level": risk_level,
        "confidence_score": min(score, 100),
        "flags": detected_flags
    }