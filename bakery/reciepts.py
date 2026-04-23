import csv
table_name = 'RECEIPTS'

with open("receipts.csv", 'r', encoding= 'utf8') as file, open(f'bakery-build-{table_name}.sql', 'w', encoding='utf8') as outfile:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        values = []

        for val in row:
            val = val.strip(" ").strip("'")
            if val == "":
                values.append('NULL')
            elif 'Oct' in val:
                val = val.replace('Oct', '10')
                values.append(f"STR_TO_DATE('{val}', '%d-%m-%Y')")
            else:
                values.append(f"'{val}'")

        columns = ", ".join(header)
        values_str = ", ".join(values)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)