import time
import pandas as pd
import numpy as np
# I have used the same bikeshare.py file and i have added the need parts so that it will work.
# I just capitilized the first name for the city,s name in Citi_Data dictionry so it can work with the raw input below.
# I tried not to use complicated filters for the day and month to make  the code simple.
# I changed the Hyphen (-) to be 120 instead of 40 to help me read the results easily.

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
    print('Hello! Let\'s explore some US bikeshare data for the first six months on 2017!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("would you  like to see data for Chicago , New york city, or Washington?\n")
    while city  not in  CITY_DATA.keys():
        print("the city you entered is not valid")
        city = input("Please enter a valid city.\n").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june',"all"]
    month = input("which month? \n").lower()
    while  month  not in months:
        print("the month you entered is not valid!")
        month = input("please enter a valid month.\n")
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', "all"]
    day = input("which day?monday, tuesday, wednesday, thursday, friday, saturday, sunday\n").lower()
    while day not in DAYS:
        print("the day you entered is not valid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        day = input("please enter a valid day.\n").lower()
        
    print('-'*120)
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
    print("loading data..................................................................................")
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
        
    #Filter for month
    months = ['january', 'february', 'march', 'april', 'may', 'june',"all"]
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filter for day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel..................................\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(common_day)
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip............................................\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:{} ".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['whole_trip'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    combination = df['whole_trip'].mode()[0]
    print("The most frequent combination of trips are from {} ".format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration................................................................\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time,60)
    hour, second = divmod(minute,60)
    print("the total_travel_time is {} hours , {} minutes , {} second".format(hour,minute,second))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    minute, second = divmod(mean_travel_time,60)
    if minute < 60 :
         print("the_mean_travel_time is {} minutes , {} second".format(minute,second))
    else:
        hour, second = divmod(minute,60)
        print("the mean_travel_time is {} hours , {} minutes , {} second".format(hour,minute,second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The types of users by number are :\n{}".format(user_type))


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Gender are :\n{}".format(gender))
    except :
        print("sorry Gender information for this city is not available")
    # Display earliest, most recent, and most common year of birth
    try :
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth: {}\n\nThe most recent year of birth: {}\n\nThe most common year of birth {}".format(earliest,recent,common_year))
    except:
        print("sorry Birth Year information for this city is not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)
    
# display data function
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == "yes") :
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
