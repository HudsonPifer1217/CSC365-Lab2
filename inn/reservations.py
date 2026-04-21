import csv
table_name = 'RESERVATIONS'

with open("Reservations.csv", 'r', encoding= 'utf8') as file, open(f'Reservations-build-{table_name}.sql', 'w', encoding='utf8') as outfile:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        values = []
        month_num = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
                     'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
        for val in row:
            val = val.strip(" ").strip("'")
            if val == "":
                values.append('NULL')
            for month in month_num:
                if month in val:
                    val = val.replace(month,month_num[month])
                    values.append(f"STR_TO_DATE('{val}', '%d-%b-%y')")
                    break
            else:
                values.append(f"'{val}'")

        columns = ", ".join(header)
        values_str = ", ".join(values)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)