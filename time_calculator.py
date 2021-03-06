def add_time(start, duration, day=None):
    start_split = start.split(' ')
    am_pm = start_split[1]
    hour = int(start_split[0].split(':')[0])
    minutes = int(start_split[0].split(':')[1])
    hours_to_add = int(duration.split(':')[0])
    minutes_to_add = int(duration.split(':')[1])
    new_minutes = 0
    new_hours = 0
    new_time = None
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # convert time to military equivalent
    if am_pm == 'PM':
        hour += 12

    # calculate total hours and minutes
    total_hours = hour + hours_to_add
    total_minutes = minutes + minutes_to_add

    # add to the total hours if there are more than 60 total minutes
    if total_minutes > 60:
        total_hours += 1
        new_minutes = total_minutes - 60
    else:
        new_minutes = total_minutes

    # add 0 it minutes are single digits
    if new_minutes < 10:
        new_minutes = '0' + str(new_minutes)
    else:
        new_minutes = str(new_minutes)

    days = total_hours // 24

    # adjust total hours based on number of days
    if total_hours > 24:
        new_hours = total_hours - (days * 24)
    else:
        new_hours = total_hours
    
    # set time
    if new_hours < 12:
        if new_hours == 0:
            new_time = '12:' + new_minutes + ' AM'
        else:
            new_time = str(new_hours) + ':' + new_minutes + ' AM'
    elif new_hours < 24:
        if new_hours == 12:
            new_time = '12:' + new_minutes + ' PM'
        else:
            new_time = str(new_hours - 12) + ':' + new_minutes + ' PM'

    # set new day
    if day != None:
        day_index = days_list.index(day.lower())
        new_day_index = (day_index + days)

        if new_day_index > 6:
            new_day_index = new_day_index - (days + 1)
        new_day = days_list[new_day_index]


    # set time if day is included
    if day != None:
        # print(new_day_index)
        new_time = new_time + ', ' + new_day.capitalize()

    # set time with additional info
    if days == 1:
        new_time = new_time + ' (next day)'
    elif days >= 2:
        new_time = new_time + f' ({days} days later)'

    return new_time


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
add_time("8:16 PM", "466:02", "tuesday")
# Returns: 6:18 AM, Monday (20 days later)