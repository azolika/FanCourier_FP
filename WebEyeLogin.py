def webeye_login(server_url, username, password, log_file_name):
    from urllib.error import URLError
    from urllib.request import urlopen
    from datetime import datetime
    from LogWriter import log_writer

    login_url = server_url + "exec.cgi?Gr=" + username + "&Pw=" + password + "&Xlat=txt/si.txt"
    log_writer(log_file_name, login_url, 0)
    try:
        login_response = urlopen(login_url, timeout=120)
    except URLError:
        login_date = 0
        error_code = 0
    else:
        login_date = login_response.read()

        try:
            int(login_date)
        except ValueError:
            login_date = 0
            error_code = 1
        else:
            login_date = int(login_date)
            login_date = datetime.utcfromtimestamp(login_date).strftime('%Y-%m-%d %H:%M:%S')
            error_code = 5
    return login_date, error_code
