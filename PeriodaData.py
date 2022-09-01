class PeriodData:
    def __init__(self):
        self.weekend_distance = 0
        self.workday_distance = 0
        self.weekend_consumption = 0
        self.workday_consumption = 0

    def get_period_data(self, server_url, username, password, car_id, log_file_name,
                        oi_log_file_name, slo, shi, wkmm1, week_sign, distance):
        from urllib.request import urlopen
        from urllib.error import URLError
        import time
        import sys
        from ErrorCodes import e_interpreter
        from LogWriter import log_writer
        from DeleteFile import delete_file

        i = 0
        if slo[i] != shi[i]:
            while i < len(slo):
                url = server_url + "avlw.cgi?Gr=" \
                      + username + "&Lang=hu&Big=&Pw=" \
                      + password + "&Xlat=WayWork.htm&Par0=Work%3ACar&Par1=&Par2=&Con=txt&C=" \
                      + car_id + "&SLo=" \
                      + str(slo[i]) + "&SHi=" \
                      + str(shi[i]) + "&TN=3&AO=1&I0=1&FPoi=&F=&L=04+_" \
                                      "+WayWork.htm%26Work%3ACar&CG=&CD=&LenA0=0.001&LenM1=" \
                      + str(wkmm1) + "&Drv=0&Home="
                log_writer(oi_log_file_name, url, 0)
                restart_number = 0

                while restart_number < 5:
                    try:
                        url_response = urlopen(url, timeout=120)

                    except URLError:
                        restart_number = restart_number + 1
                        log_writer(log_file_name, e_interpreter(2), 1)
                        log_writer(log_file_name, "Waiting " + str(restart_number * 10) + " sec", 1)
                        time.sleep(restart_number * 10)
                        log_writer(log_file_name, "Restarting process. " +
                                   str(6 - restart_number) + " attempts remain", 1)
                        if restart_number == 5:
                            log_writer(log_file_name, "Critical error", 1)
                            sys.exit("Critical Error")

                    else:
                        restart_number = 5
                        file_object = open('partialM.txt', 'wb')
                        file_object.write(url_response.read())
                        file_object.close()
                        file_object = open('partialM.txt', 'r', encoding="Windows-1250")
                        while 1:
                            text = file_object.readline()
                            if text == "":
                                break
                            else:
                                if text.find("|Összesen|") != -1 and text.find("|Nappal|") == -1:
                                    t = 0
                                    while t < 5:
                                        text = text[text.find("|") + 1:]
                                        t = t + 1
                                    gps_temp = text[:text.find("|")]
                                    text = text[text.find("|") + 1:]
                                    text = text[text.find("|") + 1:]
                                    can_temp = text[:text.find("|")]

                                    if can_temp == "0.0":
                                        temp = gps_temp
                                    else:
                                        temp = can_temp
                                    t = 0
                                    while t < 8:
                                        text = text[text.find("|") + 1:]
                                        t = t + 1
                                    fuel_level_consumption_temp = text[:text.find("|")]
                                    t = 0
                                    while t < 6:
                                        text = text[text.find("|") + 1:]
                                        t = t + 1
                                    can_consumption_temp = text[:text.find("|")]

                                    if fuel_level_consumption_temp == "0.0":
                                        fuel_temp = fuel_level_consumption_temp
                                    else:
                                        fuel_temp = can_consumption_temp

                                    if fuel_temp == "":
                                        fuel_temp = 0

                                    try:
                                        fuel_temp = float(fuel_temp)
                                    except ValueError:
                                        fuel_temp = 0
                                    else:
                                        fuel_temp = float(fuel_temp)

                                    if week_sign[i] == "NW":
                                        self.workday_distance = self.workday_distance + float(temp)
                                        self.workday_consumption = self.workday_consumption + float(fuel_temp)
                                    else:
                                        self.weekend_consumption = self.weekend_consumption + float(fuel_temp)
                                    break
                        file_object.close()
                        delete_file('partialM.txt')
                        self.weekend_distance = float(distance[-3]) - self.workday_distance
                i = i + 1
