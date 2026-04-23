import csv 
int_columns = {"Id", "Country"}

with open("car-makers.csv", "r", encoding="utf8") as file, open("cars-build-CAR_MAKERS.sql", "w", encoding="utf8") as outfile:
    reader = csv.reader(file, skipinitialspace=True)
    header = next(reader)
    for row in reader:
        country_index = header.index('Country')
        if row[country_index].strip().strip("'") == '':
            continue
        values = []
        for col, val in zip(header, row):
            val = val.strip().strip("'")
            if val == "":
                values.append("NULL")
            elif col in int_columns:
                values.append(val)
            else:
                val = val.replace("'", "''")
                values.append(f"'{val}'")

        columns = ", ".join(header)
        values_str = ", ".join(values)
        sql = f"INSERT INTO CAR_MAKERS ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)
print("Done — written to cars-build-CAR_MAKERS.sql")