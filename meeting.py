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

def meeting_cost(duration_hours, cost_per_person):
    total = 0
    for person, rate in cost_per_person.items():
        total = total + rate
    return total / duration_hours

print(people_hours(1.5, 6))
