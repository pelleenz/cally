import caldav
from caldav import Calendar
from datetime import datetime
from icalevents.icalevents import events

CALDAV_URL = "http://192.168.178.151:9100/remote.php/dav/principals/users/test"
USERNAME = "test"
PASSWORD = "i6CeL-Cndj6-5ksed-wP9D8-DmYGH"

def get_calendar_url():
  with caldav.DAVClient(CALDAV_URL, username=USERNAME, password=PASSWORD) as client:
    for calendar in client.principal().calendars():
      if calendar.name == "abscs":
        print("right")
        push_events()
      else: 
        get_events()


def get_events():
  client = caldav.DAVClient(CALDAV_URL, username=USERNAME, password=PASSWORD)
  principal = client.principal()
  for calendar in principal.calendars():
    print(calendar)
    for event in calendar.events():
        print(event.data)
        
def push_events():
  with caldav.DAVClient(CALDAV_URL, username=USERNAME, password=PASSWORD) as client:
     
    calendar = client.calendar(url = "http://192.168.178.151:9100/remote.php/dav/calendars/test/test/")
    event = calendar.save_event(
    dtstart=datetime(2024, 5, 17, 6, 13),
    dtend=datetime(2024, 5, 18, 18, 32),
    summary="Do the task",
    rrule={"FREQ": "YEARLY"},
    )
    
    print(event)
    
def ical_get_events():
  es = events()
  
  for event in es:
    print(event)