import json
import pandas

with open("data.json", "r") as read_file:
    data = json.load(read_file)["data"]

gradeBook = pandas.DataFrame(data)
# gradeBook1 = pandas.DataFrame(data)

# Creates a new Excel File
gradeBook.to_excel('Grade Book.xlsx')

# Write to an existing sheet
# with pandas.ExcelWriter("Grade Book 1.xlsx", engine="xlsxwriter") as writer:
#     gradeBook.to_excel(writer, sheet_name='Grade_1')
#     gradeBook1.to_excel(writer, sheet_name='Grade_2')
