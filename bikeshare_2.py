import time
import pandas as pd
import numpy as np
import module_filter as filter
import module_load_data as data

city_data_dict = { 'C': 'chicago.csv',
                   'N': 'new_york_city.csv',
                   'W': 'washington.csv' }

city_dict = {'C' : 'Chicago',
             'N' : 'New York',
             'W' : 'Washington'
            }

filter_dict= {'M' : 'month',
              'D' : 'day',
              'B' : 'both',
              'N' : 'no'
             }

month_dict = {1 : 'January',
              2 : 'February',
              3 : 'March',
              4 : 'April',
              5 : 'May',
              6 : 'June'
             }

day_dict = {1 : 'Monday',
            2 : 'Tuesday',
            3 : 'Wednesday',
            4 : 'Thursday',
            5 : 'Friday',
            6 : 'Saturday',
            7 : 'Sunday'
           }

def pretty_print(input_variable):

    if input_variable == "Unnamed: 0":
        input_variable = "ID"

    label = input_variable + ":" + ' '*int(27-len(input_variable))

    return label

def time_stats(df, filter_mode):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    common_month_count = df['month'].value_counts().max()

    # display the most common day of week
    common_day = df['day'].mode()[0]
    common_day_count = df['day'].value_counts().max()

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    common_hour_count = df['hour'].value_counts().max()
    if filter_mode != "B":
        print("{}'{}' with '{}'".format(pretty_print("Most Popular Month"), month_dict[common_month], common_month_count),
            "\n{}'{}' with '{}'".format(pretty_print("Most Popular Day"), day_dict[common_day], common_day_count))
    else:
        print("{}'{}' for '{}s' in '{}'".format(pretty_print("Number of rentals"), common_month_count, day_dict[common_day], month_dict[common_month]))

    print("{}'{}' with '{}'".format(pretty_print("Most Popular Start Hour"), common_hour, common_hour_count),
          "\n{}'{}'".format(pretty_print("Filter Mode"), filter_dict[filter_mode]))
    print("{}'%s' seconds.\n".format(pretty_print("This took")) % (time.time() - start_time))
    print('-'*60)


def station_stats(df, filter_mode):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    common_start_station_scount = df['Start Station'].value_counts().max()

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    common_end_station_count = df['End Station'].value_counts().max()

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    common_trip_count = df['Trip'].value_counts().max()

    print("{}'{}' with '{}'".format(pretty_print("Most Popular Start Station"), common_start_station, common_start_station_scount),
          "\n{}'{}' with '{}'".format(pretty_print("Most Popular End Station"), common_end_station, common_end_station_count),
          "\n{}'{}' with '{}'".format(pretty_print("Most Popular Trip"), common_trip, common_trip_count),
          "\n{}'{}'".format(pretty_print("Filter Mode"), filter_dict[filter_mode]))
    print("{}'%s' seconds.\n".format(pretty_print("This took")) % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df, filter_mode):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    total_travel_time_formated = str(total_travel_time // 3600) + ":" + str(total_travel_time %3600 // 60) + ":" + str(total_travel_time %3600 % 60)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("{}'{} s' ≈ '{}'".format(pretty_print("Total Travel Time"), total_travel_time, total_travel_time_formated),
          "\n{}'{}'".format(pretty_print("Mean Travel Time"), mean_travel_time),
          "\n{}'{}'".format(pretty_print("Filter Mode"), filter_dict[filter_mode]))
    print("{}'%s' seconds.\n".format(pretty_print("This took")) % (time.time() - start_time))
    print('-'*60)


def user_stats(df, filter_mode):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()

    # Display counts of gender
    if 'Gender' in df:
        count_gender= df['Gender'].value_counts()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        common_birth_count = df['Birth Year'].value_counts().max()

    print("Counts of User Types")

    for user_type_index,user_type in enumerate(count_user_type.index.tolist()):
        print("{}'{}'".format(pretty_print(user_type),count_user_type[user_type_index]))

    print("\nCounts of Genders")
    if 'Gender' in df:
        for gender_index,gender in enumerate(count_gender.index.tolist()):
            print("{}'{}'".format(pretty_print(gender),count_gender[gender_index]))
    else:
        print("{}'{}'".format(pretty_print("Gender"),"no Gender Data available"))

    print("\nFurther Details")

    if 'Birth Year' in df:
        print("{}'{}'".format(pretty_print("Earliest Year of Birth"), earliest_birth),
              "\n{}'{}'".format(pretty_print("Most recent Year of Birth"), recent_birth),
              "\n{}'{}' with '{}'".format(pretty_print("Most common Year of Birth"), common_birth, common_birth_count))
    else:
        print("{}'{}'".format(pretty_print("Year of Birth"),"no Year of Birth Data available"))

    print("{}'{}'".format(pretty_print("Filter Mode"), filter_dict[filter_mode]))
    print("{}'%s' seconds.\n".format(pretty_print("This took")) % (time.time() - start_time))
    print('-'*60)


def main():
    iteration = int()
    number_entries = int()
    while True:
        city, month, day, filter_mode = filter.get_filters(city_dict, filter_dict, month_dict, day_dict)

        df = data.load_data(city_data_dict, city, month, day)

        time_stats(df, filter_mode)
        station_stats(df, filter_mode)
        trip_duration_stats(df, filter_mode)
        user_stats(df, filter_mode)

        while True:
            if iteration == 0:
                individual = str(input("\nWould you like to view individual trip data? yes (y) or no (n).\n"))
                if individual.lower() != "y": break
                while True:
                    try:
                        number_entries = int(input("\nHow much entries would you like to show?\n"))
                        break
                    except (ValueError, TypeError, KeyError) as e:
                        print("\nYou entered an invalid Value {}".format(e, number_entries))
            else:
                individual = str(input("\nMore trip data? yes (y) or no (n).\n"))
                if individual.lower() != "y": break

            df_dict = df[iteration: iteration+number_entries].to_dict('records')

            for i in df_dict:
                print("\n")
                for key in i:
                    print("{}'{}'".format(pretty_print(key), i[key]))

            iteration += number_entries



        restart = input("\nWould you like to restart? yes (y) or no (n).\n")
        if restart.lower() != "y":
            break


if __name__ == "__main__":
	main()
