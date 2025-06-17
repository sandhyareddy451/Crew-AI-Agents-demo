import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

search_tool = SerperDevTool()
llm = ChatOpenAI(model = "gpt-3.5-turbo")

def create_research_agent():
    return Agent (
         role = "Research Specialist",
         goal = "conduct through research on given topic",
         backstor= "you are an experienced researcher in finding and synthesizing information from the various sources",
         verbose = True,
         allow_deligation = False,
         tools = [search_tool],
         llm=llm
         
    )
    
def create_research_task(agent, topic):
    return Task(
        description = f"Research the following topic and provide a comprehensive summery:{topic}",
        agent = agent,
        expected_output= "A detailed summary of the research findings including key points and insights"
        
        
        
    )

def run_research(topic):
    agent= create_research_agent(),
    task = create_research_task(agent, topic)
    crew = Crew(agent=[agent], task=[task])
    results = crew.kickoff()
    return results


if __name__ =='__main__':
    print("welcome to the research agents")
    topic = input("rnter the research topid")
    result = run_research(topic)
    print("Run results: ")
    
    