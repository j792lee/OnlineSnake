import gspread
from oauth2client.service_account import ServiceAccountCredentials


def insertScore(score, name):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("High Scores Snake-7b087cb39e8c.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("high scores").sheet1

    data = sheet.get_all_records()

    for i,row in enumerate(data):
        if score >= row['score']:
            sheet.insert_row([name, score], i+2)
            return

    sheet.insert_row([name, score], len(data) + 2)

def printHS(screen, font):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("High Scores Snake-7b087cb39e8c.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("high scores").sheet1

    data = sheet.get_all_records()
    screen.blit(font.render("GLOBAL HIGH SCORES", 30, (255, 255, 255)), (400, 20))
    for i, row in enumerate(data):
        if i >= 5:
            break
        screen.blit(font.render("{0}) ".format(i+1), 30, (255, 255, 255)), (400, 90 + 100 * i))
        screen.blit(font.render("{0} ".format(data[i]["name"]), 30, (255, 255, 255)), (450, 90+ 100 * i))
        screen.blit(font.render("{0}".format(data[i]["score"]), 30, (255, 255, 255)), (650, 90 + 100 * i))






