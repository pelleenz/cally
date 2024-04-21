import caldav
import time
from datetime import datetime
from icalevents.icalevents import events as ical_event
import os
import logging
import sys

def main():
  logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
  logging.basicConfig(
    stream=sys.stderr,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.ERROR,
    datefmt='%Y-%m-%d %H:%M:%S')
  
  ical_file_path = os.environ['ICS_PATH']
  caldav_url = os.environ['CALDAV_URL']
  username = os.environ['CALDAV_USER']
  password = os.environ['CALDAV_PASS']
  target_cal = os.environ['CALDAV_CALENDAR']
  prefix = os.environ['CALDAV_PREFIX']
  while True:
    ical_events = ical_loader(ical_file_path)
    client = caldav_conn(caldav_url, username, password)
    calendar = cal_finder(client, target_cal)
    caldav_parser(ical_events, calendar, prefix)
    time.sleep(60)

def caldav_conn(caldav_url, username, password):
  client = caldav.DAVClient(url=caldav_url, username=username, password=password)
  logging.info("Connection to CalDAV Server established")
  return client

def ical_loader(ical_file_path):
  ical_events = ical_event(ical_file_path)
  return ical_events

def caldav_parser(ical_events, calendar, prefix):
  for event in ical_events:
    event_summary = str(prefix + " " + event.summary)
    event_start = event.start
    event_end = event.end
    event_uid = event.uid
  
    duplicate = duplicate_check(calendar, event_summary, event_start, event_end, event_uid)
    
    if duplicate is False:        
      calendar.add_event(summary=event_summary, dtstart=event_start, dtend=event_end, uid=event_uid)
      logging.info(f"Event {event_summary} added to Calendar")
    else:
      logging.info(f"Duplicate found, Event {event_summary} not added")
        
def cal_finder(client, target_cal):
  principal = client.principal()
  calendars = principal.calendars()
  for calendar in calendars:
    if str(calendar) == target_cal:
      return calendar
    
  logging.error(f"Calendar {str(calendar)} not found")
  raise Exception("Calender not found on the server.")

def duplicate_check(calendar, event_summary, event_start, event_end, event_uid):
  events_in_range = calendar.events()
  
  if len(events_in_range) == 0:
    return False
  
  for event in events_in_range:
    event_data = event.data

    res = [] 
    for sub in event_data.split('\n'): 
      if ':' in sub: 
        res.append(map(str.strip, sub.split(':', 1))) 
    res = dict(res)
    print(res.get('UID'))
    
    if (event_uid == res.get('UID')):
      return True
    return False
  
def convert_datetime_format(input_datetime_str):
    input_format = "%Y-%m-%d %H:%M:%S%z"
    dt = datetime.strptime(str(input_datetime_str), input_format)

    output_format = "%Y%m%dT%H%M%S"
    output_datetime_str = dt.strftime(output_format)

    return output_datetime_str

if __name__ == "__main__":
  main()