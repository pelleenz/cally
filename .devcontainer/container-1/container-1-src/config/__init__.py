import os

environ = {}
environ['ical_file_path'] = os.environ['ICS_PATH']
environ['caldav_url'] = os.environ['CALDAV_URL']
environ['username'] = os.environ['CALDAV_USER']
environ['password'] = os.environ['CALDAV_PASS']
environ['target_cal'] = os.environ['CALDAV_CALENDAR']
environ['prefix'] = os.environ['CALDAV_PREFIX']