def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    else:
        suffix = "am" if hours < 12 else "pm"
        hour12 = hours % 12
        if hour12 == 0:
            hour12 = 12
        return f"{hour12}:{minutes:02d}{suffix}"
print(time_string(14,30,'24'))  # Should print 02:30
print(time_string(3,50,'12'))  # Should print 03:50

