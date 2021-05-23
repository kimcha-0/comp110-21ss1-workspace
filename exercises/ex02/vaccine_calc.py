"""A vaccination calculator."""

__author__: str = "730407570"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: str = input("Population: ")
doses_administered: str = input("Doses administered: ")
doses_per_day: str = input("Doses per day: ")
target_percent_vaccinated: str = input("Target percent vaccinated: ")

unvaccinated_pop: float = int(population) - int(target_percent_vaccinated) * .01 * int(population)
days_to_target: float = unvaccinated_pop / int(doses_per_day)

today: datetime = datetime.today()
days_to_target_date: timedelta = timedelta(days_to_target)
target_date: datetime = today + days_to_target_date
print("We will reach " + str(target_percent_vaccinated) + "% vaccination in " + str(int(days_to_target)) + " days, which falls on " + target_date.strftime( "%B %d, %Y."))