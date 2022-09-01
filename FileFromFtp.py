def file_from_ftp(ip, username, password, path, filename):
    import ftplib
    try:
        ftp = ftplib.FTP(ip)
    except:
        return 7
    else:
        try:
            ftp.login(username, password)
        except ftplib.error_perm:
            return 8
        else:
            try:
                ftp.cwd(path)
            except ftplib.error_perm:
                return 9
            else:
                try:
                    ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
                except ftplib.error_perm:
                    return 10
                else:
                    ftp.quit()
                    return 1
