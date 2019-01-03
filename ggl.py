from __future__ import print_function
import calendar
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def availibility( events, start, end ):
    DAY_START = datetime.time( hour = 8 )
    DAY_END = datetime.time( hour = 20 )

    availibility = {}

    between = end - start

    for day in range(0, between.days):
        availibility[ start + datetime.timedelta(days=day) ] = {}

    for event in events:
        
        
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def process_date( date_str ):
    data = [ int( item ) for item in date_str.split("-") ]
    return datetime.date( data[0], data[1], data[2] )

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    start_str = "2019-01-01"
    end_str = "2019-01-04"
#    start_str = input("Enter start date['2019-01-01']: ")
#    end_str = input("Enter end date['2019-01-04']: ")
        
    start = process_date( start_str )
    end = process_date( end_str )
    availibility( events, start, end )

if __name__ == '__main__':
    main()
