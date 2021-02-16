import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="finalyear123", database="fypdb")

mycursor = mydb.cursor()

select_smt = "SELECT * FROM uk_deaths_within_28_days_of_positive_test_by_date"
mycursor.execute(select_smt)

myresult_uk_death = mycursor.fetchall()

select_smt = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'uk_deaths_within_28_days_of_positive_test_by_date'"
mycursor.execute(select_smt)
myresult_uk_death_columns = mycursor.fetchall()
#print(myresult_uk_death)
#for row in myresult_uk_death:
 #   print(row)

rows = (myresult_uk_death_columns[3])
tuple(rows)
print(rows)

result = []
for i in range(0, len(rows)):
    result.append(rows[i])

for i in range(0, len(myresult_uk_death)):
    result.append(myresult_uk_death[i])

for row in result:
    print(row)

#myresult_uk_death.insert(0, rows)

#print(myresult_uk_death)

select_smt_2 = "SELECT * FROM pakistan_covid_profile"
mycursor.execute(select_smt_2)

myresult_pakistan_profile = mycursor.fetchall()

select_smt_3 = "SELECT * FROM uk_gdp"
mycursor.execute(select_smt_3)

myresult_uk_gdp = mycursor.fetchall()

select_smt_4 = "SELECT * FROM eng_mean_temp"
mycursor.execute(select_smt_4)

myresult_eng_mean_temp = mycursor.fetchall()