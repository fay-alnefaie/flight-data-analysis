import pandas as pd

def format_time(time_val):
    if pd.isna(time_val) or time_val == 2400: 
        return "00:00"
    
    time_val = int(time_val)
    hours = (time_val // 100) % 24  
    minutes = time_val % 100         
    
    return f"{hours:02d}:{minutes:02d}"