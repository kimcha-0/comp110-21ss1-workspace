"""Practicing with CSVs."""

from csv import DictReader

# row orinted: list[dict[str, str]]
# column oriented: dict[str, list[str]]

file_handle = open("data/weather.csv", encoding="utf8")
csv_reader = DictReader(file_handle)

# a table can be modeled as a list of rows
# where each row is a dictionary with the column title as the key

table: list[dict[str, str]] = []
for row in csv_reader:
    table.append(row)
    # print(row)
print(table)

file_handle.close()

# let's calculate the average high temp
# process the table by a specific column
high_temps: list[float] = []
for row in table:
    high: float  = float(row["high"])
    high_temps.append(high)
print(f"The high temps were {high_temps}")
# sum() sums the elements in the list
avg_high: float = sum(high_temps) / len(high_temps)
print(f"The average high temp was: {avg_high}.")
