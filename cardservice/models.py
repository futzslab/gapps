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


# class CalendarEvent(BaseModel):

class GEvent(BaseModel):
    commonEventObject: CommonEvent
    authorizationEventObject: AuthorizationEvent
    drive: DriveEvent = None
    docs: EditorEvent = None
    sheets: EditorEvent = None
    slides: EditorEvent = None
    gmail: GmailEvent = None
    # calendar: CalendarEvent = None
