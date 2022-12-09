"""Module to manage fastapi models."""

from typing import List
from pydantic import BaseModel


class TimeZone(BaseModel):
    id: str
    offset: int


class CommonEvent(BaseModel):
    userLocale: str
    hostApp: str
    platform: str
    timeZone: TimeZone
    parameters: dict = {}
    formInputs: dict = {}


class AuthorizationEvent(BaseModel):
    userOAuthToken: str
    systemIdToken: str
    userIdToken: str


class DriveItem(BaseModel):
    id: str = None
    iconUrl: str = None
    mimeType: str = None
    title: str = None
    addonHasFileScopePermission: bool = False


class DriveEvent(BaseModel):
    selectedItems: List[DriveItem] = []
    activeCursorItem: DriveItem = None


class EditorEvent(BaseModel):
    """Docs, Sheets, slides """
    id: str = None
    title: str = None
    addonHasFileScopePermission: bool = False


class GmailEvent(BaseModel):
    messageId: str = None
    threadId: str = None
    accessToken: str = None
    toRecipients: List[str] = []
    ccRecipients: List[str] = []
    bccRecipients: List[str] = []


class Organizer(BaseModel):
    email: str = None


class Capabilities(BaseModel):
    canSeeAttendees: bool = None
    canAddAttendees: bool = None
    canSeeConferenceData: bool = None
    canSetConferenceData: bool = None


class Attendee(BaseModel):
    email: str = None
    optional: bool = None
    displayName: str = None
    organizer: bool = None
    # self: bool = None
    resource: bool = None
    responseStatus: str = None
    comment: str = None
    additionalGuests: int = None


class ConferenceSolution(BaseModel):
    iconUri: str = None
    key: dict = None
    name: str = None


class EntryPoint(BaseModel):
    accessCode: str = None
    entryPointFeatures: List[str] = None
    entryPointType: str = None
    label: str = None
    meetingCode: str = None
    passcode: str = None
    password: str = None
    pin: str = None
    regionCode: str = None
    uri: str = None


class ConferenceData(BaseModel):
    conferenceId: str = None
    conferenceSolution: ConferenceSolution = None
    entryPoints: List[EntryPoint] = None
    notes: str = None
    parameters: dict = None


class CalendarEvent(BaseModel):
    id: str = None   # the event id
    recurringEventId: str = None
    calendarId: str = None
    organizer: Organizer = None
    attendees: List[Attendee] = []
    conferenceData: ConferenceData = None
    capabilities: Capabilities = None


class GEvent(BaseModel):
    commonEventObject: CommonEvent
    authorizationEventObject: AuthorizationEvent
    drive: DriveEvent = None
    docs: EditorEvent = None
    sheets: EditorEvent = None
    slides: EditorEvent = None
    gmail: GmailEvent = None
    calendar: CalendarEvent = None
