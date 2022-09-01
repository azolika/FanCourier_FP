def log_writer(log_file_name, log_message, debug_print):
    from datetime import datetime

    log_tim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_object = open(log_file_name, 'a')
    file_object.write(str(log_tim) + "|" + log_message + "\n")
    if debug_print == 1:
        print(str(log_tim) + "|" + log_message)
    file_object.close()
