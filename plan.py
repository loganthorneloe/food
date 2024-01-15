import random
import yaml
from datetime import datetime, timedelta

weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def plan_meals(protein, vegs, carbs):
  meal_plan = []
  shopping_list = []

  # pasta meal
  pasta_meal, used_protein, used_veg = plan_pasta(vegs)
  meal_plan.append(pasta_meal)

  block_list = [used_protein, used_veg]

  for i in range(3):
    # forcing chicken breast once a week
    if "chicken_breast" not in block_list:
      meat = "chicken_breast"
    else:
      # grab protein
      meat = random.choice(protein)
      while meat in block_list:
        meat = random.choice(protein)

    block_list.append(meat)
    shopping_list.append(meat)

    # grab veg
    veg = random.choice(vegs)
    while veg in block_list:
      veg = random.choice(vegs)

    block_list.append(veg)
    shopping_list.append(veg)

    # grab carb
    carb = random.choice(carbs)
    while carb in block_list:
      carb = random.choice(carbs)

    block_list.append(carb)
    shopping_list.append(carb)

    meal = {'carb': carb, 'meat': meat, 'veg': veg}
    meal_plan.append(meal)
  
  return meal_plan, shopping_list

def organize_meals(meals, days):
  new_meals = {"Tuesday":"Chicken nuggets with mac and cheese", "Friday": "Costco pizza", "Saturday": "audible or leftovers"}
  format_string = "{} with {} and {}"
  for meal in meals:
    meal_string = format_string.format(meal['meat'], meal['carb'], meal['veg'])
    day = random.choice(days)
    days.remove(day)
    new_meals[day] = meal_string

  return new_meals

def assign_to_date(meals, prep_list):
  reminders = {}
  format_date_string = "{}/{}/{}"
  now = datetime.now()

  # let's start with tomorrow
  for i in range(1,8):
    date = now + timedelta(days=i)
    month = date.month
    day = date.day
    year = date.year
    weekday = weekday_names[date.weekday()]
    meal_date = format_date_string.format(month,day,year) + " 4:00"
    if any(element in meals[weekday] for element in prep_list):
      # set a possible marinating reminder here
      prep_date = date - timedelta(days=1)
      prep_month = prep_date.month
      prep_day = prep_date.day
      prep_year = prep_date.year
      prep_full = format_date_string.format(prep_month, prep_day, prep_year) + " 6:00"
      reminders[prep_full] = "Marinate Chicken?"
    reminders[meal_date] = meals[weekday].replace("_"," ")

  return reminders

def pull_from_yaml():
  data = yaml.safe_load(open('food.yaml','r'))
  return data['protein'], data['vegs'], data['carbs'], data['days'], data['prep_list']

def plan_pasta(vegs):
  pasta_meats = ['ground beef','shrimp']
  meat = random.choice(pasta_meats)
  veg = random.choice(vegs)

  pasta_meal = {'carb': 'pasta', 'meat': meat, 'veg': veg}
  return pasta_meal, meat, veg

protein, vegs, carbs, days, prep_list = pull_from_yaml()
meals, shopping_list = plan_meals(protein, vegs, carbs)
new_meals = organize_meals(meals, days)
reminders = assign_to_date(new_meals, prep_list)


ret = {}
ret['reminders'] = reminders
ret['shopping'] = shopping_list
print(ret)