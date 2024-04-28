from frontend import create_app
from flask import render_template
import config
import caldav

def frontend():
   
  app = create_app()
  
  @app.route('/')
  def home():
    principal = config.client.principal()
    calendars = principal.calendars()
    for calendar in calendars: 
      if str(calendar) == config.environ['target_cal']:
        events = calendar.events()
        return render_template("home.html", principal=principal, calendar=calendar, events=events)

  app.run(debug=True)
