import logging
import random
import praw
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    title: str = Field(..., example='DS TODO: Insert example title here to show up in docs')
    body: str = Field(..., example='DS TODO: Same')

# Load your pickled model here:
# model = pickle.load ...

@router.post('/predict')
async def predict(item: Item):
    """Make random baseline predictions for classification problem."""

    # You can access the attributes like this:
    post = item.title + ' ' + item.body

    log.info(post)

    # Then use your pickled model:
    # y_pred = model.decision_function(post)[0]

    return {
        'title': "Is Fusion nullified for the Extreme Z Awakening Event?",
        'post': "On JP I missed out on my chance to do SSJ3 Goku the first time so I'm doing it now. Been lucked out of rotations for most of these stages and I've noticed that for my Fusions team, LR Gogeta would NEVER fuse. I'm genuinely curious if the mechanic is nullified for the event or i'm just getting AWFUL RNG.",
        'prediction': ["DBZDokkanBattle", "Subreddit2", "Subreddit3", "Subreddit4", "Subreddit5", "Subreddit6", "Subreddit7", "Subreddit8", "Subreddit9", "Subreddit10"]   
    }
