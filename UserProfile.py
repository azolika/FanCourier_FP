class UserProfile:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.grp = ""
        self.TN = ""
        self.AO = ""
        self.I0 = ""
        self.M1 = ""

    def gr_to_grp(self, server_url, username, password, log_file_name, oi_log_file_name):
        from urllib.request import urlopen
        from urllib.error import URLError
        import time
        import sys
        from ErrorCodes import e_interpreter
        from LogWriter import log_writer
        from DeleteFile import delete_file

        clipar = ""

        self.username = username
        self.password = password
        restart_number, i = 0, 0
        gr_to_grp_oi_url = server_url + "exec.cgi?Gr=" + username + "&Pw=" + password + "&Xlat=txt/UsrTool.sql"
        log_writer(oi_log_file_name, gr_to_grp_oi_url, 0)
        while i < 1:
            try:
                data = urlopen(gr_to_grp_oi_url, timeout=60)
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
                #            client_data = data.read()
                file_object = open('client_data.txt', 'wb')
                file_object.write(data.read())
                file_object.close()
                file_object = open('client_data.txt', 'r', encoding="Windows-1250")
                while 1:
                    file_line = file_object.readline()
                    if file_line == "":
                        break
                    else:
                        if file_line[0:5] == "G.GRP":  # GRP
                            equal_sign_position = file_line.find("=")
                            self.grp = file_line[equal_sign_position + 2:].strip("\n")
                        if file_line[0:8] == "G.CLIPAR":
                            equal_sign_position = file_line.find("=")
                            clipar = file_line[equal_sign_position + 2:].strip("\n")

                point_position = clipar.find(":")
                comma_position = clipar.find(";")
                self.TN = clipar[point_position + 1:comma_position]
                clipar = clipar[comma_position + 1:]

                point_position = clipar.find(":")
                comma_position = clipar.find(";")
                self.AO = clipar[point_position + 1:comma_position]
                clipar = clipar[comma_position + 1:]

                point_position = clipar.find(":")
                comma_position = clipar.find(";")
                self.I0 = clipar[point_position + 1:comma_position]
                clipar = clipar[comma_position + 1:]

                point_position = clipar.find(":")
                self.M1 = clipar[point_position + 1:]

                file_object.close()
                delete_file('client_data.txt')
                return self
