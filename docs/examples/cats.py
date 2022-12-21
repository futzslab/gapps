""" To run this example: uvicorn simple_demo:app --reload --port 8080 """
from datetime import datetime
import pytz
from urllib.parse import quote

from gapps import CardService
from gapps.cardservice import models, utilities as ut

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import googleapiclient.discovery
import google.oauth2.credentials


app = FastAPI(title="Cats example")


@app.get("/")
async def root():
    return {"message": "Welcome to Cats App example"}


@app.post("/homepage", response_class=JSONResponse)
async def homepage(gevent: models.GEvent):
    date = datetime.now(tz=pytz.timezone(gevent.commonEventObject.timeZone.id))
    message = 'Good night'
    if 12 > date.hour >= 6:
        message = 'Good morning'
    elif 18 > date.hour >= 12:
        message = 'Good afternoon'

    message += ' ' + gevent.commonEventObject.hostApp

    return create_cat_card(message, True)


@app.post('/on_items_selected', response_class=JSONResponse)
async def on_drive_items_selected(gevent: models.GEvent):
    all_items = gevent.drive.selectedItems
    all_items = all_items[:5]  # Include at most 5 items in the text.
    print(all_items)

    text = '\n'.join([truncate(item.title) for item in all_items])
    return create_cat_card(text)


@app.post('/on_change_cat', response_class=JSONResponse)
async def on_change_cat(gevent: models.GEvent):
    """Callback for the 'Change cat' button.

    Parameters
    ----------
    gevent: models.GEvent
        e The event object. See the following link:
        https://developers.google.com/gmail/add-ons/concepts/actions#action_event_objects

    Returns
    -------
    response: CardService.ActionResponse
        The action response to apply.

    """
    # Get the text that was shown in the current cat image. This was passed as
    # a parameter on the Action set for the button.
    text = gevent.commonEventObject.parameters['text']

    # The isHomepage parameter is passed as a string, so convert to a Boolean.
    is_homepage = gevent.commonEventObject.parameters['is_homepage'] == 'True'

    # Create a new card with the same text.
    card = create_cat_card(text, is_homepage)

    # Create an action response that instructs the add-on to replace
    # the current card with the new one.
    navigation = CardService.newNavigation() \
        .updateCard(card)

    actionResponse = CardService.newActionResponseBuilder()  \
        .setNavigation(navigation)

    return actionResponse.build()


def truncate(message, max_message_length=40):
    """Truncate a message to fit in the cat image.

    Parameters
    ----------
    message : str
        message The message to truncate.
    max_message_length: int, optional
        the maximum number of characters that can fit in the cat image.
        default: 40

    Returns
    -------
    m_truncated: str
        The truncated message.

    """
    if len(message) > max_message_length:
        message = message[:40] + '...'

    return message


def create_cat_card(text, is_homepage=False):
    # Use the "Cat as a service" API to get the cat image. Add a "time" URL
    # parameter to act as a cache buster.
    now = datetime.now()
    # Replace forward slashes in the text, as they break the CataaS API.
    caption = text.replace('/', ' ')
    # encodeURIComponent
    caption = quote(caption, safe="!~*'()")
    imageUrl = f'https://cataas.com/cat/says/{caption}?time={now.timestamp()}'

    image = CardService.newImage() \
        .setImageUrl(imageUrl)  \
        .setAltText('Meow')

    # Create a button that changes the cat image when pressed.
    # Note: Action parameter keys and values must be strings.
    action = CardService.newAction()  \
        .setFunctionName('https://gwa.momentz.fr/on_change_cat') \
        .setParameters({'text': text, 'is_homepage': str(is_homepage)})

    button = CardService.newTextButton()  \
        .setText('Change cat')  \
        .setOnClickAction(action)  \
        .setTextButtonStyle(CardService.TextButtonStyle.FILLED)

    buttonSet = CardService.newButtonSet()  \
        .addButton(button)

    # Create a footer to be shown at the bottom.
    footer = CardService.newFixedFooter()  \
        .setPrimaryButton(CardService.newTextButton()
                          .setText('Powered by cataas.com')
                          .setOpenLink(CardService.newOpenLink()
                                       .setUrl('https://cataas.com')))

    # Assemble the widgets and return the card.
    section = CardService.newCardSection()  \
        .addWidget(image)  \
        .addWidget(buttonSet)

    card = CardService.newCardBuilder()  \
        .addSection(section) \
        .setFixedFooter(footer)

    if not is_homepage:
        # Create the header shown when the card is minimized,
        # but only when this card is a contextual card. Peek headers
        # are never used by non-contexual cards like homepages.
        peekHeader = CardService.newCardHeader()  \
            .setTitle('Contextual Cat')  \
            .setImageUrl('https://www.gstatic.com/images/icons/material/system/1x/pets_black_48dp.png')  \
            .setSubtitle(text)

        card.setPeekCardHeader(peekHeader)

    return card.build()


@app.post('/on_gmail_message', response_class=JSONResponse)
def on_gmail_message(gevent: models.GEvent):
    """Callback for rendering the card for a specific Gmail message.

    Parameters
    ----------
    gevent: models.GEvent
        e The event object. See the following link:
        https://developers.google.com/gmail/add-ons/concepts/actions#action_event_objects

    Returns
    -------
    response: CardService.Card
        The card to show to the user.

    """
    # Get the ID of the message the user has open.
    # messageId = gevent.gmail.messageId

    # Get an access token scoped to the current message and use it for GmailApp
    # calls.
    access_token = gevent.authorizationEventObject.userOAuthToken
    cred = google.oauth2.credentials.Credentials(access_token)
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=cred)

    # Get current message. We do not use it, this is just for demo.
    # message = service.users().messages().get(userId='me',
    #                                          id=messageId).execute()

    # Get current message Thread
    thread = service.users().threads().get(userId='me',
                                           id=gevent.gmail.threadId).execute()
    # print(f"NB Threads: {len(thread['messages'])}")

    # Get the subject of the email.
    subject = ''
    for t in thread['messages'][0]['payload']['headers']:
        if t.get('name', '') == 'Subject':
            subject = t.get('value')

    # If neccessary, truncate the subject to fit in the image.
    subject = truncate(subject)

    return create_cat_card(subject)


@app.post('/on_gmail_compose', response_class=JSONResponse)
def on_gmail_compose(gevent: models.GEvent):
    """Callback for rendering the card for the compose action dialog.

    Parameters
    ----------
    gevent: models.GEvent
        e The event object. See the following link:
        https://developers.google.com/gmail/add-ons/concepts/actions#action_event_objects

    Returns
    -------
    response: CardService.Card
        The card to show to the user.

    """
    header = CardService.newCardHeader()  \
        .setTitle('Insert cat')  \
        .setSubtitle('Add a custom cat image to your email message.')

    # Create text input for entering the cat's message.
    text_input = CardService.newTextInput()  \
        .setFieldName('text')  \
        .setTitle('Caption')  \
        .setHint('What do you want the cat to say?')

    # Create a button that inserts the cat image when pressed.
    action = CardService.newAction()  \
        .setFunctionName('https://gwa.momentz.fr/on_gmail_insert_cat')

    button = CardService.newTextButton()  \
        .setText('Insert cat')  \
        .setOnClickAction(action)  \
        .setTextButtonStyle(CardService.TextButtonStyle.FILLED)

    buttonSet = CardService.newButtonSet().addButton(button)

    # Assemble the widgets and return the card.
    section = CardService.newCardSection()  \
        .addWidget(text_input)  \
        .addWidget(buttonSet)

    card = CardService.newCardBuilder()  \
        .setHeader(header)  \
        .addSection(section)

    return card.build()


@app.post('/on_gmail_insert_cat', response_class=JSONResponse)
def on_gmail_insert_cat(gevent: models.GEvent):
    """Callback for inserting a cat into the Gmail draft.

    Parameters
    ----------
    gevent: models.GEvent
        e The event object. See the following link:
        https://developers.google.com/gmail/add-ons/concepts/actions#action_event_objects

    Returns
    -------
    response: CardService.UpdateDraftActionResponse
        The draft update response.

    """
    # Get the text that was entered by the user.
    form_inputs = gevent.commonEventObject.formInputs
    text = ut.get_form_value(form_inputs, 'text')
    text = text[0] if len(text) else ''

    # Use the "Cat as a service" API to get the cat image. Add a "time" URL
    # parameter to act as a cache buster.
    now = datetime.now()
    imageUrl = 'https://cataas.com/cat'
    if text:
        # Replace forward slashes in the text, as they break the CataaS API.
        caption = text.replace('/', ' ')
        # encodeURIComponent
        caption = quote(caption, safe="!~*'()")
        imageUrl += f'/says/{caption}?time={now.timestamp()}'

    imageHtmlContent =   \
        f'<img style="display: block max-height: 300px" src="{imageUrl}"/>'

    draft_action = CardService.newUpdateDraftBodyAction()  \
        .addUpdateContent(imageHtmlContent,
                          CardService.ContentType.MUTABLE_HTML)  \
        .setUpdateType(CardService.UpdateDraftBodyType.IN_PLACE_INSERT)

    response = CardService.newUpdateDraftActionResponseBuilder()  \
        .setUpdateDraftBodyAction(draft_action)  \
        .build()

    return response


@app.post('/on_calendar_event_open', response_class=JSONResponse)
def on_calendar_event_open(gevent: models.GEvent):
    """Callback for rendering the card for a specific Calendar event.

    Parameters
    ----------
    gevent: models.GEvent
        e The event object. See the following link:
        https://developers.google.com/gmail/add-ons/concepts/actions#action_event_objects

    Returns
    -------
    response: CardService.Card
        The card to show to the user.

    """
    # Get the ID of the Calendar and the event
    calendar_id = gevent.calendar.calendarId
    event_id = gevent.calendar.id

    # Get an access token scoped to the current calendar
    access_token = gevent.authorizationEventObject.userOAuthToken
    cred = google.oauth2.credentials.Credentials(access_token)
    service = googleapiclient.discovery.build('calendar', 'v3',
                                              credentials=cred)

    # The event metadata doesn't include the event's title, so using the
    # calendar.readonly scope and fetching the event by it's ID.
    event = service.events().get(calendarId=calendar_id,
                                 eventId=event_id).execute()

    if not event:
        # This is a new event still being created.
        return create_cat_card('A new event! Am I invited?')

    title = event.get('summary', 'A new event! Should I go?')
    # If necessary, truncate the title to fit in the image.
    title = truncate(title)
    return create_cat_card(title)
