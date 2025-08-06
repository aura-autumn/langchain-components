from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()

model=ChatOpenAI()

#Schema
json_schema={
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "title": "Key Themes",
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of key themes discussed in the review."
    },
    "summary": {
      "title": "Summary",
      "type": "string",
      "description": "A brief summary of the review."
    },
    "sentiment": {
      "title": "Sentiment",
      "type": "string",
      "description": "Return sentiment of the review-negative, positive, or neutral.",
      "enum": [
        "Pos",
        "Neg",
        "Neu"
      ]
    },
    "pros": {
      "title": "Pros",
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "Return the list of pros if any.",
      "default": "null"
    },
    "cons": {
      "title": "Cons",
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "Return the list of cons if any.",
      "default": "null"
    },
    "name": {
      "title": "Name",
      "type": "string",
      "description": "Return the name of the reviewer.",
      "default": "Anonymous"
    }
  },
  "required": [
    "key_themes",
    "summary",
    "sentiment"
  ]
}



structured_model= model.with_structured_output(json_schema)

result=structured_model.invoke("5 stars. Absolutely fire!!!")

print(result)