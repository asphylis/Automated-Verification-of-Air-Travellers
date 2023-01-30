import cv2
import pytesseract


def number_extraction():
    img = cv2.imread('aadharcard.jpg')
    tessdata_dir_config = "C:\\Program Files\\Tesseract-OCR\\tessdata"
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    result = pytesseract.image_to_string(img)

    t = ""
    dob = ""

    for r in result:
        if r.isdigit():
            t = t+r
            dob = t
    s=len(t)
    dob = dob[0:8]
    t = t[s-12:]
    return t

aadhar = number_extraction()
print("Aadhar Number : ", aadhar)


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# JSON File in which credentials are stored
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("projectwork").sheet1

#Get all the data stored in CSV file
data2 = sheet.col_values(5)


if aadhar in data2:
    status = "Verified"
else:
    status = "Unverified"

print(status)

f = open("result.txt", "a")
f.write(status)
f.close()