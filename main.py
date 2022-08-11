import pandas

data = pandas.read_csv("Original_Squirrel_Data.csv")
gray = (data[data["Primary Fur Color"] == "Gray"])
cinnamon = (data[data["Primary Fur Color"] == "Cinnamon"])
black = (data[data["Primary Fur Color"] == "Black"])
am_count = (data[data["Shift"] == "AM"])
pm_count = (data[data["Shift"] == "PM"])
ground = (data[data["Location"] == "Ground Plane"])
above = (data[data["Location"] == "Above Ground"])
na = (data[data["Location"].isnull()])

squirrel_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Fur Count": [len(gray), len(cinnamon),  len(black)],
    "Location": ["Not Specified", "Ground Plane", "Above Ground"],
    "Location Count": [len(na), len(ground), len(above)],
    "Shift": ["AM", "PM", " "],
    "Shift Count": [len(am_count), len(pm_count), " "],
}


fur_data = pandas.DataFrame(squirrel_data)
fur_data.to_csv("Squirrel Data.csv")
