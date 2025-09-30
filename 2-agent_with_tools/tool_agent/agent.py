import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

def show_current_time() -> dict:
    """
    Returns the current time as a readable string.
    
    Returns:
        The current date and time
    """
    return {"current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Agent that gives the can use various tools",
    instruction="""
    You are a simple and polite AI Agent who can use the following tools:
    - show_current_time
    """,
    tools=[show_current_time],
    # tools=[google_search]
    # Unfortunatelly, at the moment, ADK cannot mix built-in tools with custom tools
)
