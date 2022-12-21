from gapps import CardService


def build_basic_cards():
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel('Software engineer')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1Divider1 = CardService.newDivider()

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png')

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Jane Doe')  \
        .setBottomLabel('Product manager')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1Divider2 = CardService.newDivider()

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1')

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

    expected = {'action': {'navigations': [{'pushCard': {'sections': [{'widgets': [{'decoratedText': {'bottomLabel': 'Software engineer', 'startIcon': {'iconUrl': 'https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png'}, 'text': 'John Doe'}}, {'divider': {}}, {'decoratedText': {'bottomLabel': 'Product manager', 'startIcon': {'iconUrl': 'https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png'}, 'text': 'Jane Doe'}}, {'divider': {}}, {'decoratedText': {'bottomLabel': 'Vice president', 'startIcon': {'iconUrl': 'https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1'}, 'text': 'Jamie Doe'}}], 'collapsible': False, 'header': 'List of users'}]}}]}}

    assert card == expected
    return card


def build_users_list_card():
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel('Software engineer')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1Divider1 = CardService.newDivider()

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png')

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Jane Doe')  \
        .setBottomLabel('Product manager')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1Divider2 = CardService.newDivider()

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1')

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
            'https://fonts.gstatic.com/s/i/googlematerialicons/email/v6/grey600-24dp/1x/gm_email_grey600_24dp.png'
        )

    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('john.doe@mail.com')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/chat/v6/grey600-24dp/1x/gm_chat_grey600_24dp.png'
        )

    cardSection1DecoratedText2 = CardService.newDecoratedText()  \
        .setText('Online')  \
        .setBottomLabel('Vice president')  \
        .setStartIcon(cardSection1DecoratedText2Icon1)

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()  \
        .setIconUrl(
            'https://fonts.gstatic.com/s/i/googlematerialicons/call/v6/grey600-24dp/1x/gm_call_grey600_24dp.png'
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
            'Greece planning/vacation recommendations — We stayed in Santorini for the first day'
        )  \
        .setWrapText(True)

    cardSection1DecoratedText6 = CardService.newDecoratedText()  \
        .setTopLabel('Nov 8')  \
        .setText(
            'Chocolate Factory Tour  — Congratulations on finding the golden ticket! The tour begins.'
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


def test_footer():
    cardFooter1Button1Action1 = CardService.newAction()  \
        .setFunctionName('https://gwa.momentz.fr/')  \
        .setParameters({})

    cardFooter1Button1Action2 = CardService.newAction()  \
        .setFunctionName('ttps://gwa.momentz.fr/2')  \
        .setParameters({})

    cardFooter1Button1OpenLink1 = CardService.newOpenLink()  \
        .setUrl('https://example.com')

    cardFooter1Button1 = CardService.newTextButton()  \
        .setText('Click me')  \
        .setOnClickAction(cardFooter1Button1Action1)  \
        .setOnClickOpenLinkAction(cardFooter1Button1Action2)  \
        .setOpenLink(cardFooter1Button1OpenLink1)

    cardFooter1 = CardService.newFixedFooter()  \
        .setPrimaryButton(cardFooter1Button1)

    cardSection1DecoratedText1Icon1 = CardService.newIconImage()  \
        .setIconUrl('https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png')
    cardSection1DecoratedText1 = CardService.newDecoratedText()  \
        .setText('John Doe')  \
        .setBottomLabel('Software Developer')  \
        .setStartIcon(cardSection1DecoratedText1Icon1)

    cardSection1 = CardService.newCardSection()  \
        .setHeader('My Profile')  \
        .addWidget(cardSection1DecoratedText1)

    card = CardService.newCardBuilder()  \
        .setFixedFooter(cardFooter1) \
        .addSection(cardSection1)  \
        .build()

    print(card)
    assert card == {'action': {'navigations': [{'pushCard': {'sections': [{'widgets': [{'decoratedText': {'bottomLabel': 'Software Developer', 'startIcon': {'iconUrl': 'https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png'}, 'text': 'John Doe'}}], 'collapsible': False, 'header': 'My Profile'}], 'fixedFooter': {'primaryButton': {'onClick': {'action': {'function': 'https://gwa.momentz.fr/', 'parameters': [{}]}, 'openDynamicLinkAction': {'function': 'ttps://gwa.momentz.fr/2', 'parameters': [{}]}, 'openLink': {'url': 'https://example.com'}}, 'text': 'Click me'}}}}]}}

# test_basic_cards()
# build_user_card()
# build_form_controls_card()
# test_footer()

# card = test_basic_cards()
# import ipdb; ipdb.set_trace()
# navigation = CardService.newNavigation().updateCard(card)
# te = CardService.newActionResponseBuilder().setNavigation(navigation)
# import ipdb; ipdb.set_trace()
# te.build()