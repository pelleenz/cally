import caldav
import os
from datetime import datetime
from icalevents.icalevents import events as ical_event
import logging
import asyncio

async def backend():
  print("backend started")

  environ = {}
  environ['ical_file_path'] = os.environ['ICS_PATH']
  environ['caldav_url'] = os.environ['CALDAV_URL']
  environ['username'] = os.environ['CALDAV_USER']
  environ['password'] = os.environ['CALDAV_PASS']
  environ['target_cal'] = os.environ['CALDAV_CALENDAR']
  environ['prefix'] = os.environ['CALDAV_PREFIX']

  
  while True:
    caldav_parser(ical_loader(environ), cal_finder(caldav_conn(environ), environ), environ)
    print("backend")
    await asyncio.sleep(10)

def caldav_conn(environ):
  client =  caldav.DAVClient(url=environ['caldav_url'], username=environ['username'], password=environ['password'])
  logging.info("Connection to CalDAV Server established")
  return client

def ical_loader(environ):
  ical_events = ical_event(url=environ['ical_file_path'])
  return ical_events

def caldav_parser(ical_events, calendar, environ):
  
  for event in ical_events:
    event_summary = str(environ['prefix'] + event.summary)
    event_start = event.start
    event_end = event.end
    event_uid = event.uid
    print(event_uid)
    duplicate = duplicate_check(calendar, event_uid)
    
    if duplicate is False:
      calendar.add_event(summary=event_summary, dtstart=event_start, dtend=event_end, uid=event_uid)
      logging.info(f"Event {event_summary} added to Calendar")
    else:
      logging.info(f"Duplicate found, Event {event_summary} not added")
        
def cal_finder(client, environ):
  principal = client.principal()
  calendars = principal.calendars()
  for calendar in calendars:
    if str(calendar) == environ['target_cal']:
      return calendar
    
  logging.error(f"Calendar {str(calendar)} not found")
  raise Exception("Calender not found on the server.")

def duplicate_check(calendar, event_uid):
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
    print(event_uid)
    if (event_uid == res.get('UID')):
      return True
  return False
  
def convert_datetime_format(input_datetime_str):
    input_format = "%Y-%m-%d %H:%M:%S%z"
    dt = datetime.strptime(str(input_datetime_str), input_format)

    output_format = "%Y%m%dT%H%M%S"
    output_datetime_str = dt.strftime(output_format)

    return output_datetime_str
 
async def main():
  t1 = asyncio.create_task(backend())
  await asyncio.gather(t1)
    
if __name__ == "__main__":
  asyncio.run(main())