from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from llm_config import llm  # Import the LLM setup
import os
from config_loader import get_serper_api_key

@CrewBase
class SportsCrew:
    """Crew to gather and summarize sports news"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def sports_researcher(self) -> Agent:
        search_tool = SerperDevTool(api_key=get_serper_api_key())  # Google Search Tool
        return Agent(
            config=self.agents_config["sports_researcher"],
            tools=[search_tool],  # Enables web search
            llm=llm,  # Attach Gemini 2.0 Flash LLM
            verbose=True,
        )

    @agent
    def sports_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["sports_writer"],
            llm=llm,  # Attach Gemini 2.0 Flash LLM
            verbose=True,
        )

    @task
    def research_sports_news(self) -> Task:
        return Task(
            config=self.tasks_config["research_sports_news"],
            agent=self.sports_researcher()
        )

    @task
    def write_sports_summary(self) -> Task:
        return Task(
            config=self.tasks_config["write_sports_summary"],
            agent=self.sports_writer()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Sports News Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Tasks run in order
            verbose=True,
        )

if __name__ == "__main__":
    sports_crew = SportsCrew().crew()
    results = sports_crew.kickoff()