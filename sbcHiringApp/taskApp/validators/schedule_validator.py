from django.core.exceptions import ValidationError
from datetime import datetime, timezone

start_time = datetime.now(timezone.utc)
end_time = datetime.now(timezone.utc)
def validate_start_date_time(value):
    global start_time
    weekday = value.weekday()
    time = value.hour
    if time < 9 or time > 18 or weekday > 5:
        raise ValidationError("This field is invalid. Insert working hours")
        
    else:
        start_time = value
        return value
def validate_end_date_time(value):
    global start_time,end_time
    weekday = value.weekday()
    time = value.hour
    end_time = value
    duration = end_time - start_time
    duration_in_m = divmod(duration.total_seconds(),60)[0]
    if time < 9 or time > 18 or weekday > 5 or duration_in_m < 0 or duration_in_m > 30:
        raise ValidationError("This field is invalid. Time is not within working hours or exceeds 30min limit")
        
    else:
        return value