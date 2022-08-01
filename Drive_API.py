import calendar
import copy
import datetime

from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


def connection():
    CREDENTIALS_FILE = 'JSON/credentials.json'  # имя файла с закрытым ключом
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    service = discovery.build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = ''  # ID таблицы
    include_grid_data = True
    return service, spreadsheet_id, include_grid_data


def Color_of_Greed(ranges):
    service, spreadsheet_id, include_grid_data = connection()
    request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=include_grid_data)
    response = request.execute()
    res = response.get("sheets")
    res = res[0].get("data")
    res = res[0].get("rowData")
    mass = []
    for i in range(len(res)):
        for key in res[i]:
            if key == 'values':
                s = res[i][key]
                s = s[0]["userEnteredFormat"]
                s = s["backgroundColor"]
                s = s.values()
                s = list(s)
                count = 0
                for j in range(len(s)):
                    count += s[j]
                if count == 3:
                    mass.append(True)
                else:
                    mass.append(False)
    return mass


def Check_Date(data):
    service, spreadsheet_id, include_grid_data = connection()
    sheet_metadata = service.spreadsheets()
    sheet_metadata_get = sheet_metadata.get(spreadsheetId=spreadsheet_id).execute()
    sheets = sheet_metadata_get.get('sheets', '')
    title = []
    for i in range(len(sheets)):
        title.append(sheets[i].get("properties", {}).get("title"))
    # sheet_id = sheets[0].get("properties", {}).get("sheetId", 0)
    for i in range(len(title)):
        result = sheet_metadata.values().get(spreadsheetId=spreadsheet_id, range=title[i]).execute()
        result = result.get('values')
        for j in range(1, len(result[0]), 2):
            if data == result[0][j]:
                if i != 0 and j == 1:
                    return title[i], result[1][j], True
                elif i == 0 and j == 1:
                    return title[i], result[1][j], title[len(title)-1], True
                else:
                    return title[i], result[1][j], False


def updateDate():
    date = str(datetime.datetime.today().date())
    date_list = date[5:].split('-')
    actual_date = date_list[1] + '.' + date_list[0]
    check = copy.deepcopy(Check_Date('16.02'))
    if check[-1]:
        if len(check) > 3:
            title = check[2]
        else:
            title = check[0][:-1] + str(int(check[0][-1]) - 1)
        service, spreadsheet_id = connection()[:-1]
        cell_format = {
            "backgroundColor": {"red": 1, "green": 1, "blue": 1}
        }
        cells_range = {
            "startRowIndex": 3,
            "endRowIndex": 35,
            "startColumnIndex": 1,
            "endColumnIndex": 15,
        }
        body = {
            "requests": [
                {
                    "repeatCell": {
                        "range": cells_range,
                        "cell": {"userEnteredFormat": cell_format},
                        "fields": "userEnteredFormat.backgroundColor"
                    }
                }
            ]
        }

        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

        cal = calendar.monthrange(int(str(datetime.datetime.today().date())[:4]), int(date_list[0]))

        range_date = []
        count = 1
        k = 1
        for i in range(1, 15):
            if i % 2 == 0:
                if (count+6) + int(date_list[1]) > cal[1]:
                    month = date_list[0][-1]
                    if int(month) + 1 > 12:
                        k = ((count+6) + int(date_list[1])) - cal[1]
                        print(k)
                        month = '00'
                        range_date.append(str(k) + '.' + (date_list[0][:-1] + str(int(month) + 1)) + '.' +
                                          date[:3] + str(int(date[3:4])+1))
                    else:
                        range_date.append(str(k) + '.' + (date_list[0][:-1] + str(int(month) + 1)))
                else:
                    range_date.append(str(int(date_list[1]) + (count+6)) + '.' + date_list[0])
                count += 1
            else:
                range_date.append('')


        service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=title + '!A1',
                                               valueInputOption="USER_ENTERED", body={"values": [range_date]}).execute()
        return 'Successfully update!'
    return 'No update'
#print(updateDate())
# print(Check_Date('25.02'))