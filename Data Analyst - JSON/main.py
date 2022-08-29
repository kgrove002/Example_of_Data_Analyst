import json
import pandas

with open("data.json", "r") as read_file:
    data = json.load(read_file)["data"]

gradeBook = pandas.DataFrame(data)
gradeBook1 = pandas.DataFrame(data)

with pandas.ExcelWriter("Grade Book.xlsx") as writer:
    gradeBook.to_excel(writer, sheet_name='Grade_1')
    gradeBook1.to_excel(writer, sheet_name='Grade_2')
