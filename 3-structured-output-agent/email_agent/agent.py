from google.adk.agents import Agent

root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Agent that writes emails",
    instruction="""
    You are a helpfull assistant that writes emails.
    All the emails that you write, will contain a subject and an email_body.
    I need you to write all the emails in JSON format like in the example from below:
    {
     "subject": "This is where you add the text for the subject of the email - keep it short and to the point",
     "email_body": "this is the place where you will add the text of the email. Keep a professional tone"
    }
    """,
)