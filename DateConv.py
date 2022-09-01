def to_rom_date(date_to_convert):
    import datetime
    week = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    date_to_convert = date_to_convert[8:10] + "/" + date_to_convert[5:7] + "/" + date_to_convert[0:4]
    date_to_convert1 = datetime.datetime.strptime(date_to_convert, '%d/%m/%Y')
    x = date_to_convert1.weekday()
    x = week[x]
    date_to_convert = str(date_to_convert)[:10] + " " + x
    return date_to_convert
