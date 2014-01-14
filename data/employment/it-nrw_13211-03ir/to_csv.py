# encoding: utf-8

"""
Converts excel source data from Landesdatenbank NRW
for statistic 13211-03ir to clean CSV
"""

import xlrd
import csv
import re
import calendar


def read_xls(path):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    table = []
    for row in range(sheet.nrows):
        row_as_list = []
        for col in range(sheet.ncols):
            row_as_list.append(excel_field_to_value(sheet, row, col))
        table.append(row_as_list)
    data = []
    # now read only data rows (year string in first column)
    for row in table:
        if count_none(row) / float(len(row)) == 1.0:
            continue
        if row[0] is None:
            continue
        match = re.match(r"[0-9]{4}", row[0])
        if match is None:
            continue
        if len(row) != 37:
            continue
        data.append(row)
    out = []
    # now we should only have data rows left
    # with 37 columns
    for row in data:
        year = int(row.pop(0))
        for month in range(1, 13):
            first, last = calendar.monthrange(year, month)
            datestr = "%s-%02d-%02d" % (year, month, last)
            outrow = [datestr]
            for subcol in ['gesamt', 'maennlich', 'weiblich']:
                outrow.append(row.pop(0))
            out.append(outrow)
    # sort rows by date
    out = sorted(out, key=lambda item: item[0])
    return out


def excel_field_to_value(sheet, row_index, col_index):
    """
    Returns the excel sheet field indicated by row and column col_index
    as a proper float, int, unicode or None
    """
    ctype = sheet.cell_type(row_index, col_index)
    val = sheet.cell_value(row_index, col_index)
    if ctype == 0 or ctype == 6 or val == u' ' or val == u'' or val == u'...':
        # Empty or blank field
        return None
    if ctype == 2:
        # number
        if ("%.1f" % val).split('.')[1] == '0':
            val = int(val)
    if ctype == 4:
        if val == 1:
            return True
        return False
    return val


def count_none(row):
    """Counts the number of None values in a list"""
    n = 0
    for f in row:
        if f is None:
            n += 1
    return n


def export_csv(data, path):
    with open(path, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['datum', 'gesamt', 'maennlich', 'weiblich'])
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    data = read_xls('_source/13211-03ir.xls')
    export_csv(data, '13211-03ir.csv')
