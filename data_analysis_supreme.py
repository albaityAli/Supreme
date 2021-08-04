import pandas as pd
import openpyxl
import time

def check_name(cell):
    cell = cell.capitalize()
    return cell


def check_postcode(cell):
    cell = cell.replace(" ", "").upper()
    return cell


def check_numbers(cell):
    return cell.replace('"', '')


df = pd.read_excel("supreme_accounts.xlsx", converters={
    'Postcode': check_postcode,
    'CardNumber': check_numbers,
    'ExpiryM': check_numbers,
    'ExpiryY': check_numbers,
    'Security': check_numbers,
    'Phone': check_numbers,
})
shape = df.shape
rows = []
for i in range(1, shape[0]+1):
    rows.append(i)

