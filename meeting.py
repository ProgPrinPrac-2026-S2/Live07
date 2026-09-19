c = {
    "Alice": 50,
    "Bob": 80,
    "Charlie": 100
}

def people_hours(duration_hours, attendees):
    if duration_hours == None:
        return 0
    if attendees == None:
        attendees = 0
    return duration_hours * attendees

print(people_hours(1.5, 6))
