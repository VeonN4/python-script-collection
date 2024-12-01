import datetime

startDate = input("Masukan tanggal ke-1 (dd-mm-yyy): ")
endDate = input("Masukan tanggal ke-2 (dd-mm-yyy): ")
days = 0

start = datetime.datetime.strptime("{}".format(startDate), "%d-%m-%Y")
end = datetime.datetime.strptime("{}".format(endDate), "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days += 1

print(f"Dari {startDate} ke {endDate} membutuhkan {days} hari")