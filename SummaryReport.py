class SummaryReport:
    def __init__(self):
        self.lpl = []
        self.driver_name = []
        self.km_start = []
        self.km_end = []
        self.km_total = []
        self.km_work = []
        self.km_prv = []
        self.km_limit = []
        self.consumption_workday = []
        self.consumption_weekday = []

    def sum_data(self, lpl, driver_name, km_start, km_work, km_prv, km_limit, consumption_workday, consumption_weekday):
        self.lpl.append(lpl)
        self.driver_name.append(driver_name)
        self.km_start.append(km_start)
        self.km_work.append(km_work)
        self.km_prv.append(km_prv)

        if km_start == "":
            km_start = 0
        if km_work == "":
            km_work = 0
        if km_prv == "":
            km_prv = 0

        self.km_end.append(float(km_work) + float(km_prv) + float(km_start))
        self.km_total.append(float(km_work) + float(km_prv))
        self.km_limit.append(km_limit)
        self.consumption_workday.append(consumption_workday)
        self.consumption_weekday.append(consumption_weekday)
