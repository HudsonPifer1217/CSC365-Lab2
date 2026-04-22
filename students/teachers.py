import csv
 
table_name = 'TEACHERS'
int_columns = {'Classroom'}
 
with open("teachers.csv", 'r', encoding='utf-8-sig') as file, \
     open(f'students-build-{table_name}.sql', 'w', encoding='utf-8') as outfile:
 
    reader = csv.reader(file, skipinitialspace=True)  # <-- fixes leading spaces
    header = [h.strip() for h in next(reader)]
 
    for row in reader:
        values = []
 
        for col, val in zip(header, row):
            val = val.strip().strip("'")  # remove whitespace and surrounding quotes
 
            if val == "":
                values.append('NULL')
            elif col in int_columns:
                values.append(val)              # INT — no quotes
            else:
                val = val.replace("'", "''")    # escape embedded single quotes
                values.append(f"'{val}'")
 
        columns = ", ".join(header)
        values_str = ", ".join(values)
 
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        outfile.write(sql)
 
print(f"Done — written to students-build-{table_name}.sql")