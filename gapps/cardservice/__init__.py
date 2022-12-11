
from .constants import (BorderType, ComposedEmailType, ContentType,
                        DisplayStyle, GridItemLayout, HorizontalAlignment,
                        Icon, ImageCropType, ImageStyle, LoadIndicator,
                        OnClose, OpenAs, SelectionInputType, SwitchControlType,
                        TextButtonStyle, UpdateDraftBodyType)
from .api import (IconImage, Action, OpenLink, Switch, DecoratedText,
                  CardSection, ActionResponseBuilder, Attachment,
                  AuthorizationAction, AuthorizationException, BorderStyle,
                  ButtonSet, CalendarEventActionResponseBuilder, CardAction,
                  CardBuilder, CardHeader, ComposeActionResponseBuilder,
                  DatePicker, DateTimePicker, Divider, FixedFooter, Grid,
                  DriveItemsSelectedActionResponseBuilder, GridItem, Image,
                  EditorFileScopeActionResponseBuilder, ImageButton,
                  ImageComponent, ImageCropStyle, Navigation,
                  Notification, SelectionInput, Suggestions, TextButton,
                  SuggestionsResponseBuilder, TextInput, TextParagraph,
                  TimePicker, UniversalActionResponseBuilder,
                  UpdateDraftActionResponseBuilder, UpdateDraftSubjectAction,
                  UpdateDraftBccRecipientsAction, UpdateDraftBodyAction,
                  UpdateDraftToRecipientsAction, UpdateDraftCcRecipientsAction)


__all__ = ['BorderType', 'ComposedEmailType', 'ContentType', 'DisplayStyle',
           'GridItemLayout', 'HorizontalAlignment', 'Icon', 'ImageCropType',
           'ImageStyle', 'LoadIndicator', 'OnClose', 'OpenAs',
           'SelectionInputType', 'SwitchControlType', 'TextButtonStyle',
           'UpdateDraftBodyType']


def newAction():
    """Create a new Action."""
    return Action()


def newActionResponseBuilder():
    """Create a new ActionResponseBuilder."""
    return ActionResponseBuilder()


def newAttachment():
    """Create a new Attachment."""
    return Attachment()


def newAuthorizationAction():
    """Create a new AuthorizationAction."""
    return AuthorizationAction()


def newAuthorizationException():
    """Create a new AuthorizationException."""
    return AuthorizationException()


def newBorderStyle():
    """Create a new BorderStyle."""
    return BorderStyle()


def newButtonSet():
    """Create a new ButtonSet."""
    return ButtonSet()


def newCalendarEventActionResponseBuilder():
    """Create a new CalendarEventActionResponseBuilder."""
    return CalendarEventActionResponseBuilder()


def newCardAction():
    """Create a new CardAction."""
    return CardAction()


def newCardBuilder():
    """Create a new CardBuilder."""
    return CardBuilder()


def newCardHeader():
    """Create a new CardHeader."""
    return CardHeader()


def newCardSection():
    """Create a new CardSection."""
    return CardSection()


def newComposeActionResponseBuilder():
    """Create a new ComposeActionResponseBuilder."""
    return ComposeActionResponseBuilder()


def newDatePicker():
    """Create a new DatePicker."""
    return DatePicker()


def newDateTimePicker():
    """Create a new DateTimePicker."""
    return DateTimePicker()


def newDecoratedText():
    """Create a new DecoratedText."""
    return DecoratedText()


def newDivider():
    """Create a new Divider."""
    return Divider()


def newDriveItemsSelectedActionResponseBuilder():
    """Create a new DriveItemsSelectedActionResponseBuilder."""
    return DriveItemsSelectedActionResponseBuilder()


def newEditorFileScopeActionResponseBuilder():
    """Create a new EditorFileScopeActionResponseBuilder."""
    return EditorFileScopeActionResponseBuilder()


def newFixedFooter():
    """Create a new FixedFooter."""
    return FixedFooter()


def newGrid():
    """Create a new Grid."""
    return Grid()


def newGridItem():
    """Create a new GridItem."""
    return GridItem()


def newIconImage():
    """Create a new IconImage."""
    return IconImage()


def newImage():
    """Create a new Image."""
    return Image()


def newImageButton():
    """Create a new ImageButton."""
    return ImageButton()


def newImageComponent():
    """Create a new ImageComponent."""
    return ImageComponent()


def newImageCropStyle():
    """Create a new ImageCropStyle."""
    return ImageCropStyle()


def newNavigation():
    """Create a new Navigation."""
    return Navigation()


def newNotification():
    """Create a new Notification."""
    return Notification()


def newOpenLink():
    """Create a new OpenLink."""
    return OpenLink()


def newSelectionInput():
    """Create a new SelectionInput."""
    return SelectionInput()


def newSuggestions():
    """Create a new Suggestions."""
    return Suggestions()


def newSuggestionsResponseBuilder():
    """Create a new SuggestionsResponseBuilder."""
    return SuggestionsResponseBuilder()


def newSwitch():
    """Create a new Switch."""
    return Switch()


def newTextButton():
    """Create a new TextButton."""
    return TextButton()


def newTextInput():
    """Create a new TextInput."""
    return TextInput()


def newTextParagraph():
    """Create a new TextParagraph."""
    return TextParagraph()


def newTimePicker():
    """Create a new TimePicker."""
    return TimePicker()


def newUniversalActionResponseBuilder():
    """Create a new UniversalActionResponseBuilder."""
    return UniversalActionResponseBuilder()


def newUpdateDraftActionResponseBuilder():
    """Create a new UpdateDraftActionResponseBuilder."""
    return UpdateDraftActionResponseBuilder()


def newUpdateDraftBccRecipientsAction():
    """Create a new UpdateDraftBccRecipientsAction"""
    return UpdateDraftBccRecipientsAction()


def newUpdateDraftBodyAction():
    """Create a new UpdateDraftBodyAction."""
    return UpdateDraftBodyAction()


def newUpdateDraftCcRecipientsAction():
    """Create a new UpdateDraftCcRecipientsAction."""
    return UpdateDraftCcRecipientsAction()


def newUpdateDraftSubjectAction():
    """Create a new UpdateDraftSubjectAction."""
    return UpdateDraftSubjectAction()


def newUpdateDraftToRecipientsAction():
    """Create a new UpdateDraftToRecipientsAction."""
    return UpdateDraftToRecipientsAction()
