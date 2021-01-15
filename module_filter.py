def get_filters(city_dict, filter_dict, month_dict, day_dict):

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day -  name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    city = None
    filter_mode = None
    month = int()
    day = int()

    user_input = None
    message = None
    output = None

    question = {1 : "Would you like to analyse data for Chicago (C), New York (N) or Washington (W)?\n",
                2 : "Would you like to filter the data by month (m), day (d), both (b) or not at all? Type 'n' for no time filter.\n",
                3 : "Which month January (1), February (2), March (3), April (4), May (5) or June (6).\n",
                4 : "Which day Monday (1), Tuesday (2), Wednesday (3), Thursday (4), Friday (5), Saturday (6) or Sunday (7).\n"
                }

    error_message = {1 : "Please enter 'C' for Chicago 'N' for New York or 'W' for Washington.\n",
                    2 : "Please enter 'm' for month, 'd' for day, 'b' for both or 'n' for no filter usage.\n",
                    3 : "Please enter '1' for January , '2' for February, '3' for March, '4' for April, '5' for May or '6' for June.\n",
                    4 : "Please enter '1' for Monday, '2' for Tuesday, '3' for Wednesday, '4' for Thursday, '5' for Friday, '6' for Saturday or '7' for Sunday.\n"
                    }

    success_message = {1 : "\nYou entered '{}' to analyse the data for the city '{}'\n",
                      2 : "\nYou entered '{}' to analyse the data by using '{}' filter\n",
                      3 : "\nYou entered '{}' to analyse the data for the month of '{}'\n",
                      4 : "\nYou entered '{}' to analyse the data for the day of '{}'\n"
                      }

    for i in question:
        message = question[i]
        while city not in city_dict or filter_mode not in filter_dict or month not in month_dict or day not in day_dict:
            try:

                if i == 1:
                    # get user input for city (chicago, new york city, washington).
                    # HINT: Use a while loop to handle invalid inputs
                    user_input = str(input(message))
                    city = user_input.upper()
                    output = city_dict[city]
                    print (success_message[i].format(user_input, output))
                    break

                elif i == 2:
                    # get user input for the usage of a filter (month, day, both or none)
                    user_input = str(input(message))
                    filter_mode = user_input.upper()
                    output = filter_dict[filter_mode]
                    print (success_message[i].format(user_input, output))
                    break

                elif i == 3 and filter_mode not in ("N","D"): #bypass month and day for 'n' or month for 'd'
                    # get user input for month (all, january, february, ... , june)
                    user_input = int(input(message))
                    month = user_input
                    output = month_dict[month]
                    print (success_message[i].format(user_input, output))
                    break

                elif i == 4 and filter_mode not in ("N", "M"): #bypass month and day for 'n' or day for 'm'
                    # get user input for day of week (all, monday, tuesday, ... sunday)
                    user_input = int(input(message))
                    day = user_input
                    output = day_dict[day]
                    print (success_message[i].format(user_input, output))
                    break

                elif filter_mode in ("N", "M", "D"):
                    break

            except (ValueError, TypeError, KeyError) as e:
                print("\nYou entered an invalid Value {}".format(e, user_input))
                message = error_message[i]

            else:
                if city not in city_dict or filter_mode not in filter_dict or month not in month_dict or day not in day_dict:
                    print("\nYou entered an invalid Value '{}'".format(user_input))
                    message = error_message[i]

    print('-'*60)
    return city, month, day, filter_mode
