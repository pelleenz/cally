import caldav
import time
from icalendar import Event
from datetime import datetime
from icalevents.icalevents import events as ical_event
import pytz

ical_file_path = "https://calendar.google.com/calendar/ical/pelleenz1999%40gmail.com/private-808f6e43ef80428f34e72d456a630606/basic.ics"
caldav_url = "http://192.168.178.151:9100/remote.php/dav/principals/users/test"
username = "test"
password = "i6CeL-Cndj6-5ksed-wP9D8-DmYGH"
target_cal = "casdfasd"
prefix = "THW// "


def main():
  while True:
    ical_events = ical_loader(ical_file_path)
    client = caldav_conn(caldav_url, username, password)
    calendar = cal_finder(client)
    caldav_parser(ical_events, calendar)
    time.sleep(60)


def caldav_conn(caldav_url, username, password):
  client = caldav.DAVClient(url=caldav_url, username=username, password=password)
  return client

def ical_loader(ical_file_path):
  ical_events = ical_event(ical_file_path)
  return ical_events

def caldav_parser(ical_events, calendar):
  for event in ical_events:
        event_summary = str(prefix + event.summary)
        event_start = event.start
        event_end = event.end
        
        duplicate = duplicate_check(calendar, event_summary, event_start, event_end)
        
        if duplicate is False:        
          calendar.add_event(summary=event_summary, dtstart=event_start, dtend=event_end)
          print(f"Event {event_summary} added to Calendar")
        
        print(f"Duplicate found, Event {event_summary} not added")
        
def cal_finder(client):
  principal = client.principal()
  calendars = principal.calendars()
  for calendar in calendars:
    if str(calendar) != target_cal:
      raise Exception("Calender not found on the server.")
    return calendar

def duplicate_check (calendar, event_summary, event_start, event_end):
  events_in_range = calendar.events()
  
  for event in events_in_range:
    event_data = event.data

    res = [] 
    for sub in event_data.split('\n'): 
      if ':' in sub: 
        res.append(map(str.strip, sub.split(':', 1))) 
    res = dict(res)
    print(event_summary)
    print(res.get('SUMMARY'))
    print("___")
    print(convert_datetime_format(event_start))
    print(res.get('DTSTART;TZID=CEST;VALUE=DATE-TIME'))
   
    if (event_summary == res.get('SUMMARY')) and \
           (convert_datetime_format(event_start) == res.get('DTSTART;TZID=CEST;VALUE=DATE-TIME')) and \
           (convert_datetime_format(event_end) == res.get('DTEND;TZID=CEST;VALUE=DATE-TIME')):
            return True  # Ein Duplikat wurde gefunden
    
  return False  # Kein Duplikat gefunden
  
def convert_datetime_format(input_datetime_str):
    # Parse the input datetime string
    input_format = "%Y-%m-%d %H:%M:%S%z"
    dt = datetime.strptime(str(input_datetime_str), input_format)

    # Convert the datetime to a different format
    output_format = "%Y%m%dT%H%M%S"
    output_datetime_str = dt.strftime(output_format)

    return output_datetime_str

if __name__ == "__main__":
  main()