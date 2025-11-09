def breakdown_time(seconds):
    if not isinstance(seconds, int) or seconds<0:
        return -1
    if seconds==0:
        return {}
    result={}
    for unit in [3600,60,1]:
        count=seconds//unit
        if count>0:
            result[unit]=count
        seconds %= unit
    return result