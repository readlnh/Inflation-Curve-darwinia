import math

living_time = 0
MILLISECONDS_PER_YEAR = ((36525 * 24 * 60 * 60) / 100) * 1000
total_left = total_left_last_year = 8000000000
total_circulation =  total_circulation_last_year = 2000000000
count = 0
f = open("out.txt", "w")
while count < 50:
    issuable_this_year = 0
    count += 1
    cnt = 0
    while living_time < MILLISECONDS_PER_YEAR * count:
        year = int(living_time / MILLISECONDS_PER_YEAR + 1)
        #print("year:{}\n".format(year))
        p = 1 - pow(0.99, int(math.sqrt(year)))
        #print("p:{}\n".format(p))
        current_total_payout = (180 * 1000.0 / MILLISECONDS_PER_YEAR) * total_left * p
        #f.write("current_total_payout:{}\n".format(current_total_payout))
        total_left -= current_total_payout
        total_circulation += current_total_payout
        issuable_this_year += current_total_payout
        # every 180s
        living_time += 180 * 1000
        cnt += 1
        #print("total_left:{}".format(total_left))

    #print(cnt)
    #print("Total circulation:{} Total Remaining Issuable:{} year:{} Issuable this year:{} p:{} Inflation Rate:{}%\n".format(total_circulation_last_year, total_left_last_year, count, issuable_this_year, p, (issuable_this_year / total_circulation) * 100 ))
    f.write(
        "{} | {} | {} | {} | {} | {}% |\n".format(
            total_circulation_last_year/100_000_000, total_left_last_year/100_000_000, count, issuable_this_year/100_000_000, p,
            (issuable_this_year / total_circulation) * 100))
    total_circulation_last_year = total_circulation
    total_left_last_year = total_left
