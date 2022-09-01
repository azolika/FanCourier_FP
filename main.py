import sys
from CarList import CarList
from FanCourierExcelReader import FanCourierTo
from IniReader import IniReader
from ErrorCodes import e_interpreter
from UserProfile import UserProfile
from WebEyeLogin import webeye_login
from LogWriter import log_writer
from FileFromFtp import file_from_ftp
from FullPeriodData import FullPeriodData
from ReportWrite import excel_writer
from PeriodaData import PeriodData
from Odometer import Odometer
from SummaryReport import SummaryReport
from GlobalWrite import global_write
from EmailSend import email_sent, email_sent2
from PeriodRead import ReportPeriods
from DeleteFile import delete_file

# Global report
summary_report = SummaryReport()
# READ REPORT PARAM FROM INI#

environment = IniReader()
environment.ini_reader("AReport.ini")
environment.ini_test()

# ENVIRONMENT TEST
if environment.error != "":
    e_interpreter(environment.error)
    sys.exit(e_interpreter(environment.error))

# WebEye Login with environment parameters #

login = webeye_login(environment.server_url,
                     environment.username,
                     environment.password,
                     environment.oi_log_file_name)
# LOGIN TEST #
if login[1] != 5:
    log_writer(environment.log_file_name,
               e_interpreter(login[1]), 1)
    sys.exit(e_interpreter(environment.error))

# GET FILE FROM FTP
ftp_file = file_from_ftp(environment.ftp_adr,
                         environment.ftp_username,
                         environment.ftp_password,
                         environment.ftp_folder,
                         environment.ftp_file)

if ftp_file != 1:
    log_writer(environment.log_file_name,
               e_interpreter(ftp_file),
               1)
    sys.exit()

# Period read
report_period = ReportPeriods()
report_period.auto_period(environment.mode,
                          environment.weekend_start,
                          environment.weekend_end)

# GET USER PROFILE
user_profile = UserProfile()
user_profile.gr_to_grp(environment.server_url,
                       environment.username,
                       environment.password,
                       environment.log_file_name,
                       environment.oi_log_file_name)

# GET CAR LIST

car_list_webeye = CarList()
car_list_webeye.car_list(environment.server_url,
                         environment.username,
                         environment.password,
                         user_profile.grp,
                         environment.log_file_name,
                         environment.oi_log_file_name)

# EXCEL DATA READ

recip = FanCourierTo()
recip.excel_reader(environment.ftp_file,
                   car_list_webeye,
                   environment.log_file_name)

i = 0
delete_file(environment.ftp_file)
invalid_car_id = []
while i < len(recip.mail_address):
    try:
        int(recip.webeye_car_id[i])
    except ValueError:
        log_writer(environment.log_file_name, recip.webeye_car_id[i] + "--> NOT FOUND", 1)
        invalid_car_id.append(recip.webeye_car_id[i])
    else:
        log_writer(environment.log_file_name, recip.lpl_plate[i] + "--> START", 1)
        full_period_data = FullPeriodData()
        full_period_data.get_full_period_data(environment.server_url,
                                              environment.username,
                                              environment.password,
                                              recip.webeye_car_id[i],
                                              environment.log_file_name,
                                              environment.oi_log_file_name,
                                              report_period.full_slo,
                                              report_period.full_shi,
                                              recip.wkmm1[i])
        partial_period_data = PeriodData()
        partial_period_data.get_period_data(environment.server_url,
                                            environment.username,
                                            environment.password,
                                            recip.webeye_car_id[i],
                                            environment.log_file_name,
                                            environment.oi_log_file_name,
                                            report_period.SLo,
                                            report_period.SHi,
                                            recip.wkmm1[i],
                                            report_period.weekend,
                                            full_period_data.distance)

        km = Odometer()
        km.odometer_km(environment.server_url,
                       environment.username,
                       environment.password,
                       recip.webeye_car_id[i],
                       report_period.full_slo,
                       report_period.full_shi,
                       environment.oi_log_file_name,
                       environment.log_file_name)

        excel_writer(recip.lpl_plate[i] + ".xlsx",
                     len(full_period_data.day_date) - 3,
                     recip.lpl_plate[i],
                     report_period.full_slo,
                     report_period.full_shi,
                     recip.real_name[i],
                     full_period_data.day_date,
                     full_period_data.start,
                     full_period_data.end,
                     full_period_data.distance,
                     partial_period_data.workday_distance,
                     environment.weekend_start,
                     environment.weekend_end,
                     km.start_km)

        summary_report.sum_data(recip.lpl_plate[i],
                                recip.real_name[i],
                                km.start_km,
                                partial_period_data.workday_distance,
                                partial_period_data.weekend_distance,
                                recip.km_limit[i],
                                partial_period_data.workday_consumption,
                                partial_period_data.weekend_consumption)
        if environment.driver == '1':
            email_sent(recip.mail_address[i],
                       environment.email_subject,
                       environment.email_title,
                       environment.email_body1,
                       environment.email_body2,
                       recip.lpl_plate[i] + ".xlsx",
                       environment.log_file_name,
                       environment.email_signature,
                       environment.email_cc[0],
                       environment.email_server,
                       environment.email_username,
                       environment.email_password,
                       environment.email_reply_to)

        delete_file(recip.lpl_plate[i] + ".xlsx")

        log_writer(environment.log_file_name, recip.lpl_plate[i] + "--> END", 1)
    i = i + 1
if len(summary_report.lpl) > 0:
    global_write(summary_report,
                 report_period.full_slo,
                 report_period.full_shi,
                 environment.ftp_file[:-5],
                 environment.mode,
                 environment.email_cc[0],
                 environment.log_file_name,
                 environment.signature,
                 environment.email_server,
                 environment.email_username,
                 environment.email_password,
                 environment.email_reply_to,
                 environment.summary)
invalid_car_text = ""
for car in invalid_car_id:
    invalid_car_text = invalid_car_text + "<br>" + car
email_sent2(environment.email_help[0],
            environment.log_file_name,
            environment.signature,
            environment.mode,
            environment.email_server,
            environment.email_username,
            environment.email_password,
            invalid_car_text)
# clean
delete_file(environment.ftp_file)
