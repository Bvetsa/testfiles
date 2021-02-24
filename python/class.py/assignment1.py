year = 366
december = 31
months_past = 11
days_past = year - december
sibling_steal = (days_past // 7) * 3
buy_box = 5 * months_past
coins_start = 26 
coins_per_day = 15
coins = coins_start + (((coins_per_day * days_past) - buy_box) - sibling_steal)


print("At the end of the year you will have %d coins" %(coins))