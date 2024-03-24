import caldav

CALDAV_URL = "http://192.168.178.151:9100/remote.php/dav/principals/users/test"
USERNAME = "test"
PASSWORD = "i6CeL-Cndj6-5ksed-wP9D8-DmYGH"

def get_events():
  client = caldav.DAVClient(CALDAV_URL, username=USERNAME, password=PASSWORD)
  principal = client.principal()
  for calendar in principal.calendars():
    print(calendar)
    for event in calendar.events():
        print(event)