""" To run this example:

uvicorn card_builder_templates:app --reload --port 8080

"""
import random

from gapps import CardService
from gapps.cardservice import models
from gapps.cardservice.utilities import decode_email, decode_user

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(title="Cards Generator")


@app.get("/")
async def root():
    return {"message": "Welcome to Card Generator example!"}


@app.post("/homepage", response_class=JSONResponse)
async def homepage(gevent: models.GEvent):
    user_info = decode_user(gevent.authorizationEventObject.userIdToken)
    print(f"USER INFO: {user_info}")
    email = decode_email(gevent.authorizationEventObject.userIdToken)
    print(f"USER email: {email}")

    cards = [build_users_list_card, build_multi_section_card, build_user_card,
             build_email_card, build_form_controls_card]

    # Select a random card to display
    page = random.choice(cards)()
    return page


def build_users_list_card():
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')  # noqa: E501

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel('Software engineer')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1Divider1 = CardService.newDivider()

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png')  # noqa: E501

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Jane Doe')  \
        .setBottomLabel('Product manager')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1Divider2 = CardService.newDivider()

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1')  # noqa: E501

    cardSection1DecoratedText3 = CardService.newDecoratedText()  \
        .setText('Jamie Doe')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText3Icon1)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('List of users')  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1Divider1) \
        .addWidget(cardSection1DecoratedText2)  \
        .addWidget(cardSection1Divider2) \
        .addWidget(cardSection1DecoratedText3)  \

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()

    return card


def build_multi_section_card():
    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('Item 1')  \
        .setBottomLabel('Info for Item 1 list 1')

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Item 2')  \
        .setBottomLabel('Info for Item 2 list 1')  \

    cardSection1 = CardService.newCardSection()  \
        .setHeader('Items list 1')  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1DecoratedText2)  \

    cardSection2DecoratedText1 = CardService.newDecoratedText()  \
        .setText('Item 1')  \
        .setBottomLabel('Info for Item 1 list 2')  \

    cardSection2DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Item 2')  \
        .setBottomLabel('Info for Item 2 list 2')  \

    cardSection2 = CardService.newCardSection()  \
        .setHeader('Items list 2')  \
        .addWidget(cardSection2DecoratedText1)  \
        .addWidget(cardSection2DecoratedText2)  \

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .addSection(cardSection2)  \
        .build()
    return card


def build_user_card():
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/email/v6/grey600-24dp/1x/gm_email_grey600_24dp.png'  # noqa: E501
        )

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('john.doe@mail.com')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/chat/v6/grey600-24dp/1x/gm_chat_grey600_24dp.png'  # noqa: E501
        )

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Online')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/call/v6/grey600-24dp/1x/gm_call_grey600_24dp.png'  # noqa: E501
        )

    cardSection1DecoratedText3 = CardService.newDecoratedText()  \
        .setText('+1 9897671432')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText3Icon1)

    cardSection1DecoratedText4 = CardService.newDecoratedText()  \
        .setText('Recent emails')

    cardSection1DecoratedText5 = CardService.newDecoratedText()  \
        .setTopLabel('19:23')  \
        .setText(
            'Greece planning/vacation recommendations — We stayed in Santorini for the first day'  # noqa: E501
        )  \
        .setWrapText(True)

    cardSection1DecoratedText6 = CardService.newDecoratedText()  \
        .setTopLabel('Nov 8')  \
        .setText(
            'Chocolate Factory Tour  — Congratulations on finding the golden ticket! The tour begins.'  # noqa: E501
        )  \
        .setWrapText(True)

    cardSection1ButtonList1Button1Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button1 = CardService.newTextButton()  \
        .setText('Fetch more emails')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1ButtonList1Button1Action1)

    cardSection1ButtonList1Button2Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button2 = CardService.newTextButton()  \
        .setText('EDIT')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1ButtonList1Button2Action1)

    cardSection1ButtonList1Button3Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button3 = CardService.newTextButton()  \
        .setText('MORE..')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1ButtonList1Button3Action1)

    cardSection1ButtonList1 = CardService.newButtonSet()  \
        .addButton(cardSection1ButtonList1Button1)  \
        .addButton(cardSection1ButtonList1Button2)  \
        .addButton(cardSection1ButtonList1Button3)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('Contact details')  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1DecoratedText2)  \
        .addWidget(cardSection1DecoratedText3)  \
        .addWidget(cardSection1DecoratedText4)  \
        .addWidget(cardSection1DecoratedText5)  \
        .addWidget(cardSection1DecoratedText6)  \
        .addWidget(cardSection1ButtonList1)

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()
    return card


def build_email_card():
    cardSection1DecoratedText1Button1Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1DecoratedText1Button1 = CardService.newTextButton()  \
        .setText('REPLY')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1DecoratedText1Button1Action1)  \

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('john.doe@mail.com')  \
        .setBottomLabel('sender')  \
        .setButton(cardSection1DecoratedText1Button1)

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setTopLabel('Nov 8')  \
        .setText(
            'Chocolate Factory Tour  — Congratulations on finding the golden ticket! The tour begins.'  # noqa: E501
        )  \
        .setWrapText(True)

    cardSection1DecoratedText3 = CardService.newDecoratedText()  \
        .setText('Location details')

    cardSection1DecoratedText4Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/location_on/v6/grey600-36dp/1x/gm_location_on_grey600_36dp.png'  # noqa: E501
        )

    cardSection1DecoratedText4 = CardService.newDecoratedText()  \
        .setText('274 Beacon Dr, Bradenton, FL 34203')  \
        .setStartIcon(cardSection1DecoratedText4Icon1)  \
        .setWrapText(True)

    cardSection1Image1 = CardService.newImage()  \
        .setImageUrl('https://huurbs.com/images/google-map.jpg')  \
        .setAltText('Placeholder image')  \

    cardSection1 = CardService.newCardSection()  \
        .setHeader('Contact details')  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1DecoratedText2)  \
        .addWidget(cardSection1DecoratedText3)  \
        .addWidget(cardSection1DecoratedText4)  \
        .addWidget(cardSection1Image1)

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()
    return card


def build_form_controls_card():
    cardSection1TextInput1 = CardService.newTextInput()  \
        .setFieldName('name')  \
        .setTitle('Name')  \
        .setMultiline(False)

    cardSection1TextInput2 = CardService.newTextInput()  \
        .setFieldName('email')  \
        .setTitle('Email')  \
        .setMultiline(False)

    cardSection1TextInput3 = CardService.newTextInput()  \
        .setFieldName('address')  \
        .setTitle('Address')  \
        .setMultiline(True)

    cardSection1DatePTimePicker1 = CardService.newDateTimePicker()  \
        .setFieldName('dateTime')  \
        .setTitle('Pick a date and time')

    cardSection1DecoratedText1Switch1 = CardService.newSwitch()  \
        .setControlType(CardService.SwitchControlType.CHECK_BOX)  \
        .setFieldName('saveFavorite')

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('Add to favorites')  \
        .setSwitchControl(cardSection1DecoratedText1Switch1)

    cardSection1DecoratedText2Switch1 = CardService.newSwitch()  \
        .setControlType(CardService.SwitchControlType.CHECK_BOX)  \
        .setFieldName('mergeContact')

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Merge with existing contacts')  \
        .setSwitchControl(cardSection1DecoratedText2Switch1)

    cardSection1SelectionInput1 = CardService.newSelectionInput()  \
        .setFieldName('contactType')  \
        .setTitle('Contact type')  \
        .setType(CardService.SelectionInputType.RADIO_BUTTON)  \
        .addItem('Work', 'Work', False)  \
        .addItem('Personal', 'Personal', False)

    cardSection1ButtonList1Button1Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button1 = CardService.newTextButton()  \
        .setText('Submit')  \
        .setBackgroundColor('#66b73a')  \
        .setTextButtonStyle(CardService.TextButtonStyle.FILLED)  \
        .setOnClickAction(cardSection1ButtonList1Button1Action1)

    cardSection1ButtonList1Button2Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button2 = CardService.newTextButton()  \
        .setText('EDIT')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1ButtonList1Button2Action1)

    cardSection1ButtonList1Button3Action1 = CardService.newAction()  \
        .setFunctionName('TODO')  \
        .setParameters({})

    cardSection1ButtonList1Button3 = CardService.newTextButton()  \
        .setText('MORE..')  \
        .setTextButtonStyle(CardService.TextButtonStyle.TEXT)  \
        .setOnClickAction(cardSection1ButtonList1Button3Action1)

    cardSection1ButtonList1 = CardService.newButtonSet()  \
        .addButton(cardSection1ButtonList1Button1)  \
        .addButton(cardSection1ButtonList1Button2)  \
        .addButton(cardSection1ButtonList1Button3)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('Add new contact')  \
        .addWidget(cardSection1TextInput1)  \
        .addWidget(cardSection1TextInput2)  \
        .addWidget(cardSection1TextInput3)  \
        .addWidget(cardSection1DatePTimePicker1)  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1DecoratedText2)  \
        .addWidget(cardSection1SelectionInput1)  \
        .addWidget(cardSection1ButtonList1)  \

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()
    return card
