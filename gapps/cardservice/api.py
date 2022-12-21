

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, LetterCase

from .decorators import appscript
from .constants import (BorderType, ComposedEmailType, ContentType,
                        DisplayStyle, GridItemLayout, HorizontalAlignment,
                        Icon, ImageCropType, ImageStyle, LoadIndicator,
                        OnClose, OpenAs, SelectionInputType, SwitchControlType,
                        TextButtonStyle, UpdateDraftBodyType)
from .utilities import delete_none, update_actions, hex2floats, floats2hex


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SelectionItem:
    text: str = ''
    value: str = ''
    selected: bool = False


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Action:
    function_name: str = field(metadata=config(field_name="function"),
                               default=None)
    load_indicator: LoadIndicator = None
    parameters: dict = field(
        metadata=config(
            encoder=lambda x: [{"key": k, "value": v}
                               for k, v in x.items()] if x else [{}],
            decoder=lambda x: {item["key"]: item["value"] for item in x}),
        default=None)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ActionResponse:

    def printJson(self):
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class IconImage:
    alt_text: str = None
    icon: Icon = None
    icon_url: str = ''
    image_crop_type: ImageCropType = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OpenLink:
    on_close: OnClose = None
    open_as: OpenAs = None
    url: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Navigation:

    def popCard(self):
        """Pop a card from the navigation stack."""
        res = [{"popCard": True}]
        return res

    def popToNamedCard(self, card_name):
        """Pop to the specified card by its card name."""
        res = [{"popToCard": card_name}]
        return res

    def popToRoot(self):
        """Pop the card stack to the root card."""
        res = [{"popToRoot": True}]
        return res

    def pushCard(self, card):
        """Push the given card onto the stack."""
        card = card["action"]["navigations"][0]["pushCard"]
        res = [{"pushCard": card}]
        return res

    def updateCard(self, card):
        """Update the current card with the given card."""
        card = card["action"]["navigations"][0]["pushCard"]
        res = [{"updateCard": card}]
        return res

    def printJson(self):
        """Print the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Notification:
    text: str = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ActionResponseBuilder:
    navigation: Navigation = field(metadata=config(field_name="navigations"),
                                   default=None)
    notification: Notification = None
    open_link: OpenLink = None
    state_changed: bool = None

    def build(self):
        """Build the current action response and validates it."""
        card = self.to_dict()
        card = delete_none(card)
        card = {'renderActions': {"action": card}}
        print(card)
        return card


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Attachment:
    icon_url: str = ''
    mime_type: str = ''
    resource_url: str = ''
    title: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AuthorizationAction:
    authorization_url: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AuthorizationException:
    authorization_url: str = ''
    custom_ui_callback: str = ''
    resource_display_name: str = ''

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())

    def throwException(self):
        """Throws an exception with the JSON representation of this object."""
        raise self


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BorderStyle:
    corner_radius: int = 8
    stroke_color: str = '#000000'
    type: BorderType = BorderType.NO_BORDER


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Button:
    authorization_action: Action = None
    compose_action: tuple[Action, ComposedEmailType] = None
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ButtonSet:
    button: list[Button] = field(metadata=config(field_name="buttons"),
                                 default=None)

    def field_name(self):
        """Return and override classname."""
        return "buttonList"


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Card:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CardAction:
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    text: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CardHeader:
    image_alt_text: str = ''
    image_style: ImageStyle = field(
        metadata=config(field_name="imageType", encoder=lambda x: x.value,
                        decoder=ImageStyle),
        default=ImageStyle.CIRCLE)
    image_url: str = ''
    subtitle: str = ''
    title: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TextButton:
    alt_text: str = None
    authorization_action: AuthorizationAction = None
    background_color: str = field(
        metadata=config(
            field_name="color",
            encoder=lambda x: {k: v for k, v in zip(["red", "green", "blue"],
                                                    hex2floats(x))}
            if x else None,
            decoder=lambda x: floats2hex([x.values()]) if x else None),
        default=None)
    compose_action: tuple[Action, ComposedEmailType] = None
    disabled: bool = None
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = field(
        metadata=config(field_name="openDynamicLinkAction"), default=None)
    open_link: OpenLink = None
    text_button_style: TextButtonStyle = field(
        metadata=config(encoder=lambda x: x.value, decoder=TextButtonStyle,
                        field_name="buttonStyle", exclude=lambda x: True),
        default=TextButtonStyle.TEXT)
    text: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FixedFooter:
    primary_button: TextButton = None
    secondary_button: TextButton = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Divider:
    pass


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DriveItemsSelectedActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DriveItemsSelectedActionResponseBuilder:
    _item_id: str = field(metadata=config(exclude=lambda x: True),
                          default='')

    def build(self):
        """Build the current action response and validates it."""
        card = {'renderActions':
                {"hostAppAction":
                    {"driveAction":
                        {"requestFileScope": {"itemId": self._item_id}}}}}
        print(card)
        return card

    def requestFileScope(self, itemId):
        """Request file scope."""
        self._item_id = itemId
        return self


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EditorFileScopeActionResponse:

    def printJson(self):
        """Print the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EditorFileScopeActionResponseBuilder:
    _item_id: str = field(metadata=config(exclude=lambda x: True),
                          default='')

    def build(self):
        """Build the current action response and validates it."""
        card = {'renderActions':
                {"hostAppAction":
                    {"editorAction":
                        {"requestFileScopeForActiveDocument": {}}}}}
        print(card)
        return card

    def requestFileScopeForActiveDocument(self, itemId):
        """Request file scope."""
        self._item_id = itemId
        return self


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Switch:
    control_type: SwitchControlType = field(
        metadata=config(encoder=lambda x: x.value, decoder=SwitchControlType),
        default=SwitchControlType.SWITCH)
    field_name: str = field(metadata=config(field_name="name"), default='')
    on_change_action: Action = None
    selected: bool = False
    value: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DecoratedText:
    authorization_action: Action = None
    bottom_label: str = None
    button: Button = None
    compose_action: tuple[Action, ComposedEmailType] = None
    end_icon: IconImage = None
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    start_icon: IconImage = None
    switch_control: Switch = None
    text: str = ''
    top_label: str = None
    wrap_text: str = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DatePicker:
    field_name: str = ''
    on_change_action: Action = None
    title: str = ''
    value_in_ms_since_epoch: int = 0


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DateTimePicker:
    field_name: str = field(metadata=config(field_name="name"), default='')
    on_change_action: Action = None
    time_zone_offset_in_mins: int = field(
        metadata=config(field_name="timezoneOffsetDate"), default=0)
    title: str = field(metadata=config(field_name="label"), default='')
    value_in_ms_since_epoch: int = field(
        metadata=config(field_name="valueMsEpoch"), default=0)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Image:
    alt_text: str = ''
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    image_url: str = ''
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ImageButton:
    alt_text: str = ''
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    icon: Icon = Icon.NONE
    icon_url: str = ''
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ImageCropStyle:
    aspect_ratio: float = 1.0
    image_crop_type: ImageCropType = field(
        metadata=config(encoder=lambda x: x.value, decoder=ImageCropType),
        default=ImageCropType.CIRCLE)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ImageComponent:
    alt_text: str = ''
    border_style: BorderStyle = None
    crop_style: ImageCropStyle = None
    image_url: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CardSection:
    widget: list = field(metadata=config(field_name="widgets"), default=None)
    collapsible: bool = False
    header: str = ""
    num_uncollapsible_widgets: int = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CardBuilder:
    card_action: list[CardAction] = None
    section: list[CardSection] = field(metadata=config(field_name="sections"),
                                       default=None)
    display_style: DisplayStyle = None
    fixed_footer: FixedFooter = None
    header: CardHeader = None
    name: str = None
    peek_card_header: CardHeader = None

    def build(self):
        """Build the current card and validates it."""
        card = self.to_dict()
        card['sections'] = []
        for section in self.section:
            d_section = section.to_dict()
            d_section['widgets'] = []
            for widget in section.widget:
                if hasattr(widget, "field_name") and  \
                   callable(getattr(widget, "field_name")):
                    name = widget.field_name()
                else:
                    name = widget.__class__.__name__
                    name = name[0].lower() + name[1:]
                d_section['widgets'].append({name: widget.to_dict()})
            card['sections'].append(d_section)

        card = delete_none(card)
        card = update_actions(card)
        print(card)

        page = {"action": {"navigations": [{"pushCard": card}]}}
        return page


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ComposeActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ComposeActionResponseBuilder:
    # gmail_draft: GmailDraft = None

    def build(self):
        """Builds the current compose action response and validates it."""
        card = {'renderActions':
                {"hostAppAction":
                    {"gmailAction":
                        {"addonComposeUiActionMarkup": {"type": {}}}}}}
        print(card)
        return card


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ConferenceData:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CalendarEventActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CalendarEventActionResponseBuilder:
    attachments: list[Attachment] = field(
        metadata=config(field_name="addAttachmentsActionMarkup"), default=None)
    attendees: list[str] = field(
        metadata=config(field_name="editAttendeesActionMarkup"), default=None)
    conference_data: ConferenceData = field(
        metadata=config(field_name="editConferenceDataActionMarkup"),
        default=None)

    def build(self):
        """Builds the current action response and validates it."""
        card = self.to_dict()
        card = delete_none(card)
        card = {'renderActions':
                {"hostAppAction":
                    {"calendarAction": card}}}
        print(card)
        return card


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GridItem:
    identifier: str = None
    image: ImageComponent = None
    layout: GridItemLayout = field(metadata=config(encoder=lambda x: x.value,
                                                   decoder=GridItemLayout),
                                   default=GridItemLayout.TEXT_BELOW)
    subtitle: str = None
    text_alignment: HorizontalAlignment = field(
        metadata=config(encoder=lambda x: x.value,
                        decoder=HorizontalAlignment),
        default=HorizontalAlignment.START)
    title: str = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Grid:
    item: list[GridItem] = None
    authorization_action: AuthorizationAction = None
    border_style: BorderStyle = field(default_factory=BorderStyle)
    compose_action: tuple[Action, ComposedEmailType] = None
    num_columns: int = 1
    on_click_action: Action = field(metadata=config(field_name="onClick"),
                                    default=None)
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    title: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SelectionInput:
    item: list[SelectionItem] = field(
        metadata=config(field_name="selection_item"), default=None)
    field_name: str = field(metadata=config(field_name="name"), default='')
    on_change_action: Action = None
    title: str = field(metadata=config(field_name="label"), default='')
    type: SelectionInputType = field(
        metadata=config(encoder=lambda x: x.value, decoder=SelectionInputType),
        default=SelectionInputType.DROPDOWN)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Suggestions:
    suggestion: list[str] = None
    suggestions: list[list[str]] = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuggestionsResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuggestionsResponseBuilder:
    suggestions: Suggestions = None

    def build(self):
        """Builds the current suggestions response and validates it."""
        return SuggestionsResponse()


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TextInput:
    field_name: str = field(metadata=config(field_name="name"), default='')
    hint: str = field(metadata=config(field_name="hintText"), default='')
    multiline: bool = field(
        metadata=config(
            field_name="type",
            encoder=lambda x: 'MULTIPLE_LINE' if x else 'SINGLE_LINE',
            decoder=lambda x: x == 'MULTIPLE_LINE'),
        default=False)
    on_change_action: Action = None
    suggestions: Suggestions = None
    suggestions_action: Action = None
    title: str = field(metadata=config(field_name="label"), default='')
    value: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TextParagraph:
    text: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TimePicker:
    field_name: str = ''
    hours: int = 0   # 0-23
    minutes: int = 0  # 0-59
    on_change_action: Action = None
    title: str = ''


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UniversalActionResponse:
    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UniversalActionResponseBuilder:
    open_link: OpenLink = None

    def build(self):
        """Builds the current universal action response and validates it."""
        return UniversalActionResponse()

    def displayAddOnCards(self, cardObjects: list):
        """Displays the add-on with the specified cards."""
        return UniversalActionResponse()


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftActionResponse:
    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftBccRecipientsAction:
    update_bcc_recipients: list[str] = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class InsertContent:
    content: str = None
    content_type: ContentType = field(
        metadata=config(encoder=lambda x: x.value,
                        decoder=ContentType),
        default=ContentType.UNSPECIFIED_CONTENT_TYPE)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftBodyAction:
    update_content: list[InsertContent] = field(
        metadata=config(
            field_name='insertContents',
            encoder=lambda x: [{"content": c, "contentType": t.value}
                               for c, t in x] if x else None),
        default=None)
    update_type: UpdateDraftBodyType = field(
        metadata=config(field_name='type',
                        encoder=lambda x: x.value,
                        decoder=UpdateDraftBodyType),
        default=UpdateDraftBodyType.UNSPECIFIED_ACTION_TYPE)


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftCcRecipientsAction:
    update_cc_recipients: list[str] = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftSubjectAction:
    update_subject: list[str] = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftToRecipientsAction:
    update_to_recipients: list[str] = None


@appscript
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateDraftActionResponseBuilder:
    update_draft_bcc_recipients_action: UpdateDraftBccRecipientsAction = field(
        metadata=config(field_name="updateBccRecipients"), default=None)
    update_draft_body_action: UpdateDraftBodyAction = field(
        metadata=config(field_name="updateBody"), default=None)
    update_draft_cc_recipients_action: UpdateDraftCcRecipientsAction = field(
        metadata=config(field_name="updateCcRecipients"), default=None)
    update_draft_subject_action: UpdateDraftSubjectAction = field(
        metadata=config(field_name="updateSubject"), default=None)
    update_draft_to_recipients_action: UpdateDraftToRecipientsAction = field(
        metadata=config(field_name="updateToRecipients"), default=None)

    def build(self):
        """Build the current universal action response and validates it."""
        card = self.to_dict()
        card = delete_none(card)
        card = {'renderActions':
                {"hostAppAction":
                    {"gmailAction":
                        {"updateDraftActionMarkup": card}}}}
        print(card)
        return card
