from datetime import date, datetime, timedelta


now = datetime.now()

start_date = now
end_date = datetime(now.year, now.month, 1)

for i in range(1,25):
	print(start_date.month, "  |  ", start_date, "  |  ", end_date)
	start_date = end_date - timedelta(microseconds = 1)
	if (12 + now.month - i) % 12 == 0:
		end_date = datetime(end_date.year - 1, 12, 1)
	else:
		end_date = datetime(end_date.year, (12 + end_date.month - 1) % 12, 1)