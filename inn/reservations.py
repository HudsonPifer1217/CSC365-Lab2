import csv
table_name = 'RESERVATIONS'

with open("Reservations.csv", 'r', encoding= 'utf8') as file, open(f'Reservations-build-{table_name}.sql', 'w', encoding='utf8') as outfile:
    reader = csv.reader(file)
    header = next(reader)

    month_num = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
                 'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

    for row in reader:
        values = []

        for i in range(0,9):
            val = row[i].strip(" ").strip("'")
            if val == "":
                values.append('NULL')
            elif i == 2 or i == 3:
                for month in month_num:
                    if month in val.upper():
                        val = val.replace(month,month_num[month])
                        break
                values.append(f"STR_TO_DATE('{val}', '%d-%m-%y')")
            else:
                values.append(f"'{val}'")

        columns = ", ".join(header)
        values_str = ", ".join(values)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)