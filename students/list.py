import csv
table_name = "LIST"
int_columns = {'Classroom', 'Grade'}

with open("list.csv", 'r', encoding= 'utf8') as file, open(f'students-build-{table_name}.sql', 'w', encoding='utf8') as outfile:
    reader = csv.reader(file, skipinitialspace=True)
    header = next(reader)

    for row in reader:
        values = []
        for col, val in zip(header, row):  # ← need col too!
            val = val.strip().strip("'")
            if val == "":
                values.append('NULL')
            elif col in int_columns:
                values.append(val)           # INT — no quotes
            else:
                val = val.replace("'", "''")
                values.append(f"'{val}'")
        
        columns = ", ".join(header)
        values_str = ", ".join(values)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)

print(f"Done — written to students-build-{table_name}.sql")