from fastapi import FastAPI, HTTPException
from .scraper import scrape_and_clean_text
from .analyzer import analyze_text_with_ai, AnalysisRequest, AnalysisResponse

app = FastAPI(
    title="ClauseEater API",
    description="API for analyzing Terms of Service and Privacy Policies.",
    version="0.1.0",
)

@app.get("/health", summary="Health Check", tags=["Health"])
def health_check():
    """
    Endpoint to check if the API is running.
    """
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalysisResponse, summary="Analyze Text or URL", tags=["Analysis"])
def analyze(request: AnalysisRequest):
    """
    Analyzes text from a URL or direct text input to identify problematic clauses.

    - **url**: The URL of the terms of service page.
    - **text**: The text of the terms of service.

    Either `url` or `text` must be provided.
    """
    if request.url:
        cleaned_text = scrape_and_clean_text(request.url)
        if not cleaned_text:
            raise HTTPException(status_code=400, detail="Could not fetch or clean text from the URL.")
    elif request.text:
        cleaned_text = request.text
    else:
        raise HTTPException(status_code=400, detail="Either 'url' or 'text' must be provided.")

    analysis_result = analyze_text_with_ai(request.url, cleaned_text)

    return analysis_result
