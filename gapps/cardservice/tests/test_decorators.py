from gapps import CardService
from gapps.cardservice import decorators as dec
from dataclasses_json import LetterCase, dataclass_json
from dataclasses import dataclass


def create_basic_cards():
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIcon(CardService.Icon.FLIGHT_ARRIVAL)  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel('Software engineer')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png')

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Jane Doe')  \
        .setBottomLabel('Product manager')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1')

    cardSection1DecoratedText3 = CardService.newDecoratedText()  \
        .setText('Jamie Doe')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText3Icon1)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('List of users')  \
        .addWidget(cardSection1DecoratedText1)  \
        .addWidget(cardSection1DecoratedText2)  \
        .addWidget(cardSection1DecoratedText3)  \

    card = CardService.newCardBuilder()  \
        .addSection(cardSection1)  \
        .build()

    return card


def test_appscript_decorator():

    @dec.appscript
    @dataclass_json(letter_case=LetterCase.CAMEL)
    @dataclass
    class Person:
        friends: list
        name: str
        age: int

    te = Person(name='jon', age='4', friends=[]).addFriends(3).addFriends(4)
    assert te.to_dict() == {'friends': [3, 4], 'name': 'jon', 'age': '4'}
