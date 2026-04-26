import pandas as pd

# دالة لتحويل التنسيق الرقمي (مثل 1545) إلى صيغة وقت (15:45)
def format_time(time_val):
    if pd.isna(time_val) or time_val == 2400: # معالجة القيم المفقودة أو غير المنطقية
        return "00:00"
    
    time_val = int(time_val)
    hours = (time_val // 100) % 24  # القسمة المطولة تعطي الساعة
    minutes = time_val % 100         # باقي القسمة يعطي الدقائق
    
    return f"{hours:02d}:{minutes:02d}"