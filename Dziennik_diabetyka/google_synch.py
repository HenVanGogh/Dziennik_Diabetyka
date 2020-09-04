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
from include.losowanie_zartu_z_pliku import say_a_joke
from include.dane import dodaj_wpis
from include.wykresy import graph_of_last_30_measurments, measurments_from_chosen_day_and_month_and_year,\
    measurments_from_chosen_month_and_year
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '14ESR9it8oqTc3dytP9tHoYMUpzbY0YKl8kUsghV24xg'
scope_permission = "https://www.googleapis.com/auth/drive.file"
SAMPLE_SPREADSHEET_ID = ""
def main():
    first_time_user = True
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            first_time_user = False
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
        tmp_data = []
        with open('dziennik.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for i in data:
                print(" ")
                print(i)
                is_there = 0
                for row in reader:
                    print(row)
                    if(i == row):
                        is_there = 1
                        break
                if(is_there == 0):
                    tmp_data.append(i)
        print(tmp_data)
        with open('dziennik.csv', mode='a', newline='') as csv_file:
            with open('baza.csv', mode='a', newline='') as baza_file:
                writer = csv.writer(csv_file, delimiter=',')
                baza = csv.writer(baza_file, delimiter=',')
                for i in tmp_data:
                    writer.writerow(i)
                    dodaj_wpis(int(i[3]), i[0], i[1], i[2])

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
