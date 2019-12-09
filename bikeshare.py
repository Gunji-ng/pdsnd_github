import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']

days = {'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday', 'thur': 'Thursday', 'fri': 'Friday', 'sat': 'Saturday', 'sun': 'Sunday', 'all': 'all'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city's data would you like to explore?\n('Chicago', 'New York City', 'Washington'):\n").strip().lower()
        if city in CITY_DATA:
            break
        print("\nPlease enter a valid city:\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter by any month?\n('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun') Input 'all' to ignore filter:\n").strip().lower()
        if month in months:
            break
        print("\nPlease input a valid month (in the format displayed below)\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to filter by any particular day of the week?\n('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun') Input 'all' to ignore filter:\n").strip().lower()
        if day in days:
            break
        print("\nPlease input a valid day (in the format displayed below)\n")

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
    # load the City Data into a Pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to Pandas timedate format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create 'Month', 'Day of Week' and 'Hour' columns from 'Start Time'
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != 'all':
        month_no = months.index(month) + 1

        df = df[df['Month'] == month_no]

    # filter by day
    if day != 'all':
        df = df[df['Day of Week'] == days[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    print("The most common month:", months[common_month])

    # display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print("The most common day of week:", common_day)

    # display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print("The most common hour of the day:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station:", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common End Station:", popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    frequent_trip = df['Trip'].mode()[0]
    print("The most frequent trip is from:", frequent_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time within this period:", total_travel_time, "seconds")

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time within this period:", average_travel_time, "seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type count:", "\n", df['User Type'].value_counts(), "\n")

    # Check if the 'Gender' column exists in the DataFrame
    if 'Gender' in df.columns:
        # Display counts of gender
        print("Gender count:", "\n", df['Gender'].value_counts(), "\n")
    else:
        print("There's no gender information for this city", "\n")

    # Check if the 'Birth Year' column exists in the DataFrame
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth:", df['Birth Year'].min())

        print("Most recent year of birth:", df['Birth Year'].max())

        print("Most common year of birth:", df['Birth Year'].mode()[0])
    else:
        print("There's no birth year information for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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


if __name__ == "__main__":
	main()


def get_input():
    print('-'*40)
    # get user input for city (chicago, new york city, washington).
    city = input("What city's raw data would you like to explore?\n('Chicago', 'New York City', 'Washington'):\n").strip().lower()
    print('-'*40)
    return city


def load_raw_data(city):
    # load the City Data into a Pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])
    return df


def show_raw_data(df):
    # Display first five rows in the DataFrame
    print(df.head())


def parse_raw_data():
    while True:
        city = get_input()
        df = load_raw_data(city)

        show_raw_data(df)

        keep_going = input("\nWould you like to see other raw data?\nEnter 'yes' or 'no':\n").strip().lower()
        if keep_going != 'yes':
            print("Thank you for using this platform!\n")
            break


def see_raw_data():
    # Ask users if they would like to view 5 rows of raw data
    decision = input("\nWould you like to view a City's raw data (5 rows only)?\nEnter 'yes' or 'no':\n").strip().lower()

    if decision == 'yes':
        parse_raw_data()
    else:
        print("Thank you for using this platform!\n")

see_raw_data()
