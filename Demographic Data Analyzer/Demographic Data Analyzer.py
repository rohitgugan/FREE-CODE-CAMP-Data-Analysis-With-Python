import pandas as pd

def calculate_demographic_data(print_output=True):
    # Read the dataset
    df = pd.DataFrame({
        'age': [39, 50, 38, 53, 28],
        'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
        'fnlwgt': [77516, 83311, 215646, 234721, 338409],
        'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
        'education-num': [13, 13, 9, 7, 13],
        'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
        'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
        'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
        'race': ['White', 'White', 'White', 'Black', 'Black'],
        'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
        'capital-gain': [2174, 0, 0, 0, 0],
        'capital-loss': [0, 0, 0, 0, 0],
        'hours-per-week': [40, 13, 40, 40, 40],
        'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
        'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
    })

    # Question 1: How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # Question 2: What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Question 3: What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').sum() / df.shape[0] * 100

    # Question 4: What percentage of people with advanced education make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0] * 100

    # Question 5: What percentage of people without advanced education make more than 50K?
    lower_education_rich = df[~advanced_education & (df['salary'] == '>50K')].shape[0] / df[~advanced_education].shape[0] * 100

    # Question 6: What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100

    # Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max() * 100

    # Question 9: Identify the most popular occupation for those who earn >50K in India.
    indian_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = indian_high_earners.value_counts()

    if print_output:
        print("Question 1:\n", race_count, "\n")
        print("Question 2:\n", round(average_age_men, 1), "\n")
        print("Question 3:\n", round(percentage_bachelors, 1), "\n")
        print("Question 4:\n", round(higher_education_rich, 1), "\n")
        print("Question 5:\n", round(lower_education_rich, 1), "\n")
        print("Question 6:\n", min_work_hours, "\n")
        print("Question 7:\n", round(rich_percentage, 1), "\n")
        print("Question 8:\n", highest_earning_country, round(highest_earning_country_percentage, 1), "\n")
        print("Question 9:\n", top_IN_occupation, "\n")

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

# Uncomment the next line to run the function and see the results
calculate_demographic_data(print_output=True)


