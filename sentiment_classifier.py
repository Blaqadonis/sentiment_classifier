from fastapi import FastAPI
from pydantic import BaseModel, conlist
import os
import cohere
from cohere.responses.classify import Example

api_key = os.environ['api_key']
co = cohere.Client(api_key)
app = FastAPI()

class ProductReviews(BaseModel):
  reviews: conlist(str)

@app.post("/baselineprediction")
def predict_sentiment(product_reviews: ProductReviews):
  response = co.classify(
    model='embed-english-v3.0',
    inputs=product_reviews.reviews,
    examples=[Example("The order came 5 days early", "positive"), 
              Example("The item exceeded my expectations", "positive"), 
              Example("I ordered more for my friends", "positive"), 
              Example("I would buy this again", "positive"), 
              Example("I would recommend this to others", "positive"), 
              Example("The package was damaged", "negative"),
              Example("The order is 5 days late", "negative"), 
              Example("The order was incorrect", "negative"), 
              Example("I want to return my item", "negative"), 
              Example("The item\'s material feels low quality", "negative"), 
              Example("The item was nothing special", "neutral"), 
              Example("I would not buy this again but it wasn\'t a waste of money", "neutral"), 
              Example("The item was neither amazing or terrible", "neutral"), 
              Example("The item was okay", "neutral"), 
              Example("I have no emotions towards this item", "neutral")])

  return response.classifications