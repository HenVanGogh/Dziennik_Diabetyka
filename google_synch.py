from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google.auth.transport.requests
from googleapiclient import discovery
from apiclient import errors
from apiclient.http import MediaFileUpload
import sys
import datetime
import csv

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '14ESR9it8oqTc3dytP9tHoYMUpzbY0YKl8kUsghV24xg'

scope_permission = "https://www.googleapis.com/auth/drive.file"

SAMPLE_SPREADSHEET_ID = ""

def main():
    first_time_user = True

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            first_time_user = False
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    if(first_time_user):
        title = "dziennik diabetyka"
        file1 = open("file_name.txt", "w")
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                    fields='spreadsheetId').execute()
        print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
        SAMPLE_SPREADSHEET_ID = spreadsheet.get('spreadsheetId')
        file1.write(spreadsheet.get('spreadsheetId'))
        file1.close()
    else:
        file1 = open("file_name.txt", "r")
        SAMPLE_SPREADSHEET_ID = file1.read()
        file1.close()

    sheet = service.spreadsheets()

    placeholder = 0
    placeholder_1 = 0
    try:
        placeholder = sys.argv[1]
    except IndexError:
        pass

    try:
        placeholder_1 = sys.argv[2]
    except IndexError:
        pass

    if(placeholder == "r"):
        i = 1
        pointer = 0
        while (pointer != []):
            pointer = read_data(sheet, SAMPLE_SPREADSHEET_ID, "A" + str(i))
            i += 1
        data = read_data(sheet, SAMPLE_SPREADSHEET_ID, "A1:D" + str(i))
        print(data)
        try:
            os.remove('dziennik.csv')
        except OSError:
            pass
        with open('dziennik.csv' , mode='w',newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for i in data:
                writer.writerow(i)

    if(placeholder == "w"):
        current_time = datetime.datetime.now()
        i = 1
        pointer = 0
        while(pointer != []):
            pointer = read_data(sheet, SAMPLE_SPREADSHEET_ID, "A" + str(i))
            i += 1
        i -= 1
        values = [[current_time.year]]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range="A" + str(i),
            valueInputOption="RAW", body=body).execute()
        values = [[current_time.month]]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range="B" + str(i),
            valueInputOption="RAW", body=body).execute()
        values = [[current_time.day]]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range="C" + str(i),
            valueInputOption="RAW", body=body).execute()
        values = [[placeholder_1]]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range="D" + str(i),
            valueInputOption="RAW", body=body).execute()

def read_data(sheet ,SAMPLE_SPREADSHEET_ID, range_r):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_r).execute()
    return result.get('values', [])

if __name__ == '__main__':
    main()