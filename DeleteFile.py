import os


def delete_file(file_name):
    try:
        os.remove(file_name)
    except:
        pass
