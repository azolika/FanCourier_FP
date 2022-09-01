def e_interpreter(error_code):
    error_code = str(error_code)
    errors = {
        '-2': 'Unknown error',
        '-1': 'No error detected',
        '0': 'No error detected',
        '1': 'Server login failed - Invalid username or password',
        '2': 'OpenInterface not responding',
        '5': 'Successful login',
        '6': 'Invalid server_url . Pls. use http://xxx.xx/ format',
        '7': 'FTP ERROR - invalid FTP Address',
        '8': 'FTP ERROR - invalid User/Password',
        '9': 'FTP ERROR: 550 - Directory not found',
        '10': 'FTP ERROR: 550 - File not found'
    }
    try:
        errors[error_code]
    except KeyError:
        result = errors['2']
    else:
        result = errors[error_code]

    return result

