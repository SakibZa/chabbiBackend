from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
  
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')
    
  
    date_difference = (to_date_obj - from_date_obj).days
    
 
    if date_difference < difference:
        return True
    else:
        return False


from_date = '21-05-01'
to_date = '21-05-10'
difference = 10
result = check_date_difference(from_date, to_date, difference)
print(result)
