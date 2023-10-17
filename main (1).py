# Leap Year

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""
def isLoopYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("Enter the year :"))

if isLoopYear(year):
  print("{} is a loop year.".format(year))
else:
  print("{} is not a loop year.".format(year))
  