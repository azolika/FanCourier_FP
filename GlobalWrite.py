def global_write(global_data,
                 start_date, end_date,
                 filename, mode, cc,
                 log_file_name, signature, e_server, e_username, e_password, reply_to, send_email):

    import xlsxwriter
    from EmailSend import email_sent3
    from LogWriter import log_writer
    from DeleteFile import delete_file

    start = str(start_date)
    end = str(end_date)
    start = start[8:10] + "." + start[5:7] + "." + start[:4]
    end = end[8:10] + "." + end[5:7] + "." + end[:4]
    file_title = filename

    if mode == "week":
        filename = "Centralizator_saptamanal_" + filename
        file_title = "Centralizator saptamanal cont: " + file_title.upper()
    else:
        filename = "Centralizator_lunar_" + filename
        file_title = "Centralizator lunar cont: " + file_title.upper()

    # workbook add
    ff_name = filename + ".xlsx"
    workbook = xlsxwriter.Workbook(filename + ".xlsx", {'strings_to_numbers': True})
    worksheet = workbook.add_worksheet('Sheet1')
    worksheet.set_margins(left=0.75, right=0.75, top=0.75, bottom=0.75)

    arial_11_bold_center = workbook.add_format({'align': 'center', 'bold': 1})
    arial_11_bold_center.set_font_name('Arial')
    arial_11_bold_center.set_font_size(11)
    arial_11_bold_center.set_align('center')
    arial_11_bold_center.set_align('vcenter')
    arial_11_bold_center.set_border()
    arial_11_bold_center.set_border_color('#4D9FA2')

    arial_11_bold_center_wrap = workbook.add_format({'align': 'center', 'bold': 1})
    arial_11_bold_center_wrap.set_font_name('Arial')
    arial_11_bold_center_wrap.set_font_size(11)
    arial_11_bold_center_wrap.set_text_wrap()
    arial_11_bold_center_wrap.set_align('center')
    arial_11_bold_center_wrap.set_align('vcenter')
    arial_11_bold_center_wrap.set_border()
    arial_11_bold_center_wrap.set_border_color('#4D9FA2')

    calibri_16_bold_right = workbook.add_format({'align': 'center', 'bold': 1})
    calibri_16_bold_right.set_font_name('Calibri')
    calibri_16_bold_right.set_font_size(16)
    calibri_16_bold_right.set_align('left')
    calibri_16_bold_right.set_border()
    calibri_16_bold_right.set_border_color('#4D9FA2')

    arial_10_bold_center = workbook.add_format({'align': 'center', 'bold': 1})
    arial_10_bold_center.set_font_name('Arial')
    arial_10_bold_center.set_font_size(10)
    arial_10_bold_center.set_border()
    arial_10_bold_center.set_border_color('black')

    arial_10_left = workbook.add_format({'align': 'left'})
    arial_10_left.set_font_name('Arial')
    arial_10_left.set_font_size(10)
    arial_10_left.set_border()
    arial_10_left.set_border_color('black')

    arial_10_left_bold = workbook.add_format({'align': 'left', 'bold': 1})
    arial_10_left_bold.set_font_name('Arial')
    arial_10_left_bold.set_font_size(10)
    arial_10_left_bold.set_border()
    arial_10_left_bold.set_border_color('black')

    arial_11_left = workbook.add_format({'align': 'left', 'bold': 1})
    arial_11_left.set_font_name('Arial')
    arial_11_left.set_font_size(11)
    arial_11_left.set_border()
    arial_11_left.set_border_color('#4D9FA2')

    arial_10_right = workbook.add_format({'align': 'right'})
    arial_10_right.set_font_name('Arial')
    arial_10_right.set_font_size(10)
    arial_10_right.set_border()
    arial_10_right.set_border_color('black')

    arial_10_right_km = workbook.add_format({'align': 'right'})
    arial_10_right_km.set_font_name('Arial')
    arial_10_right_km.set_font_size(10)
    arial_10_right_km.set_num_format('0.0 km;-0.0 km;0.0 km')
    arial_10_right_km.set_border()
    arial_10_right_km.set_border_color('black')

    # merge
    worksheet.merge_range("A1:J1", "")

    # set column
    if mode == "week":
        worksheet.set_column('A:A', 21)
        worksheet.set_column('B:B', 21)
        worksheet.set_column('C:C', 19)
        worksheet.set_column('D:D', 19)
        worksheet.set_column('E:E', 19)
        worksheet.set_column('F:F', 19)
        worksheet.set_column('G:G', 19)
        worksheet.set_column('H:H', 19)
        worksheet.set_column('I:I', 19)
        worksheet.set_column('J:J', 19)
        worksheet.set_column('K:K', 24)
        worksheet.set_column('L:L', 24)
        worksheet.set_column('M:M', 24)
        worksheet.set_column('N:N', 40)
    else:
        worksheet.set_column('A:A', 21)
        worksheet.set_column('B:B', 21)
        worksheet.set_column('C:C', 19)
        worksheet.set_column('D:D', 19)
        worksheet.set_column('E:E', 19)
        worksheet.set_column('F:F', 19)
        worksheet.set_column('G:G', 19)
        worksheet.set_column('H:H', 19)
        worksheet.set_column('I:I', 24)
        worksheet.set_column('J:J', 24)
        worksheet.set_column('K:K', 24)
        worksheet.set_column('L:L', 40)
    # write week
    if mode == "week":
        worksheet.write("A1", file_title, calibri_16_bold_right)
        worksheet.write("A2", "Numar inmatriculare", arial_11_bold_center)
        worksheet.write("B2", "Nume", arial_11_bold_center)
        worksheet.write("C2", "Data inceput", arial_11_bold_center)
        worksheet.write("D2", "Data sfarsit", arial_11_bold_center)
        worksheet.write("E2", "Distanta parcursa", arial_11_bold_center)
        worksheet.write("F2", "Interes serviciu", arial_11_bold_center)
        worksheet.write("G2", "Interes privat", arial_11_bold_center)
        worksheet.write("H2", "KM Initial", arial_11_bold_center)
        worksheet.write("I2", "KM Final", arial_11_bold_center)
        worksheet.write("J2", "Limita aprobata", arial_11_bold_center)
        worksheet.write("K2", "Depasire limita", arial_11_bold_center)
        worksheet.write("L2", "Consum total", arial_11_bold_center)
        worksheet.write("M2", "Consum inters serviciu", arial_11_bold_center)
        worksheet.write("N2", "Consum inters privat", arial_11_bold_center)
    else:
        worksheet.write("A1", file_title, calibri_16_bold_right)
        worksheet.write("A2", "Numar inmatriculare", arial_11_bold_center)
        worksheet.write("B2", "Nume", arial_11_bold_center)
        worksheet.write("C2", "Distanta parcursa", arial_11_bold_center)
        worksheet.write("D2", "Interes serviciu", arial_11_bold_center)
        worksheet.write("E2", "Interes privat", arial_11_bold_center)
        worksheet.write("F2", "KM Initial", arial_11_bold_center)
        worksheet.write("G2", "KM Final", arial_11_bold_center)
        worksheet.write("H2", "Limita aprobata", arial_11_bold_center)
        worksheet.write("I2", "Depasire limita", arial_11_bold_center)
        worksheet.write("J2", "Consum total", arial_11_bold_center)
        worksheet.write("K2", "Consum inters serviciu", arial_11_bold_center)
        worksheet.write("L2", "Consum inters privat", arial_11_bold_center)

    i = 0
    while i < len(global_data.lpl):
        try:
            float(global_data.km_limit[i])
        except ValueError:
            km_limit = 0
        except TypeError:
            km_limit = 0
        else:
            km_limit = float(global_data.km_limit[i])

        try:
            float(global_data.km_prv[i])
        except ValueError:
            km_prv = 0
        except TypeError:
            km_prv = 0
        else:
            km_prv = float(global_data.km_prv[i])

        if km_limit - km_prv < 0:
            km_exceed = (km_limit - km_prv) * -1
        else:
            km_exceed = ""

        total_consumption = global_data.consumption_workday[i] + global_data.consumption_weekday[i]

        if mode == 'month':
            worksheet.write(i + 2, 0, global_data.lpl[i], arial_10_left)
            worksheet.write(i + 2, 1, global_data.driver_name[i], arial_10_left)
            worksheet.write(i + 2, 2, global_data.km_total[i], arial_10_left)
            worksheet.write(i + 2, 3, global_data.km_work[i], arial_10_left)
            worksheet.write(i + 2, 4, global_data.km_prv[i], arial_10_left)
            worksheet.write(i + 2, 5, global_data.km_start[i], arial_10_left)
            worksheet.write(i + 2, 6, global_data.km_end[i], arial_10_left)
            worksheet.write(i + 2, 7, km_limit, arial_10_left)
            worksheet.write(i + 2, 8, str(km_exceed), arial_10_left)
            worksheet.write(i + 2, 9, total_consumption, arial_10_left)
            worksheet.write(i + 2, 10, global_data.consumption_workday[i], arial_10_left)
            worksheet.write(i + 2, 11, global_data.consumption_weekday[i], arial_10_left)
            i = i+1
        else:
            worksheet.write(i + 2, 0, global_data.lpl[i], arial_10_left)
            worksheet.write(i + 2, 1, global_data.driver_name[i], arial_10_left)
            worksheet.write(i + 2, 2, start[:10], arial_10_left)
            worksheet.write(i + 2, 3, end[:10], arial_10_left)
            worksheet.write(i + 2, 4, global_data.km_total[i], arial_10_left)
            worksheet.write(i + 2, 5, global_data.km_work[i], arial_10_left)
            worksheet.write(i + 2, 6, global_data.km_prv[i], arial_10_left)
            worksheet.write(i + 2, 7, global_data.km_start[i], arial_10_left)
            worksheet.write(i + 2, 8, global_data.km_end[i], arial_10_left)
            worksheet.write(i + 2, 9, km_limit, arial_10_left)
            worksheet.write(i + 2, 10, str(km_exceed), arial_10_left)
            worksheet.write(i + 2, 11, total_consumption, arial_10_left)
            worksheet.write(i + 2, 12, global_data.consumption_workday[i], arial_10_left)
            worksheet.write(i + 2, 13, global_data.consumption_weekday[i], arial_10_left)
            i = i + 1
    workbook.close()
    if send_email == "1":
        email_sent3(cc, ff_name, log_file_name, signature, mode, e_server, e_username, e_password, reply_to)
        log_writer(log_file_name, "Summary report sent", 1)
        delete_file(ff_name)
    log_writer(log_file_name, "Summary report generated: " + ff_name, 1)


