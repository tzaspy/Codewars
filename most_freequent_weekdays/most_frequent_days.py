def is_leap_year(year):
    return 1 if (((year %4  == 0) and (year % 100 != 0)) or (year % 400 == 0 )) else 0

def most_frequent_days(year):
    dict= {
        '0' : "Monday",
        '1' : "Tuesday",
        '2' : "Wednesday",
        '3' : "Thursday",
        '4' : "Friday",
        '5' : "Saturday",
        '6' : "Sunday"
    }
    # first day of year 1 is Monday
    cent_year = year - (year % 100) + 1
    first_day = ( sum ( map(lambda c: 124 + is_leap_year(c), range(100, cent_year, 100)), 0) +
        sum( map(lambda y: 1 + is_leap_year(y), range(cent_year, year))) ) % 7
    return [ dict[ str(first_day) ] ] if is_leap_year(year) == 0 else [ dict[str(min (first_day, (first_day + 1) % 7))], dict[str(max(first_day, (first_day + 1) % 7))] ]
