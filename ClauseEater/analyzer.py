from pydantic import BaseModel
from typing import List, Optional

# Pydantic models for data validation and schema generation

class AnalysisRequest(BaseModel):
    """
    Request model for the /analyze endpoint.
    Accepts either a URL or a direct text input.
    """
    url: Optional[str] = None
    text: Optional[str] = None

class Flag(BaseModel):
    """
    Represents a problematic clause or "flag" found in the text.
    """
    type: str
    risk: str  # "Low", "Medium", "High"
    description: str

class AnalysisResponse(BaseModel):
    """
    Response model for the /analyze endpoint.
    Provides a structured analysis of the terms of service.
    """
    url: Optional[str]
    risk_score: int
    summary: str
    flags: List[Flag]

def analyze_text_with_ai(url: str, text: str) -> AnalysisResponse:
    """
    Simulates sending text to an AI model for analysis.

    In a real application, this function would contain the logic to call
    an external AI API (e.g., OpenAI, PaLM, Gemini). For this MVP, it
    returns a hardcoded mock response.

    Args:
        url: The URL of the content being analyzed.
        text: The cleaned text to be analyzed.

    Returns:
        An AnalysisResponse object with the analysis results.
    """
    # Mock analysis - replace with actual AI call
    print(f"Analyzing text from: {url}")
    print(f"Text length: {len(text)} characters")

    return AnalysisResponse(
        url=url,
        risk_score=72,
        summary="The site collects data of location and shares it with third parties.",
        flags=[
            Flag(
                type="Data Sharing",
                risk="High",
                description="Allows data sharing without explicit consent."
            ),
            Flag(
                type="Responsibility Disclaimer",
                risk="Medium",
                description="The site is not responsible for data loss."
            ),
        ]
    )
