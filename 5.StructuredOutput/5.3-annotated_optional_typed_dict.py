from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model=ChatOpenAI()

#Schema

class Review(TypedDict):
    key_themes: Annotated[list[str], "List of key themes discussed in the review."]
    summary: Annotated[str, "A brief summary of the review."]
    sentiment: Annotated[str, "Return sentiment of the review-negative, positive, or neutral."]


class detailed_review(Review, Total=False):
    pros: Annotated[list[str], "Return the list of pros if any."]
    cons: Annotated[list[str], "Return the list of cons if any."]


structured_model= model.with_structured_output(detailed_review)

result=structured_model.invoke("5 stars. Absolutely fire!!!")

print(result)
print(result["summary"])
print(result['sentiment'])