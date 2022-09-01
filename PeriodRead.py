class ReportPeriods:
    def __init__(self):
        self.SLo = []
        self.SHi = []
        self.weekend = []
        self.full_slo = ""
        self.full_shi = ""

    def auto_period(self, mode, weekend_start, weekend_end):
        from datetime import date, timedelta

        if mode == 'week':
            running_date = date.today()
            running_day = running_date.isoweekday()
            first_day = running_date - timedelta(days=running_day + 6)
            last_day = running_date - timedelta(days=running_day)
            friday = first_day + timedelta(days=4)

            self.SLo.append(str(first_day) + "+" + "00:00:00")
            self.SHi.append(str(first_day) + "+" + weekend_end)
            self.weekend.append("W")

            self.SLo.append(str(first_day) + "+" + weekend_end)
            self.SHi.append(str(friday) + "+" + weekend_start)
            self.weekend.append("NW")

            self.SLo.append(str(friday) + "+" + weekend_start)
            self.SHi.append(str(last_day) + "+" + "23:59:59")
            self.weekend.append("W")

        else:
            running_date = date.today()
            # running_date = date(2021,9,1)
            running_date = running_date.replace(day=1)
            last_day = running_date + timedelta(days=-1)
            first_day = last_day.replace(day=1)
            if first_day.isoweekday() <= 5:

                friday = first_day + timedelta(days=5 - first_day.isoweekday())
                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)

                self.SLo.append(str(first_day) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)

                if monday == last_day:
                    self.SLo.append(str(monday) + "+" + "00:00:00")
                    self.SHi.append(str(monday) + "+" + "23:59:59")
                    self.weekend.append("NW")
                else:
                        if friday > last_day:
                            if monday <= last_day:
                                self.SLo.append(str(monday) + "+" + "00:00:00")
                                self.SHi.append(str(last_day) + "+" + "23:59:59")
                                self.weekend.append("NW")
                        else:
                            self.SLo.append(str(monday) + "+" + "00:00:00")
                            self.SHi.append(str(friday) + "+" + "23:59:59")
                            self.weekend.append("NW")

                            saturday = friday + timedelta(days=1)
                            sunday = saturday + timedelta(days=1)
                            if saturday <= last_day:
                                if sunday <= last_day:
                                    self.SLo.append(str(saturday) + "+" + "00:00:00")
                                    self.SHi.append(str(sunday) + "+" + "23:59:59")
                                    self.weekend.append("W")
                                else:
                                    self.SLo.append(str(saturday) + "+" + "00:00:00")
                                    self.SHi.append(str(last_day) + "+" + "23:59:59")
                                    self.weekend.append("W")
            else:
                sunday = first_day + timedelta(days=7 - first_day.isoweekday())
                self.SLo.append(str(first_day) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = monday + timedelta(days=4)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                self.SLo.append(str(saturday) + "+" + "00:00:00")
                self.SHi.append(str(sunday) + "+" + "23:59:59")
                self.weekend.append("W")

                monday = sunday + timedelta(days=1)
                friday = friday + timedelta(days=7)
                self.SLo.append(str(monday) + "+" + "00:00:00")
                self.SHi.append(str(friday) + "+" + "23:59:59")
                self.weekend.append("NW")

                saturday = friday + timedelta(days=1)
                sunday = saturday + timedelta(days=1)
                if saturday == last_day:
                    self.SLo.append(str(saturday) + "+" + "00:00:00")
                    self.SHi.append(str(saturday) + "+" + "23:59:59")
                    self.weekend.append("W")
                else:
                    if sunday > last_day:
                        self.SLo.append(str(saturday) + "+" + "00:00:00")
                        self.SHi.append(str(last_day) + "+" + "23:59:59")
                        self.weekend.append("W")
                    else:
                        self.SLo.append(str(saturday) + "+" + "00:00:00")
                        self.SHi.append(str(sunday) + "+" + "23:59:59")
                        self.weekend.append("W")

                        monday = sunday + timedelta(days=1)
                        friday = friday + timedelta(days=7)
                        if monday <= last_day:
                            if friday < last_day:
                                self.SLo.append(str(monday) + "+" + "00:00:00")
                                self.SHi.append(str(friday) + "+" + "23:59:59")
                                self.weekend.append("NW")
                            else:
                                self.SLo.append(str(monday) + "+" + "00:00:00")
                                self.SHi.append(str(last_day) + "+" + "23:59:59")
                                self.weekend.append("NW")
        self.full_slo = self.SLo[0]
        self.full_shi = self.SHi[-1]
