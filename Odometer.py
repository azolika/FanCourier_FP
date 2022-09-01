class Odometer:
    def __init__(self):
        self.start_km = ""

    def odometer_km(self, server_url, username, password, car_id, slo, shi, oi_log_file_name, log_file_name):
        from urllib.request import urlopen
        from urllib.error import URLError
        import time
        import sys
        from ErrorCodes import e_interpreter
        from LogWriter import log_writer
        from DeleteFile import delete_file

        url = server_url + "avlw.cgi?Gr=" \
              + username + "&Lang=hu&Big=&Pw=" \
              + password + "&Xlat=&Par0=&Par1=&Par2=&Con=wex&C=" \
              + car_id + "&SLo=" \
              + str(slo) + "&SHi=" \
              + str(shi) + "TN=3&AO=1&I0=1&FPoi=&F=&L=01&CG=&CD=&L" \
                           "enA0=0.001&LenM1=1&Drv=0&Home="
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
                file_object = open('CANkm.txt', 'wb')
                file_object.write(url_response.read())
                file_object.close()
                file_object = open('CANkm.txt', 'r', encoding="Windows-1250")
                next_tag = 0

                while 1:
                    text = file_object.readline()

                    if text == "":
                        break
                    else:
                        if text == "<CName>Megtett út</CName>\n":
                            next_tag = "CVal1"
                        if next_tag == "CVal1" and text == "<Can7>\n":
                            next_tag = ""
                        if next_tag == "CVal1" and text[:7] == "<CVal1>":
                            self.start_km = str(round(float(text[7:-9]), 2))
                            break
                file_object.close()
                delete_file('CANkm.txt')
