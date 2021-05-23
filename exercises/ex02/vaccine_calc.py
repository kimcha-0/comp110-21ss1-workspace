"""A vaccination calculator."""
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

__author__: str = "730407570"
# Begin your solution here...
population: str = input("Population: ")
doses_administered: str = input("Doses administered: ")
doses_per_day: str = input("Doses per day: ")
t_vax: str = input("Target percent vaccinated: ")

target_pop: float = int(population) * int(t_vax) * .01
vaccinated_pop: float = int(doses_administered) / 2
unvaccinated_pop: float = int(population) - vaccinated_pop
goal_pop: float = target_pop - vaccinated_pop
g_days: int = int(round(goal_pop * 2 / int(doses_per_day)))

today: datetime = datetime.today()
days_to_goal_date: timedelta = timedelta(g_days)
t_date: datetime = today + days_to_goal_date

print("We will reach " + (t_vax) + "% vaccination in "
      + str(g_days) + " days, which falls on " + t_date.strftime("%B %d, %Y."))