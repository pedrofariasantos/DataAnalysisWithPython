import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1
    )

    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_edu)]
    lower_education = df[~df['education'].isin(advanced_edu)]

    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0]
         / higher_education.shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0]
         / lower_education.shape[0]) * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers[min_workers['salary'] == '>50K'].shape[0]
         / min_workers.shape[0]) * 100, 1
    )

    country_earnings = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_earnings = country_earnings['>50K'] * 100
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(country_earnings.max(), 1)

    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
