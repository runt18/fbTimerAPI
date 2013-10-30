# mongoengine database module
from mongoengine import *
from datetime import datetime
import logging

# Document: {
#   person: StringField
#   totalTime: NumberLong,
#   timeZoneOffset: NumberLong,
#   sessionTime:[
#     {
#       sessionId: StringField
#       sessionStart: datetime
#       sessionEnd: datetime
#     },
#     {
#       sessionId: StringField
#       sessionStart: datetime
#       sessionEnd: datetime
#     }
#   ]
# }

class pageSession(EmbeddedDocument):
  sessionStart = LongField()
  sessionEnd = LongField()

class session(EmbeddedDocument):
  sessionTotalTime = LongField()
  pageSessions = ListField( EmbeddedDocumentField(pageSession) )

class UserDocument(Document):
  personID = StringField()
  totalTime = LongField()
  timeZoneOffset = IntField()

  # List of sessions of the user,
  userSessions = ListField( EmbeddedDocumentField(session) )

  # Timestamp will record the date and time idea was created.
  timestamp = DateTimeField(default=datetime.now())

class ShowTimer(Document):
  dataID = StringField(default='showTimer')
  showTimer = BooleanField(default=False)