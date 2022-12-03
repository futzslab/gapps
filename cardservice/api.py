

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config

from .decorators import appscript
from .constants import (BorderType, ComposedEmailType, ContentType,
                        DisplayStyle, GridItemLayout, HorizontalAlignment,
                        Icon, ImageCropType, ImageStyle, LoadIndicator,
                        OnClose, OpenAs, SelectionInputType, SwitchControlType,
                        TextButtonStyle, UpdateDraftBodyType)
from .utilities import delete_none

@appscript
@dataclass_json
@dataclass
class Person:
    friends: list
    name: str
    age: int


@appscript
@dataclass_json
@dataclass
class Action:
    function_name: str = None
    load_indicator: LoadIndicator = None
    parameters: dict = None


@appscript
@dataclass_json
@dataclass
class ActionResponse:

    def printJson(self):
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class IconImage:
    alt_text: str = None
    icon: Icon = None
    icon_url: str = ''
    image_crop_type: ImageCropType = None


@appscript
@dataclass_json
@dataclass
class OpenLink:
    on_close: OnClose = None
    open_as: OpenAs = None
    url: str = ''


@appscript
@dataclass_json
@dataclass
class Navigation:

    def popCard(self):
        """Pops a card from the navigation stack."""
        return {}

    def popToNamedCard(self, cardName):
        """Pops to the specified card by its card name."""
        return {}

    def popToRoot(self):
        """Pops the card stack to the root card."""
        return {}

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())

    def pushCard(self, card):
        """Pushes the given card onto the stack."""
        return {}

    def updateCard(self, card):
        """Updates the current card with the given card."""
        return {}


@appscript
@dataclass_json
@dataclass
class Notification:
    text: str = None


@appscript
@dataclass_json
@dataclass
class ActionResponseBuilder:
    navigation:	Navigation = None
    notification: Notification = None
    open_link: OpenLink = None
    state_changed: bool = False

    def build(self):
        """Builds the current action response and validates it."""
        return ActionResponse()


@appscript
@dataclass_json
@dataclass
class Attachment:
    icon_url: str = ''
    mime_type: str = ''
    resource_url: str = ''
    title: str = ''


@appscript
@dataclass_json
@dataclass
class AuthorizationAction:
    authorization_url: str = ''


@appscript
@dataclass_json
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
@dataclass_json
@dataclass
class BorderStyle:
    corner_radius: int = 8
    stroke_color: str = '#000000'
    type: BorderType = BorderType.NO_BORDER


@appscript
@dataclass_json
@dataclass
class Button:
    authorization_action: Action = None
    compose_action: tuple[Action, ComposedEmailType] = None
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json
@dataclass
class ButtonSet:
    button: list[Button] = None


@appscript
@dataclass_json
@dataclass
class Card:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class CardAction:
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    text: str = ''


@appscript
@dataclass_json
@dataclass
class CardHeader:
    image_alt_text: str = ''
    image_style: ImageStyle = ImageStyle.CIRCLE
    image_url: str = ''
    subtitle: str = ''
    title: str = ''


@appscript
@dataclass_json
@dataclass
class TextButton:
    alt_text: str = ''
    authorization_action: AuthorizationAction = None
    background_color: str = TextButtonStyle.TEXT
    compose_action: tuple[Action, ComposedEmailType] = None
    disabled: bool = False
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    text_button_style: TextButtonStyle = TextButtonStyle.TEXT
    text: str = ''


@appscript
@dataclass_json
@dataclass
class FixedFooter:
    primary_button: TextButton = None
    secondary_button: TextButton = None


@appscript
@dataclass_json
@dataclass
class Divider:
    pass


@appscript
@dataclass_json
@dataclass
class DriveItemsSelectedActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class DriveItemsSelectedActionResponseBuilder:

    def build(self):
        """Builds the current action response and validates it."""
        return DriveItemsSelectedActionResponse()

    def requestFileScope(self, itemId):
        """Requests file scope."""
        return self


@appscript
@dataclass_json
@dataclass
class EditorFileScopeActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class EditorFileScopeActionResponseBuilder:

    def build(self):
        """Builds the current action response and validates it."""
        return EditorFileScopeActionResponse()

    def requestFileScopeForActiveDocument(self, itemId):
        """Requests file scope."""
        return self


@appscript
@dataclass_json
@dataclass
class Switch:
    control_type: SwitchControlType = SwitchControlType.SWITCH
    field_name: str = ''
    on_change_action: Action = None
    selected: bool = False
    value: str = ''


@appscript
@dataclass_json
@dataclass
class DecoratedText:
    authorization_action: Action = None
    bottom_label: str = None
    button: Button = None
    compose_action: tuple[Action, ComposedEmailType] = None
    end_icon: IconImage = None
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    start_icon: IconImage = None
    switch_control: Switch = None
    text: str = ''
    top_label: str = None
    wrap_text: str = None



@appscript
@dataclass_json
@dataclass
class DatePicker:
    field_name: str = ''
    on_change_action: Action = None
    title: str = ''
    value_in_ms_since_epoch: int = 0


@appscript
@dataclass_json
@dataclass
class DateTimePicker:
    field_name: str = ''
    on_change_action: Action = None
    time_zone_offset_in_mins: int = 0
    title: str = ''
    value_in_ms_since_epoch: int = 0


@appscript
@dataclass_json
@dataclass
class Image:
    alt_text: str = ''
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    image_url: str = ''
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json
@dataclass
class ImageButton:
    alt_text: str = ''
    authorization_action: AuthorizationAction = None
    compose_action: tuple[Action, ComposedEmailType] = None
    icon: Icon = Icon.NONE
    icon_url: str = ''
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None


@appscript
@dataclass_json
@dataclass
class ImageCropStyle:
    aspect_ratio: float = 1.0
    image_crop_type: ImageCropType = ImageCropType.CIRCLE


@appscript
@dataclass_json
@dataclass
class ImageComponent:
    alt_text: str = ''
    border_style: BorderStyle = None
    crop_style: ImageCropStyle = None
    image_url: str = ''


@appscript
@dataclass_json
@dataclass
class CardSection:
    widget: list = field(metadata=config(field_name="widgets"), default=None)
    collapsible: bool = False
    header: str = ""
    num_uncollapsible_widgets: int = 0


@appscript
@dataclass_json
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
        card = delete_none(card)
        print(card)
        import ipdb; ipdb.set_trace()
        return card


@appscript
@dataclass_json
@dataclass
class ComposeActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class ComposeActionResponseBuilder:
    # gmail_draft: GmailDraft = None

    def build(self):
        """Builds the current compose action response and validates it."""
        return ComposeActionResponse()


@appscript
@dataclass_json
@dataclass
class ConferenceData:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class CalendarEventActionResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class CalendarEventActionResponseBuilder:
    attachments: list[Attachment] = None
    attendees: list[str] = None
    conference_data: ConferenceData = None

    def build(self):
        """Builds the current action response and validates it."""
        return CalendarEventActionResponse()


@appscript
@dataclass_json
@dataclass
class GridItem:
    identifier: str = None
    image: ImageComponent = None
    layout: GridItemLayout = GridItemLayout.TEXT_BELOW
    subtitle: str = None
    text_alignment: HorizontalAlignment = HorizontalAlignment.START
    title: str = None


@appscript
@dataclass_json
@dataclass
class Grid:
    item: list[GridItem] = None
    authorization_action: AuthorizationAction = None
    border_style: BorderStyle = BorderStyle()
    compose_action: tuple[Action, ComposedEmailType] = None
    num_columns: int = 1
    on_click_action: Action = None
    on_click_open_link_action: Action = None
    open_link: OpenLink = None
    title: str = ''


@appscript
@dataclass_json
@dataclass
class SelectionInput:
    item: list[tuple[str, str, bool]] = None
    field_name: str = ''
    on_change_action: Action = None
    title: str = ''
    type: SelectionInputType = SelectionInputType.DROPDOWN


@appscript
@dataclass_json
@dataclass
class Suggestions:
    suggestion: list[str] = None
    suggestions: list[list[str]] = None


@appscript
@dataclass_json
@dataclass
class SuggestionsResponse:

    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class SuggestionsResponseBuilder:
    suggestions: Suggestions = None

    def build(self):
        """Builds the current suggestions response and validates it."""
        return SuggestionsResponse()


@appscript
@dataclass_json
@dataclass
class TextInput:
    field_name: str = ''
    hint: str = ''
    multiline: bool = False
    on_change_action: Action = None
    suggestions: Suggestions = None
    suggestions_action: Action = None
    title: str = ''
    value: str = ''


@appscript
@dataclass_json
@dataclass
class TextParagraph:
    text: str = ''


@appscript
@dataclass_json
@dataclass
class TimePicker:
    field_name: str = ''
    hours: int = 0   # 0-23
    minutes: int = 0  # 0-59
    on_change_action: Action = None
    title: str = ''


@appscript
@dataclass_json
@dataclass
class UniversalActionResponse:
    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
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
@dataclass_json
@dataclass
class UpdateDraftActionResponse:
    def printJson(self):
        """Prints the JSON representation of this object."""
        print(self.to_json())


@appscript
@dataclass_json
@dataclass
class UpdateDraftBccRecipientsAction:
    update_bcc_recipients: list[str] = None


@appscript
@dataclass_json
@dataclass
class UpdateDraftBodyAction:
    update_content: list[str, ContentType] = None
    update_type: UpdateDraftBodyType = None


@appscript
@dataclass_json
@dataclass
class UpdateDraftCcRecipientsAction:
    update_cc_recipients: list[str] = None


@appscript
@dataclass_json
@dataclass
class UpdateDraftSubjectAction:
    update_subject: list[str] = None


@appscript
@dataclass_json
@dataclass
class UpdateDraftToRecipientsAction:
    update_to_recipients: list[str] = None


@appscript
@dataclass_json
@dataclass
class UpdateDraftActionResponseBuilder:
    update_draft_bcc_recipients_action: UpdateDraftBccRecipientsAction = None
    update_draft_body_action: UpdateDraftBodyAction = None
    update_draft_cc_recipients_action: UpdateDraftCcRecipientsAction = None
    update_draft_subject_action: UpdateDraftSubjectAction = None
    update_draft_to_recipients_action: UpdateDraftToRecipientsAction = None

    def build(self):
        """Builds the current universal action response and validates it."""
        return UpdateDraftActionResponse()



# Not completed classes
# ComposeActionResponseBuilder
# missing classes
