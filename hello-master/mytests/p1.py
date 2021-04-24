import pandas as pd

filename = 't1.xlsx'
book = pd.read_excel(filename, sheet_name='첫번째 시트', header=0)

book = book.sort_values(by='좋아요', ascending=False)

print(book)