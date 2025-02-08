def life_in_weeks(age):
    weeks_per_year = 4 * 12
    current_age_in_weeks = age * weeks_per_year
    result = (90 * weeks_per_year) - current_age_in_weeks
    return result
    
age = int(input ("what is your current age?: "))
weeks = life_in_weeks(age)
print (f"You have {weeks} left. ")