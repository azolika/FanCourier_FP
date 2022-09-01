from urllib.error import URLError
from urllib.request import urlopen
from LogWriter import log_writer
from DeleteFile import delete_file
import sys


class CarList:
    def __init__(self):
        self.car = []
        self.lpl = []
        self.lpl_clear = []
        self.dam = []
        self.str00 = []
        self.str01 = []
        self.str02 = []
        self.wkmm1 = []
        self.timaxv = []
        self.wvhnrm = []
        self.nam = []
        self.pwd = []
        self.tim = []
        self.tm2 = []
        self.sms = []
        self.tst = []
        self.cgr = []
        self.poi = []
        self.wstat = []
        self.wname = []
        self.ipp = []
        self.can_km = []

    def car_list(self, server_url, username, password, group_id, log_file_name, oi_log_file_name):
        oi_url = server_url + "brw.cgi?Gr=" + username + "&Pw=" + password + "&Lang=ro&T=Grc&Con=txt&MK" \
                                                                             "=Grp&MV=" + group_id + "&Q=a&txthead=1"
        log_writer(oi_log_file_name, oi_url, 0)
        log_writer(log_file_name, "Vehicle list download start", 1)
        restart_number = 0
        while restart_number < 5:
            try:
                f = urlopen(oi_url, timeout=180)
            except URLError:
                restart_number = restart_number + 1
                if restart_number < 5:
                    log_writer(log_file_name, "URL error or timeout", 1)
                else:
                    sys.exit()
            else:
                restart_number = 5
                file_object = open('car_list', 'wb')
                file_object.write(f.read())
                file_object.close()
                file_object = open('car_list', 'r')
                while 1:
                    line = file_object.readline()
                    if line == "":
                        break
                    else:
                        if line[0] != "_":
                            live_car_wstat = line.find("Abonat")
                            if live_car_wstat != -1:
                                line = line[line.find("|") + 1:]
                                local_car = line[:line.find("|")]
                                self.car.append(local_car)
                                line = line[line.find("|") + 1:]
                                self.lpl.append(line[:line.find("|")])
                                temp_lpl = line[:line.find("|")]
                                self.lpl_clear.append(temp_lpl.replace("-", ""))
                                line = line[line.find("|") + 1:]
                                self.dam.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.str00.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.str01.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.str02.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                wkmm1 = (line[:line.find("|")])
                                if wkmm1 == '0.000000':
                                    wkmm1 = '-1'
                                self.wkmm1.append(wkmm1)
                                line = line[line.find("|") + 1:]
                                self.timaxv.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.wvhnrm.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.nam.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.pwd.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.tim.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.tm2.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.sms.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.tst.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.cgr.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.poi.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.ipp.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.wstat.append(line[:line.find("|")])
                                line = line[line.find("|") + 1:]
                                self.wname.append(line[:line.find("|")])
                file_object.close()
                delete_file("car_list")
                log_writer(log_file_name, "Vehicle list download end", 1)
