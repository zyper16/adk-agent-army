from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

#Define output schema
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )


#Email writting agent
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Agent that writes emails",
    instruction="""
    You are a helpfull assistant that writes emails.
    All the emails that you write, will contain a subject and an email_body.
    I need you to write all the emails in JSON format like in the example from below:
    {
     "subject": "This is where you add the text for the subject of the email - keep it short and to the point",
     "body": "this is the place where you will add the text of the email. Keep a professional tone"
    }
    """,
    output_schema=EmailContent,
)