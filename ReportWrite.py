def excel_writer(filename, number_of_reported_day, lpl, start, end, name,
                 day_day, day_start, day_end, day_dist, work, weekend_start, weekend_end,
                 km_start):
    import xlsxwriter
    from DateConv import to_rom_date
    # conversions
    start = str(start)
    end = str(end)

    # workbook add
    workbook = xlsxwriter.Workbook(filename, {'strings_to_numbers': True})
    worksheet = workbook.add_worksheet('Sheet1')
    worksheet.set_margins(left=0.75, right=0.75, top=0.75, bottom=0.75)

    # format
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

    calibri_16_bold_center = workbook.add_format({'align': 'center', 'bold': 1})
    calibri_16_bold_center.set_font_name('Calibri')
    calibri_16_bold_center.set_font_size(16)
    calibri_16_bold_center.set_align('center')
    calibri_16_bold_center.set_align('vcenter')
    calibri_16_bold_center.set_border()
    calibri_16_bold_center.set_border_color('#4D9FA2')

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

    #   merge
    worksheet.merge_range("A1:F1", "")
    worksheet.merge_range("A2:F2", "")
    worksheet.merge_range('A3:F3', '')
    worksheet.merge_range('A4:B4', '')
    worksheet.merge_range('C4:D4', '')
    worksheet.merge_range('E4:F4', '')
    worksheet.merge_range('A6:A7', '')
    worksheet.merge_range('B6:F6', '')
    worksheet.merge_range('D7:E7', '')

    #   set column
    worksheet.set_column('A:A', 20.56)
    worksheet.set_column('B:B', 11.78)
    worksheet.set_column('C:C', 9.78)
    worksheet.set_column('D:D', 12.67)
    worksheet.set_column('E:E', 5.78)
    worksheet.set_column('F:F', 16.89)
    worksheet.set_column('G:G', 12)

    # set row
    worksheet.set_row(0, 42.0)
    worksheet.set_row(1, 7.2)
    worksheet.set_row(2, 24.6)
    worksheet.set_row(3, 49.8)
    worksheet.set_row(4, 13.8)
    worksheet.set_row(5, 15)
    worksheet.set_row(5, 13.8)
    i = 0
    while i < number_of_reported_day + 6:
        worksheet.set_row(5 + i, 13.8)
        i = i + 1

    # image
    worksheet.insert_image('A1', "resources/FC.png", {'x_scale': 0.9, 'y_scale': 0.9})
    worksheet.insert_image('F1', "resources/WElogo", {'x_scale': 0.75, 'y_scale': 0.75})
    # write
    worksheet.write("A3", "", calibri_16_bold_center)
    worksheet.write("B3", "", calibri_16_bold_center)
    worksheet.write("B4", "", calibri_16_bold_center)
    worksheet.write("D4", "", calibri_16_bold_center)
    worksheet.write("C3", "", calibri_16_bold_center)
    worksheet.write("D3", "", calibri_16_bold_center)
    worksheet.write("E3", "", calibri_16_bold_center)
    worksheet.write("F3", "", calibri_16_bold_center)
    worksheet.write("F4", "", calibri_16_bold_center)
    worksheet.write("C6", "", calibri_16_bold_center)
    worksheet.write("D6", "", calibri_16_bold_center)
    worksheet.write("E6", "", calibri_16_bold_center)
    worksheet.write("F6", "", calibri_16_bold_center)
    worksheet.write("A6", "", calibri_16_bold_center)
    worksheet.write("A7", "", calibri_16_bold_center)
    worksheet.write("E7", "", calibri_16_bold_center)
    worksheet.write("A3", "Foaie de parcurs", calibri_16_bold_center)
    worksheet.write("A4", "Nr inmatriculare: " + lpl, arial_11_bold_center_wrap)
    worksheet.write("C4", "Perioadă raportată:\n" + to_rom_date(start)[:10] +
                    "\n" + to_rom_date(end)[:10], arial_11_bold_center_wrap)
    worksheet.write("E4", name, arial_11_bold_center_wrap)
    worksheet.write("A6", "Data", arial_11_bold_center_wrap)
    worksheet.write("B6", "Timp mișcare", arial_11_bold_center_wrap)
    worksheet.write("B7", "Start", arial_11_left)
    worksheet.write("C7", "Închidere", arial_11_left)
    worksheet.write("D7", "Distanța parcursă (km)", arial_11_bold_center_wrap)
    worksheet.write("F7", "Observatii", arial_11_bold_center_wrap)
    i = 0
    while i < number_of_reported_day:
        worksheet.write(i+7, 0, to_rom_date(day_day[i]), arial_10_left)
        worksheet.write(i + 7, 1, day_start[i], arial_10_right)
        worksheet.write(i + 7, 2, day_end[i], arial_10_right)
        worksheet.write(i + 7, 3, str(day_dist[i]) + " km", arial_10_right)
        worksheet.write(i + 7, 4, "", arial_10_left)
        worksheet.write(i + 7, 5, "", arial_10_left)
        i = i + 1
    last_write_row = number_of_reported_day + 7
    worksheet.write(last_write_row, 0, "Total", arial_10_left_bold)
    worksheet.write(last_write_row, 3, str(day_dist[-3]) + " km", arial_10_right)
    ww = float(day_dist[-3]) - float(work)
    worksheet.write(last_write_row + 1, 3, str(round(work, 1)) + " km", arial_10_right)
    worksheet.write(last_write_row + 2, 3, str(round(ww, 1)) + " km", arial_10_right)
    if weekend_start == "23:59:59":
        worksheet.write(last_write_row + 1, 0, "L-V", arial_10_left)
    else:
        worksheet.write(last_write_row + 1, 0, "L " + weekend_end[0:5] + "- V " + weekend_start[0:5], arial_10_left)

    if weekend_end == "00:00:00":
        worksheet.write(last_write_row + 2, 0, "S,D", arial_10_left)
    else:
        worksheet.write(last_write_row + 2, 0, "V " + weekend_start[0:5] + " - L " + weekend_end[0:5], arial_10_left)

    worksheet.write(last_write_row + 3, 0, "KM PLECARE", arial_10_left)

    worksheet.write(last_write_row + 4, 0, "KM SOSIRE", arial_10_left)
    worksheet.merge_range(last_write_row + 5, 0, last_write_row + 5, 5, "")

    if km_start == "":
        worksheet.write(last_write_row + 3, 1, "0 km", arial_10_right)
    else:
        worksheet.write(last_write_row + 3, 1, km_start + " km", arial_10_right)

    if km_start == "":
        km_start = 0
    else:
        try:
            km_start = float(km_start)
        except ValueError:
            km_start = 0
        else:
            pass

    km_end = km_start + float(day_dist[-3])
    worksheet.write(last_write_row + 4, 1, str(round(km_end,2)) + " km", arial_10_right)

    worksheet.write(last_write_row + 5, 0, "AUTOVEHICULUL ESTE IN STARE DE FUNCTIONARE / SEMNATURA")

    # add border to empty cells
    worksheet.write(last_write_row, 1, "", arial_10_left)
    worksheet.write(last_write_row, 2, "", arial_10_left)
    worksheet.write(last_write_row, 4, "", arial_10_left)
    worksheet.write(last_write_row, 5, "", arial_10_left)
    worksheet.write(last_write_row + 1, 1, "", arial_10_left)
    worksheet.write(last_write_row + 1, 2, "", arial_10_left)
    worksheet.write(last_write_row + 1, 4, "", arial_10_left)
    worksheet.write(last_write_row + 1, 5, "", arial_10_left)
    worksheet.write(last_write_row + 2, 1, "", arial_10_left)
    worksheet.write(last_write_row + 2, 2, "", arial_10_left)
    worksheet.write(last_write_row + 2, 4, "", arial_10_left)
    worksheet.write(last_write_row + 2, 5, "", arial_10_left)

    worksheet.write(last_write_row + 3, 2, "", arial_10_left)
    worksheet.write(last_write_row + 3, 3, "", arial_10_left)
    worksheet.write(last_write_row + 3, 4, "", arial_10_left)
    worksheet.write(last_write_row + 3, 5, "", arial_10_left)

    worksheet.write(last_write_row + 4, 2, "", arial_10_left)
    worksheet.write(last_write_row + 4, 3, "", arial_10_left)
    worksheet.write(last_write_row + 4, 4, "", arial_10_left)
    worksheet.write(last_write_row + 4, 5, "", arial_10_left)

    worksheet.freeze_panes(5, 6)
    workbook.close()