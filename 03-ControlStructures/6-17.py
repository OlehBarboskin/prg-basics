entered_time = input("Enter your time in 24-hour format: ").strip()

try:
    parts = entered_time.split(':')
    if len(parts) != 2:
        raise ValueError
    h = int(parts[0])
    m = int(parts[1])
    if not (0 <= h <= 23 and 0 <= m <= 59):
        raise ValueError
except ValueError:
    print("Invalid time format. Use hh:mm (00:00 - 23:59).")
else:
    if h == 0:
        hour12 = 12
        suffix = 'am'
    elif 1 <= h <= 11:
        hour12 = h
        suffix = 'am'
    elif h == 12:
        hour12 = 12
        suffix = 'pm'
    else:
        hour12 = h - 12
        suffix = 'pm'

    print(f"Time in 12-hour format: {hour12}:{m:02d}{suffix}")