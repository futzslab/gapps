import json

from gapps.cardservice.models import (TimeZone, CommonEvent,
                                      AuthorizationEvent, DriveItem,
                                      DriveEvent, EditorEvent,
                                      GmailEvent, Organizer, Capabilities,
                                      Attendee, ConferenceSolution, EntryPoint,
                                      ConferenceData, CalendarEvent, GEvent)


def test_missing_time_zone_model():
    f_json = '''
    {
  "commonEventObject": {
    "userLocale": "fr",
    "hostApp": "GMAIL",
    "platform": "WEB",
    "timeZone": {
      "id": "Africa/Abidjan"
    },
    "parameters": {
      "text": "Good afternoon GMAIL",
      "is_homepage": "True"
    }
  },
  "gmail": {
    "accessToken": "random_access_token"
  },
  "authorizationEventObject": {
    "userOAuthToken": "random_user_oauth_token",
    "userIdToken": "random_user_id_token",
    "systemIdToken": "random_system_id_token"
  }
}
'''
    data = json.loads(f_json)
    ev = GEvent(**data)
    assert ev.commonEventObject.timeZone.id == "Africa/Abidjan"
    assert ev.commonEventObject.timeZone.offset is None
    assert ev.commonEventObject.timeZone is not None
    assert ev.commonEventObject.userLocale == "fr"
    assert ev.commonEventObject.hostApp == "GMAIL"
    assert ev.commonEventObject.platform == "WEB"
    assert ev.commonEventObject.parameters == {"text": "Good afternoon GMAIL",
                                               "is_homepage": "True"}
    assert ev.gmail.accessToken == "random_access_token"
    assert ev.authorizationEventObject.userOAuthToken == "random_user_oauth_token"  # noqa
    assert ev.authorizationEventObject.userIdToken == "random_user_id_token"
    assert ev.authorizationEventObject.systemIdToken == "random_system_id_token"  # noqa


def test_time_zone_model():
    time_zone = TimeZone(id="1", offset=2)
    assert time_zone.id == "1"
    assert time_zone.offset == 2


def test_common_event_model():
    common_event = CommonEvent(userLocale="en_US", hostApp="Gmail",
                               platform="Web")
    assert common_event.userLocale == "en_US"
    assert common_event.hostApp == "Gmail"
    assert common_event.platform == "Web"


def test_authorization_event_model():
    authorization_event = AuthorizationEvent(userOAuthToken="token1",
                                             systemIdToken="token2",
                                             userIdToken="token3")
    assert authorization_event.userOAuthToken == "token1"
    assert authorization_event.systemIdToken == "token2"
    assert authorization_event.userIdToken == "token3"


def test_drive_item_model():
    drive_item = DriveItem(id="1", iconUrl="https://example.com/icon",
                           mimeType="image/png", title="My File")
    assert drive_item.id == "1"
    assert drive_item.iconUrl == "https://example.com/icon"
    assert drive_item.mimeType == "image/png"
    assert drive_item.title == "My File"


def test_drive_event_model():
    drive_event = DriveEvent(selectedItems=[DriveItem(id="1"),
                                            DriveItem(id="2")],
                             activeCursorItem=DriveItem(id="3"))
    assert len(drive_event.selectedItems) == 2
    assert drive_event.selectedItems[0].id == "1"
    assert drive_event.selectedItems[1].id == "2"
    assert drive_event.activeCursorItem.id == "3"


def test_editor_event_model():
    editor_event = EditorEvent(id="1", title="My Document")
    assert editor_event.id == "1"
    assert editor_event.title == "My Document"


def test_gmail_event_model():
    gmail_event = GmailEvent(messageId="1", threadId="2", accessToken="token",
                             toRecipients=["user1@example.com"],
                             ccRecipients=["user2@example.com"],
                             bccRecipients=["user3@example.com"])
    assert gmail_event.messageId == "1"
    assert gmail_event.threadId == "2"
    assert gmail_event.accessToken == "token"
    assert len(gmail_event.toRecipients) == 1
    assert gmail_event.toRecipients[0] == "user1@example.com"
    assert len(gmail_event.ccRecipients) == 1
    assert gmail_event.ccRecipients[0] == "user2@example.com"
    assert len(gmail_event.bccRecipients) == 1
    assert gmail_event.bccRecipients[0] == "user3@example.com"


def test_organizer_model():
    organizer = Organizer(email="organizer@example.com")
    assert organizer.email == "organizer@example.com"


def test_capabilities_model():
    capabilities = Capabilities(canSeeAttendees=True, canAddAttendees=False,
                                canSeeConferenceData=True,
                                canSetConferenceData=False)
    assert capabilities.canSeeAttendees is True
    assert capabilities.canAddAttendees is False
    assert capabilities.canSeeConferenceData is True
    assert capabilities.canSetConferenceData is False


def test_attendee_model():
    attendee = Attendee(email="attendee@example.com", optional=True,
                        displayName="Attendee", organizer=False,
                        resource=False, responseStatus="accepted",
                        comment="No comment", additionalGuests=2)
    assert attendee.email == "attendee@example.com"
    assert attendee.optional is True
    assert attendee.displayName == "Attendee"
    assert attendee.organizer is False
    assert attendee.resource is False
    assert attendee.responseStatus == "accepted"
    assert attendee.comment == "No comment"
    assert attendee.additionalGuests == 2


def test_conference_solution_model():
    conference_solution = ConferenceSolution(
        iconUri="https://example.com/icon", key={"key": "value"},
        name="Conference Solution")
    assert conference_solution.iconUri == "https://example.com/icon"
    assert conference_solution.key == {"key": "value"}
    assert conference_solution.name == "Conference Solution"


def test_entry_point_model():
    entry_point = EntryPoint(accessCode="1234",
                             entryPointFeatures=["feature1", "feature2"],
                             entryPointType="type", label="Entry Point",
                             meetingCode="5678", passcode="pass",
                             password="password", pin="123456",
                             regionCode="US", uri="https://example.com")
    assert entry_point.accessCode == "1234"
    assert len(entry_point.entryPointFeatures) == 2
    assert entry_point.entryPointFeatures[0] == "feature1"
    assert entry_point.entryPointFeatures[1] == "feature2"
    assert entry_point.entryPointType == "type"
    assert entry_point.label == "Entry Point"
    assert entry_point.meetingCode == "5678"
    assert entry_point.passcode == "pass"
    assert entry_point.password == "password"
    assert entry_point.pin == "123456"
    assert entry_point.regionCode == "US"
    assert entry_point.uri == "https://example.com"


def test_conference_data_model():
    conference_data = ConferenceData(conferenceId="1234",
                                     conferenceSolution=ConferenceSolution(),
                                     entryPoints=[EntryPoint()],
                                     notes="Conference Notes",
                                     parameters={"param": "value"})
    assert conference_data.conferenceId == "1234"
    assert isinstance(conference_data.conferenceSolution, ConferenceSolution)
    assert len(conference_data.entryPoints) == 1
    assert isinstance(conference_data.entryPoints[0], EntryPoint)
    assert conference_data.notes == "Conference Notes"
    assert conference_data.parameters == {"param": "value"}


def test_calendar_event_model():
    calendar_event = CalendarEvent(id="1", recurringEventId="2",
                                   calendarId="3", organizer=Organizer(),
                                   attendees=[Attendee()],
                                   conferenceData=ConferenceData(),
                                   capabilities=Capabilities())
    assert calendar_event.id == "1"
    assert calendar_event.recurringEventId == "2"
    assert calendar_event.calendarId == "3"
    assert isinstance(calendar_event.organizer, Organizer)
    assert len(calendar_event.attendees) == 1
    assert isinstance(calendar_event.attendees[0], Attendee)
    assert isinstance(calendar_event.conferenceData, ConferenceData)
    assert isinstance(calendar_event.capabilities, Capabilities)


def test_gevent_model():
    common_event = CommonEvent(userLocale="en_US", hostApp="Gmail",
                               platform="Web")
    authorization_event = AuthorizationEvent(userOAuthToken="token1",
                                             systemIdToken="token2",
                                             userIdToken="token3")
    drive_event = DriveEvent(selectedItems=[DriveItem(id="1"),
                                            DriveItem(id="2")],
                             activeCursorItem=DriveItem(id="3"))
    docs_event = EditorEvent(id="1", title="My Document")
    sheets_event = EditorEvent(id="2", title="My Spreadsheet")
    slides_event = EditorEvent(id="3", title="My Presentation")
    gmail_event = GmailEvent(messageId="1", threadId="2", accessToken="token",
                             toRecipients=["user1@example.com"],
                             ccRecipients=["user2@example.com"],
                             bccRecipients=["user3@example.com"])
    calendar_event = CalendarEvent(id="4", recurringEventId="5",
                                   calendarId="6", organizer=Organizer(),
                                   attendees=[Attendee()],
                                   conferenceData=ConferenceData(),
                                   capabilities=Capabilities())
    gevent = GEvent(commonEventObject=common_event,
                    authorizationEventObject=authorization_event,
                    drive=drive_event, docs=docs_event, sheets=sheets_event,
                    slides=slides_event, gmail=gmail_event,
                    calendar=calendar_event)
    assert isinstance(gevent.commonEventObject, CommonEvent)
    assert isinstance(gevent.authorizationEventObject, AuthorizationEvent)
    assert isinstance(gevent.drive, DriveEvent)
    assert isinstance(gevent.docs, EditorEvent)
    assert isinstance(gevent.sheets, EditorEvent)
    assert isinstance(gevent.slides, EditorEvent)
    assert isinstance(gevent.gmail, GmailEvent)
    assert isinstance(gevent.calendar, CalendarEvent)
