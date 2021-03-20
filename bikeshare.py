import time
import pandas as pd
import numpy as np

 # {key: value for key, value in variable}
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   # city = str(input('would you like to see data for which city chicago, new yourk city, washington ?\n')).lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        city = str(input('Would you like to see data for  chicago, new yourk city or washington ?\n')).lower().strip()
        if city not in CITY_DATA.keys() :
            print('Your input is vaild ,please try again !')
            continue
        else:
            break
    filter_data = input('Would you like to filter data by month and day write both ? if not write "none"\n').lower().strip()

    if filter_data == 'both':
        month = input('Do you want to filter month by (all, january, february, ... , june)?\n').title().strip()
        day = input('Do you want to filter day of week by (all, monday, tuesday, ... sunday) ?\n').title().strip()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load data to DataFrame
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All' :
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()

    #convert the type of Start Time from string to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month is {} \n'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day of the week is {} \n'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour is {} \n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most popular stations and trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is {}\n'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common End Station is {} \n'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Time'].astype(str) + ' to ' + df['End Time']
    comb_start_end = df['combination'].mode()[0]
    print('The most frequent combination of Start Station and End Station is {}\n'.format(comb_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} \n'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} \n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count of User Type iS {} \n'.format(user_type))

    # TO DO: Display counts of gender
    try:
          gender = df['Gender'].value_counts()
          print('The count of Gender iS {} \n'.format(gender))
    except:
          print('There is no Gender column')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
          earliest_birth_year = df['Birth Year'].min()
          recent_birth_year = df['Birth Year'].max()
          common_birth_year = df['Birth Year'].mode()[0]
          print('The earliest Birth Year is {} \n , The most recent Birth Year is {} \n , The most common Birth Year is {} \n .'.format(earliest_birth_year,recent_birth_year,common_birth_year))
    except:
          print('There is no Birth Year column')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# the main function the code will staet runing from there 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
          break
    user_row_data = input('if you want to view row data write yes if not, no.\n').lower()
    start = 0
    end = 5
    while user_row_data == 'yes':
         print(df.iloc[start:end])
         start += 5
         end += 5
         user_row_data = input('if you want to see more rows weite yes.\n').lower()


if __name__ == "__main__":
	main()
