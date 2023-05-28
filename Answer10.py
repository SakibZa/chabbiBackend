from datetime import datetime, timedelta

def calculate_previous_date(date, n):
  
    date_obj = datetime.strptime(date, '%y-%m-%d')
    
  
    previous_date_obj = date_obj - timedelta(days=n)
    
 
    previous_date = previous_date_obj.strftime('%y-%m-%d')
    
    return previous_date


date = '16-12-10'
n = 11
previous_date = calculate_previous_date(date, n)
print(previous_date)
