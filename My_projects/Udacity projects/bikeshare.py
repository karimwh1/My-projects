import time
import pandas as pd
import numpy as np
'''identifiying the variable that will be used in the dataframe below'''
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january','february','march','april','may','june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    '''putting the required code for the use to input the data that will be used later on in filtering'''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input( "please enter city name :" ).lower()
    while city not in ['chicago','new york city','washington']:
        print("please input correct city name :")
        city = input("please enter valid city name !")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("please enter name of the month or all if no filter :").lower()
    while month not in months:
        print("please input a valid month :")
        month = input("enter valid month name !")
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please enter name of the day or all if no filter :").lower()
    while day not in days:
        print("please enter a valid day :")
        day = input("enter a valid day name !")
                               

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specif
    ied city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    '''converting the start time colmn to date time '''
    df['Start Time']= pd.to_datetime(df['Start Time'])
   
    df['month']=df['Start Time'].dt.month
    
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month) +1
    df=df[df['month']==month]
    
    
    
    df['day']=df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df['day'] == day.title()]
        
        
    df['hour']=df['Start Time'].dt.hour


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    '''getting the most popular month, day and hour using the mode function'''
    popular_month= df['month'].mode()[0]
    print('most popular month is : ', popular_month)
    
    
    
    popular_day=df['day'].mode()[0]
    print('most popular day is : ', popular_day)

    
    most_frequenthour=df['hour'].mode()[0]
    print('most frequent hour is ', most_frequenthour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

 
    
    most_common_start_station= df['Start Station'].mode()[0]
    print('Most common start station is : ',most_common_start_station)

    mostcommon_end_station = df['End Station'].mode()[0]
    print('Most common end station is : ',mostcommon_end_station)
   

    
    df['trip']= df['Start Station'] +'to' +df['End Station']
    common_trip = df['trip'].mode()[0]
    print(common_trip)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_travel_time= df['Trip Duration'].sum()
    print('Total time of all trips:',total_travel_time)


    
    mean_travel_time=df['Trip Duration'].mean()
    print('The average time of all trips:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_count= df['User Type'].value_counts()


    
    


   
    if 'Birth Year' in df:
        early_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        mostcommon_year = df['Birth Year'].mode()[0]
        
        print('early year count is :', early_year, '\n')
        print('recent year count is :', recent_year, '\n')
        print('most common year is :', mostcommon_year, '\n')
    else:
        print('There is no birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    if 'Gender' in df:
        gender_count= df['Gender'].value_counts()
        print('the gender count is :', df['Gender'].value_counts())
    else:
        print('There is no gender column')

def display_raw_data(df):
    '''input for the user to get the raw data from the trips'''
    response = input( "please enter Yes or No to print raw data :" ).lower()
    while response == 'yes':
        print(df.sample(n=5))
        
        restart = input('\nWould you new raw data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
