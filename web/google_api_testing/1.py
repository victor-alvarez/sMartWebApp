from datetime import datetime, timedelta
# this helps us build service object from any google api 
from apiclient.discovery import build
#setting up the consent using InstalledAppView right now for testing, but we will need to potentially set a seperate url content page for the users to give permsision 
from google_auth_oauthlib.flow import InstalledAppFlow
#providing read/write accesss the calendar of the user 
scopes = ['https://www.googleapis.com/auth/calendar']
#flow = InstalledAppFlow.from_client_secrets_file("client_secret_2.json", scopes=scopes)
#flow.run_console()
#now we need to save our credentials so that we dont have to run the flow over again 
import pickle
#credentials = flow.run_console()
#pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open(r"C:\Users\Kanav\Desktop\sMartWebApp\web\google_api_testing\token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
# my primary calendar
print(result['items'][0])

#Getting all the calendar events

calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()
print(result["items"][0])

#create a new calendar event
start_time = datetime(2020, 9, 2, 19, 00, 0)
end_time = start_time + timedelta(hours=1)
timezone = 'Asia/Kolkata'
event = {
  'summary': 'Meeting with Mentor Ali',
  'location': 'Ludhiana',
  'description': 'mentoring session',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute()