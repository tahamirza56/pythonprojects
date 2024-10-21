#week number and print week day
week_days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
week_number = int(input("Enter week number (1-7): "))

if 1 <= week_number <= 7:
    print(f"Day of the week: {week_days[week_number]}")
else:
    print("Invalid week number! Please enter a number between 1 and 7.")