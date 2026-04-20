import csv
table_name = 'MARATHON'

with open("marathon.csv", 'r', encoding= 'utf8') as file, open('marathon-build-MARATHON.sql', 'w', encoding='utf8') as outfile:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        values = []

        for val in row:
            if val == "":
                values.append('NULL')
            else:
                val = val.strip("'")
                values.append(f"'{val}'")

        columns = ", ".join(header)
        values_str = ", ".join(values)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)

