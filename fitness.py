from datetime import datetime



def main():

    gender = (input("What is your gender?(m/w): "))

    birthdate = (input('Enter your birth date (YYYY-MM-DD): '))

    weight = float(input('Enter your weight (in US pounds): '))

    height = float(input('Enter your height (in US inches): '))

    kg = kg_from_lb(weight)

    cm = cm_from_in(height)

    age = compute_age(birthdate)

    bmr = basal_metabolic_rate(gender, weight, height, age)

    bmi =  body_mass_index(weight, height)
    print(f'You are {age} years old')

    print(f'Your weight is {kg:.2f} kg and your height is {cm:.2f} in cm ')
   
    print(f'Your bmi is {bmi:.2f}, and your bmr is {bmr:.2f}')
    
    

def compute_age(birth):

    birthday = datetime.strptime(birth, '%Y-%m-%d')
    today = datetime.now()

    years = today.year - birthday.year

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years-= 1

    return years

def kg_from_lb(weight):

    kg = weight * 0.45359237


    return kg


def cm_from_in(height):

    cm = height * 2.45

    return cm

def body_mass_index(weight, height):

    bmi = (10000 * weight) / height **2

    return bmi




def basal_metabolic_rate(gender, weight, height, age):

    if gender.lower()== 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    


    return bmr



main()
