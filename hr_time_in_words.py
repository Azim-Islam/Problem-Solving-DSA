hours = {0:"",
         1:"one ",
         2:"two ",
         3:"three ",
         4:"four ",
         5:"five ",
         6:"six ",
         7:"seven ",
         8:"eight ",
         9:"nine ",
         10:"ten ",
         11:"eleven ",
         12:"twelve ",
         13:"thirteen ",
         14:"fourteen ",
         15:"quarter ",
         16:"sixteen ",
         17:"seventeen ",
         18:"eighteen ",
         19:"nineteen "
         }
hr = int(input())
mi = int(input())
if mi == 0:
    print(f"{hours[hr]}o' clock")
elif mi == 1:
    print(f"one minute past {hours[hr]}")
elif mi == 15:
    print(f"{hours[mi]}past {hours[hr]}")
elif mi == 30:
    print(f"half past {hours[hr]}")
elif mi < 20:
    print(f"{hours[mi]}minutes past {hours[hr]}")
elif mi >= 20 and mi < 30:
    print(f"twenty {hours[mi%10]}minutes past {hours[hr]}")
else:
    mi = 60-mi
    if mi == 1:
        print(f"one minute to {hours[hr+1]}")
    elif mi == 15:
        print(f"{hours[mi]}to {hours[hr+1]}")
    elif mi >= 20:
        print(f"twenty {hours[mi%10]}minutes to {hours[hr+1]}")
    else:
        print(f"{hours[mi]}minutes to {hours[hr+1]}")