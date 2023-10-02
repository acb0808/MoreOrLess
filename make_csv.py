import requests
import json
rsp_sheet = requests.get('https://sheets.googleapis.com/v4/spreadsheets/1u4ocn7s-ru5KHO9POa0q4nXpBtwZEirUH3uQ3dlCmjQ/values:batchGet?ranges=real-keyword&key=AIzaSyAiiUG2E6aD6d082i7dG_P1GbeEUbLPgpE').text


# check google spreadsheet api document 
rsp = json.loads(rsp_sheet)
print(rsp.keys())
print(rsp['valueRanges'][0].keys())

'''
file head
0-"name"
1-"count"
2-"category_0"
3-"category_1"
4-"category_2"
5-"category_2"
6-"imageUrl_0"
7-"imageUrl_1"
8-"imageUrl_2"
'''

# with open('더많이더적게.csv', 'w', encoding='cp949') as f:
with open('더많이더적게.csv', 'w', encoding='utf-16') as f:
    for row in rsp['valueRanges'][0]['values']:
        f.write(','.join(row[:2]) + '\n')

