from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from LogWriter import log_writer


def email_sent(to_addr,
               subject,
               title,
               body1, body2,
               filename,
               log_file_name,
               signature, cc,
               e_server, e_username, e_password,
               reply_to):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'WebEye AReport <areport@ro.webeye.eu>'
    msg['Reply-to'] = reply_to
    to_addr_string = ""
    i = 0
    while i < len(to_addr):
        if i == 0:
            to_addr_string = to_addr[i]
        else:
            to_addr_string = to_addr_string + "," + cc[i]
        i = i + 1
    msg['To'] = to_addr_string

    cc_string = ""
    i = 0
    while i < len(cc):
        if i == 0:
            cc_string = cc[i]
        else:
            cc_string = cc_string + "," + cc[i]
        i = i + 1
    msg['Cc'] = cc_string

    msg.preamble = 'Multipart massage.\n'

    html = "<html><head></head><body>"
    html = html + '<p><b><font face="poppins"color="black">' + title + '</font></b></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + body1 + '</font></p>'
    html = html + '<p><font face="poppins"color="black">' + body2 + '</font></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + signature + '</font></p>'
    html = html + "</body></html>"

    part = MIMEText(html, 'html')
    msg.attach(part)
    part = MIMEApplication(open(str(filename), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)
    server = smtplib.SMTP(e_server)
    server.ehlo()
    server.starttls()
    server.login(e_username, e_password)

    i = 0
    while i < len(to_addr):
        server.sendmail(msg['From'], to_addr[i], msg.as_string())
        log_writer(log_file_name, "Email sent To:" + to_addr[i], 1)
        i = i + 1

    i = 0
    while i < len(cc):
        server.sendmail(msg['From'], cc[i], msg.as_string())
        log_writer(log_file_name, "Email sent CC:" + cc[i], 1)
        i = i + 1


def email_sent3(to_addr, filename, log_file_name, signature, mode, e_server, e_username, e_password, reply_to):
    if mode == "week":
        subject = "Raport centralizator cont OFFCIE"
    else:
        subject = "Raport centralizator cont MANAGER"

    title = 'Buna ziua!'
    body1 = subject
    body2 = ""

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'WebEye AReport <areport@ro.webeye.eu>'
    msg['Reply-to'] = reply_to
    to_addr_string = ""
    i = 0
    while i < len(to_addr):
        if i == 0:
            to_addr_string = to_addr[i]
        else:
            to_addr_string = to_addr_string + "," + to_addr[i]
        i = i + 1
    msg['To'] = to_addr_string

    cc_string = ""

    msg['Cc'] = cc_string
    msg.preamble = 'Multipart massage.\n'

    html = "<html><head></head><body>"
    html = html + '<p><b><font face="poppins"color="black">' + title + '</font></b></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + body1 + '</font></p>'
    html = html + '<p><font face="poppins"color="black">' + body2 + '</font></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + signature + '</font></p>'
    html = html + "</body></html>"

    part = MIMEText(html, 'html')
    msg.attach(part)
    part = MIMEApplication(open(str(filename), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)
    server = smtplib.SMTP(e_server)
    server.ehlo()
    server.starttls()
    server.login(e_username, e_password)

    i = 0
    while i < len(to_addr):
        server.sendmail(msg['From'], to_addr[i], msg.as_string())
        log_writer(log_file_name, 'Email sent to:' + str(to_addr[i]), 1)
        i = i + 1


def email_sent2(to_addr, log_file_name, signature, mode, e_server, e_username, e_password, vehicle_list):
    if mode == "week":
        subject = "Vechicule neraportate cont OFFCIE"
    else:
        subject = "Vechicule neraportate cont MANAGER"

    title = 'Buna ziua!'
    body1 = subject
    body2 = vehicle_list

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'WebEye AReport <areport@ro.webeye.eu>'
    msg['Reply-to'] = 'areport@ro.webeye.eu'
    to_addr_string = ""
    i = 0
    while i < len(to_addr):
        if i == 0:
            to_addr_string = to_addr[i]
        else:
            to_addr_string = to_addr_string + "," + to_addr[i]
        i = i + 1
    msg['To'] = to_addr_string

    cc_string = ""

    msg['Cc'] = cc_string
    msg.preamble = 'Multipart massage.\n'

    html = "<html><head></head><body>"
    html = html + '<p><b><font face="poppins"color="black">' + title + '</font></b></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + body1 + '</font></p>'
    html = html + '<p><font face="poppins"color="black">' + body2 + '</font></p>'
    html = html + "<br>"
    html = html + '<p><font face="poppins"color="black">' + signature + '</font></p>'
    html = html + "</body></html>"

    part = MIMEText(html, 'html')
    msg.attach(part)
    server = smtplib.SMTP(e_server)
    server.ehlo()
    server.starttls()
    server.login(e_username, e_password)

    i = 0
    while i < len(to_addr):
        server.sendmail(msg['From'], to_addr[i], msg.as_string())
        log_writer(log_file_name, 'Invalid Lpl sent to:' + str(to_addr[i]), 1)
        i = i + 1
