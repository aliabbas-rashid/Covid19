import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="finalyear123", database="fypdb")
mycursor = mydb.cursor()

#UK DEATHS
select_smt = "SELECT * FROM uk_deaths_within_28_days_of_positive_test_by_date"
mycursor.execute(select_smt)
myresult_uk_death = mycursor.fetchall()
field_names_uk_death= [i[0] for i in mycursor.description]

#Pakistan Profile
select_smt_2 = "SELECT * FROM pakistan_covid_profile"
mycursor.execute(select_smt_2)
myresult_pakistan_profile = mycursor.fetchall()
field_names_pakistan_profile = [i[0] for i in mycursor.description]

#UK GDP
select_smt_3 = "SELECT * FROM uk_gdp"
mycursor.execute(select_smt_3)
myresult_uk_gdp = mycursor.fetchall()
field_names_uk_gdp = [i[0] for i in mycursor.description]

#UK MEAN TEMP
select_smt_4 = "SELECT * FROM eng_mean_temp"
mycursor.execute(select_smt_4)
myresult_eng_mean_temp = mycursor.fetchall()
field_names_eng_mean_temp = [i[0] for i in mycursor.description]

#UK UK GVA
select_smt_5 = "SELECT * FROM uk_gross_value_added_avg"
mycursor.execute(select_smt_5)
myresult_uk_gva = mycursor.fetchall()
field_names_uk_gva = [i[0] for i in mycursor.description]