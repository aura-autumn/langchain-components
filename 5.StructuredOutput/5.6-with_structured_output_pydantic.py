from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()

model=ChatOpenAI()

#Schema

class Review(BaseModel):
    key_themes: list[str]= Field(description="List of key themes discussed in the review.")
    summary: str= Field(description="A brief summary of the review.")
    sentiment: Literal["Pos", "Neg", "Neu"]= Field(description="Return sentiment of the review-negative, positive, or neutral.")
    pros: Optional[list[str]]=Field(default=None, description="Return the list of pros if any.")
    cons: Optional[list[str]]= Field(default=None, description="Return the list of cons if any.")
    name: Optional[str]=Field(default='Anonymous', description="Return the name of the reviewer.")


structured_model= model.with_structured_output(Review)

result=structured_model.invoke("5 stars. Absolutely fire!!!")

print(result)