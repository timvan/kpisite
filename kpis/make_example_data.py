

kpi_titles = ["Coffees", "Swims in the Sea", "Surfing sessions", "Hours worked on project", "Km's ran", "Films watched"]
kpi_periodicities = ['WK', 'MH', 'MH', "DY", "WK", "YR"]
author = request.user
kpi_groups = ["RD", "BL", "BL", "GR", "BL", "RD"]
kpi_units = "times"

activity_amount_max = [2, 1, 1, 10, 15, 1]

today = datetime.today()

for i in len(kpi_titles):
	kpi = KPI(author = request.user, title = kpi_titles[i], units = kpi_units, periodicity = kpi_periodicities[i], group = kpi_groups)
	kpi.save()
	for i in range(random.randint(20, 150)):
		new_activity = Activity(kpi = kpi, activity_value = randint(0,activity_amount_max), datetime_logged = today - timedelta(random.randit(1, 365)))
		new_activity.save()
