class IniReader:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.server_url = ""
        self.log_file_name = ""
        self.oi_log_file_name = ""
        self.ftp_adr = ""
        self.ftp_username = ""
        self.ftp_password = ""
        self.ftp_folder = ""
        self.ftp_file = ""
        self.email_subject = ""
        self.email_title = ""
        self.email_body1 = ""
        self.email_body2 = ""
        self.email_cc = []
        self.signature = ""
        self.mode = ""
        self.error = ""
        self.weekend_start = ""
        self.weekend_end = ""
        self.email_help = []
        self.email_signature = ""
        self.email_server = ""
        self.email_username = ""
        self.email_password = ""
        self.email_reply_to = ""
        self.driver = None
        self.summary = None

    def ini_reader(self, filename):
        import configparser
        config = configparser.ConfigParser()
        config.read(filename)

        self.username = config.get("USER", "username")
        self.password = config.get("USER", "password")
        self.server_url = config.get("ENVIRONMENT", "server_url")
        self.log_file_name = config.get("ENVIRONMENT", "log_file_name")
        self.oi_log_file_name = config.get("ENVIRONMENT", "oi_log_file_name")
        self.ftp_adr = config.get("FTP", "ftp_adr")
        self.ftp_username = config.get("FTP", "ftp_username")
        self.ftp_password = config.get("FTP", "ftp_password")
        self.ftp_folder = config.get("FTP", "ftp_folder")
        self.ftp_file = config.get("FTP", "ftp_file")
        self.email_subject = config.get("MESSAGE", "subject")
        self.email_body1 = config.get("MESSAGE", "body1")
        self.email_body2 = config.get("MESSAGE", "body2")
        self.email_title = config.get("MESSAGE", "title")
        self.email_signature = config.get("MESSAGE", "signature")
        cc = config.get("MESSAGE", "cc")
        self.email_cc.append(cc.split(";"))
        help_mail = config.get("MESSAGE", "help")
        self.email_help.append(help_mail.split(";"))
        self.mode = config.get("MODE", "mode")
        self.weekend_start = config.get("ENVIRONMENT", "weekend_start")
        self.weekend_end = config.get("ENVIRONMENT", "weekend_end")
        self.email_server = config.get("MAIL", "server")
        self.email_username = config.get("MAIL", "username")
        self.email_password = config.get("MAIL", "password")
        self.email_reply_to = config.get("MAIL", "reply_to")
        self.driver = config.get("MAIL", "driver")
        self.summary = config.get("MAIL", "summary")

    def ini_test(self):
        if self.server_url.strip("\n")[-1:] != '/':
            self.error = 6
