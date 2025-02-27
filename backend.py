from fastapi import FastAPI
from crewai import Crew
from main import SportsCrew  # Import your Crew setup

app = FastAPI()

@app.get("/generate_sports_news")
async def generate_sports_news():
    """Trigger the CrewAI agents and return the sports news summary."""
    try:
        sports_crew = SportsCrew().crew()
        results = sports_crew.kickoff()
        output_text = str(results) if isinstance(results, str) else "\n".join(map(str, results))
        return {"sports_news": output_text}
    except Exception as e:
        return {"error": str(e)}
