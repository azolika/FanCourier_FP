class FullPeriodData:
    def __init__(self):
        self.day_date = []
        self.start = []
        self.end = []
        self.distance = []

    def get_full_period_data(self, server_url, username, password,
                             car_id, log_file_name, oi_log_file_name, slo, shi, wkmm1):
        from urllib.request import urlopen
        from urllib.error import URLError
        import time
        import sys
        from ErrorCodes import e_interpreter
        from LogWriter import log_writer
        from DeleteFile import delete_file

        url = server_url + "avlw.cgi?Gr="\
              + username + "&Lang=hu&Big=&Pw="\
              + password + "&Xlat=WayWork.htm&Par0=Work%3ACar&Par1=&Par2=&Con=txt&C="\
              + car_id + "&SLo="\
              + str(slo) + "&SHi="\
              + str(shi) + "&TN=3&AO=1&I0=1&FPoi=&F=&L=04+_+WayWork.htm%26Work%3ACar&CG=&CD=&LenA0=0.001&LenM1="\
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
                log_writer(log_file_name, "Restarting process. " + str(6 - restart_number) + " attempts remain", 1)
                if restart_number == 5:
                    log_writer(log_file_name, "Critical error", 1)
                    sys.exit("Critical Error")

            else:
                restart_number = 5
                file_object = open('fullM.txt', 'wb')
                file_object.write(url_response.read())
                file_object.close()
                file_object = open('fullM.txt', 'r', encoding="Windows-1250")
                while 1:
                    text = file_object.readline()
                    if text == "":
                        break
                    else:
                        if text[:1] == "_":
                            pass
                        else:
                            text = text[text.find("|") + 1:]
                            text = text[text.find("|") + 1:]
                            self.day_date.append(text[:text.find("|")])
                            text = text[text.find("|") + 1:]
                            self.start.append(text[:text.find("|")])
                            text = text[text.find("|") + 1:]
                            self.end.append(text[:text.find("|")])
                            text = text[text.find("|") + 1:]
                            gps_distance = text[:text.find("|")]
                            text = text[text.find("|") + 1:]
                            text = text[text.find("|") + 1:]
                            can_distance = text[:text.find("|")]

                            if can_distance == "0.0":
                                self.distance.append(gps_distance)
                            else:
                                self.distance.append(can_distance)
                file_object.close()
                delete_file('fullM.txt')
