import caldav
import time
from icalendar import Event
from datetime import datetime
from icalevents.icalevents import events as ical_event
import configparser
import logging
import sys

def main():
  logging.basicConfig(stream=sys.stdout, level=logging.INFO)
  logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
  config = config_parser({})
  while True:
    ical_events = ical_loader(config["ical_file_path"])
    client = caldav_conn(config["caldav_url"], config["username"], config["password"])
    calendar = cal_finder(client, config)
    caldav_parser(ical_events, calendar, config)
    time.sleep(60)

def config_parser(args, path = "./"):
  try:
      parse = configparser.RawConfigParser()
      if path[-4:] == ".ini":
        parse.read(path)
      elif path[-1] == "/":
        parse.read(path + "cally.ini")
      else:
        parse.read(path + "/cally.ini")
  except:
    e = "Config file could not be read"
    logging.error(e)
    raise(e)
      
  args['ical_file_path'] = parse.get("Main", 'ical_file_path')
  args['caldav_url'] = parse.get("Main", 'caldav_url')
  args['username'] = parse.get("Main", 'username')
  args['password'] = parse.get("Main", 'password')
  args['target_cal'] = parse.get("Main", 'target_cal')
  args['prefix'] = parse.get("Main", 'prefix')
    
  return(args)

def caldav_conn(caldav_url, username, password):
  client = caldav.DAVClient(url=caldav_url, username=username, password=password)
  logging.info("Connection to CalDAV Server established")
  return client

def ical_loader(ical_file_path):
  ical_events = ical_event(ical_file_path)
  return ical_events

def caldav_parser(ical_events, calendar, config):
  for event in ical_events:
        event_summary = str(config["prefix"] + " " + event.summary)
        event_start = event.start
        event_end = event.end
        
        duplicate = duplicate_check(calendar, event_summary, event_start, event_end)
        
        if duplicate is False:        
          calendar.add_event(summary=event_summary, dtstart=event_start, dtend=event_end)
          logging.info(f"Event {event_summary} added to Calendar")
        
        logging.info(f"Duplicate found, Event {event_summary} not added")
        
def cal_finder(client, config):
  principal = client.principal()
  calendars = principal.calendars()
  for calendar in calendars:
    if str(calendar) == config["target_cal"]:
      return calendar
    
  logging.error(f"Calendar {str(calendar)} not found")
  raise Exception("Calender not found on the server.")

def duplicate_check (calendar, event_summary, event_start, event_end):
  events_in_range = calendar.events()
  
  for event in events_in_range:
    event_data = event.data

    res = [] 
    for sub in event_data.split('\n'): 
      if ':' in sub: 
        res.append(map(str.strip, sub.split(':', 1))) 
    res = dict(res)
   
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