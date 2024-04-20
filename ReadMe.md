# Cally - Your Personal CalDAV Assistant
Cally is a little Docker Container written in Python based in a DevContainer

## Features
Cally grabs a file from a iCal Server
Reads the iCal File and every Event
appends a prefix to the name of every event
compares every event with the events in the specified CalDAV Calendar
if the event does not allready exists, Cally will push the event to the CalDaV Calendar
