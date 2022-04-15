def add_time(start, duration):
    start_split = start.split(' ')
    am_pm = start_split[1]
    hours = int(start_split[0].split(':')[0])
    minutes = int(start_split[0].split(':')[1])
    add_hours = int(duration.split(':')[0])
    add_minutes = int(duration.split(':')[1])
    days = 0

    if am_pm == 'PM':
        hours += 12

    total_hours = hours + add_hours
    
    if total_hours > 24:
        days = total_hours // 24

    print(days)






    # return new_time

add_time("3:00 PM", "27:10")