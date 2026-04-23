import csv
int_columns = {"Campus","Year","CampusFee"}
table_name = "CSU_FEES"

with open("csu-fees.csv", "r", encoding="utf8") as file, open(f"build-{table_name}.sql", "w", encoding="utf8") as outfile:
    reader = csv.reader(file, skipinitialspace=True)
    header = next(reader)
    for row in reader:
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
        columns= ", ".join(header)
        values_str = ", ".join(values)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)
print(f"Done — written to build-{table_name}.sql")