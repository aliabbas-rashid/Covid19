import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="finalyear123", database="fypdb")
except mysql.Error as e:
    print(f"Exception raised: {e}")

mycursor = mydb.cursor()

# UK DEATHS
select_smt = "SELECT * FROM uk_deaths_within_28_days_of_positive_test_by_date"
mycursor.execute(select_smt)
myresult_uk_death = mycursor.fetchall()
field_names_uk_death= [i[0] for i in mycursor.description]
select_start_date_1 = "SELECT * FROM uk_deaths_within_28_days_of_positive_test_by_date WHERE id=331"
mycursor.execute(select_start_date_1)
myresult_uk_death_start_date = mycursor.fetchall()
select_end_date_1 = "SELECT * FROM uk_deaths_within_28_days_of_positive_test_by_date WHERE id=1"
mycursor.execute(select_end_date_1)
myresult_uk_death_end_date = mycursor.fetchall()
uk_death_date_start = myresult_uk_death_start_date[0]
uk_death_date_end = myresult_uk_death_end_date[0]

# Pakistan Profile
select_smt_2 = "SELECT * FROM pakistan_covid_profile"
mycursor.execute(select_smt_2)
myresult_pakistan_profile = mycursor.fetchall()
field_names_pakistan_profile = [i[0] for i in mycursor.description]
select_start_date_2 = "SELECT * FROM pakistan_covid_profile WHERE id=1"
mycursor.execute(select_start_date_2)
myresult_pakistan_covid_profile_start_date = mycursor.fetchall()
select_end_date_2 = "SELECT * FROM pakistan_covid_profile WHERE id=328"
mycursor.execute(select_end_date_2)
myresult_pakistan_covid_profile_end_date = mycursor.fetchall()
pakistan_covid_profile_date_start = myresult_pakistan_covid_profile_start_date[0]
pakistan_covid_profile_date_end = myresult_pakistan_covid_profile_end_date[0]


# UK GDP
select_smt_3 = "SELECT * FROM uk_gdp_new"
mycursor.execute(select_smt_3)
myresult_uk_gdp = mycursor.fetchall()
field_names_uk_gdp = [i[0] for i in mycursor.description]
select_start_date_3 = "SELECT * FROM uk_gdp_new WHERE id=1"
mycursor.execute(select_start_date_3)
myresult_uk_gdp_start_date = mycursor.fetchall()
select_end_date_3 = "SELECT * FROM uk_gdp_new WHERE id=168"
mycursor.execute(select_end_date_3)
myresult_uk_gdp_end_date = mycursor.fetchall()
uk_gdp_date_start = myresult_uk_gdp_start_date[0]
uk_gdp_date_end = myresult_uk_gdp_end_date[0]

# UK MEAN TEMP
select_smt_4 = "SELECT * FROM eng_mean_temp"
mycursor.execute(select_smt_4)
myresult_eng_mean_temp = mycursor.fetchall()
field_names_eng_mean_temp = [i[0] for i in mycursor.description]
select_start_date_4 = "SELECT * FROM eng_mean_temp WHERE id=1"
mycursor.execute(select_start_date_4)
myresult_eng_mean_temp_start_date = mycursor.fetchall()
select_end_date_4 = "SELECT * FROM eng_mean_temp WHERE id=137"
mycursor.execute(select_end_date_4)
myresult_eng_mean_temp_end_date = mycursor.fetchall()
eng_mean_temp_date_start = myresult_eng_mean_temp_start_date[0]
eng_mean_temp_date_end = myresult_eng_mean_temp_end_date[0]

# UK UK GVA
select_smt_5 = "SELECT * FROM uk_gross_value_added_avg"
mycursor.execute(select_smt_5)
myresult_uk_gva = mycursor.fetchall()
field_names_uk_gva = [i[0] for i in mycursor.description]
select_start_date_5 = "SELECT * FROM uk_gross_value_added_avg WHERE id=1"
mycursor.execute(select_start_date_5)
myresult_uk_gross_value_added_avg_start_date = mycursor.fetchall()
select_end_date_5 = "SELECT * FROM uk_gross_value_added_avg WHERE id=73"
mycursor.execute(select_end_date_5)
myresult_uk_gross_value_added_avg_end_date = mycursor.fetchall()
uk_gross_value_added_avg_date_start = myresult_uk_gross_value_added_avg_start_date[0]
uk_gross_value_added_avg_date_end = myresult_uk_gross_value_added_avg_end_date[0]