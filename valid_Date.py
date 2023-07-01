# validateing correct date format
import datetime

#function to validate data value
def validate_Date(date): 
 
    # giving the date format
    date_format = '%Y-%m-%d'

    # formatting the date using strptime() function
    dateObject = bool(datetime.datetime.strptime(date, date_format))
    return dateObject
        
