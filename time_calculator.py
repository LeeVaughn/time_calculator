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

    # convert time to military equivalent
    if am_pm == 'PM':
        hour += 12

    total_hours = hour + hours_to_add
    total_minutes = minutes + minutes_to_add

    if total_minutes > 60:
        total_hours += 1
        new_minutes = total_minutes - 60
    else:
        new_minutes = total_minutes

    if new_minutes < 10:
        new_minutes = '0' + str(new_minutes)
    else:
        new_minutes = str(new_minutes)

    days = total_hours // 24
    

    if total_hours <= 12:
        new_time = str(total_hours) + ':' + new_minutes + ' AM'
    elif total_hours <= 24:
        new_time = str(total_hours - 12) + ':' + new_minutes + ' PM'

    # print(hour)
    # print(new_minutes)
    # print(days)





    print(new_time)
    return new_time

add_time("11:43 AM", "00:20")