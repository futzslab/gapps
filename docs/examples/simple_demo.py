""" To run this example: uvicorn simple_demo:app --reload --port 8080 """

from gapps import CardService
from gapps.cardservice import models
from gapps.cardservice.utilities import decode_email

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(title="Cats example")


@app.get("/")
async def root():
    return {"message": "Welcome to Simple Demo App example"}


@app.post("/homepage", response_class=JSONResponse)
async def homepage(gevent: models.GEvent):
    email = decode_email(gevent.authorizationEventObject.userIdToken)

    page = build_cards(email)
    return page


def build_cards(email):
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')  # noqa: E501
    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel(email)  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('My Profile')  \
        .addWidget(cardSection1DecoratedText1)

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()

    return card
