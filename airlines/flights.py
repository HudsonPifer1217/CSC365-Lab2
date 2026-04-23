import csv
table_name = 'FLIGHTS'

with (open("flights.csv", 'r', encoding= 'utf8') as file, open('airlines-build-FLIGHTS.sql', 'w', encoding='utf8') as outfile):
    reader = csv.reader(file)
    header = next(reader)
    count = 0

    for row in reader:
        values = []
        for val in row:
            if val == "NULL":
                val = val.strip(" ").strip("'")
                values.append(f"{val}")
            else:
                val = val.strip(" ").strip("'")
                values.append(f"'{val}'")
        count +=1

        new_header = []
        count2 = 0
        for name in header:
            name = name.strip(" ")
            new_header.append(name)

        columns = ", ".join(new_header)
        values_str = ", ".join(values)


        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)
        print(count)