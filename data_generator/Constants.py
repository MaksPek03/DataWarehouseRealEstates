from datetime import datetime

positions_list = []
supervisors_list = []
real_estates_list = []
renovation_teams_list = []
purchase_list = []
generated_pesels = []
generated_nips = []

first_number_of_workers = 200
first_number_of_renovations = 300_000
first_number_of_real_estate = 60_000
second_number_of_renovations = 200_000
second_number_of_real_estate = 40_000
number_of_renovation_teams = 500
first_number_of_purchases = 60_000
second_number_of_purchases = 40_000
number_of_locations = 300
number_of_workers_supervise_purchases = first_number_of_purchases + second_number_of_purchases

min_delay_time = 0
max_delay_time = 10

min_renovation_price = 4_000
max_renovaiton_price = 150_000
min_production_year = 1900
first_max_production_year = 2015
second_max_production_year = 2023

first_min_purchase_year = datetime.strptime('1/1/2000 12:00 AM', '%d/%m/%Y %I:%M %p')
first_max_purchase_year = datetime.strptime('31/12/2015 12:00 AM', '%d/%m/%Y %I:%M %p')
second_min_purchase_year = datetime.strptime('1/1/2016 12:00 AM', '%d/%m/%Y %I:%M %p')
second_max_purchase_year = datetime.strptime('1/1/2024 12:00 AM', '%d/%m/%Y %I:%M %p')
min_purchase_price = 200_000
max_purchase_price = 2_000_000

min_date_of_establishment = datetime.strptime('1/1/1900 12:00 AM', '%d/%m/%Y %I:%M %p')
max_date_of_establishment = datetime.strptime('1/1/2000 12:00 AM', '%d/%m/%Y %I:%M %p')

min_flat_number = 1
max_flat_number = 200
min_area = 20
max_area = 100
min_nr_floor = 1
max_nr_floor = 10
first_renovation_start_date = datetime.strptime('1/1/2000 12:00 AM', '%d/%m/%Y %I:%M %p')
first_renovation_end_date = datetime.strptime('31/12/2015 12:00 AM', '%d/%m/%Y %I:%M %p')
second_renovation_start_date = datetime.strptime('1/1/2016 12:00 AM', '%d/%m/%Y %I:%M %p')
second_renovation_end_date = datetime.strptime('1/1/2024 12:00 AM', '%d/%m/%Y %I:%M %p')

odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
even_months = (4, 6, 9, 11, 24, 26, 29, 31)

first_renovations_file = open('first_renovations.txt', 'w+')
locations_file = open('first_locations.txt', 'w+')
first_real_estate_file = open('first_real_estates.txt', 'w+')
workers_file = open('first_workers.txt', 'w+')
renovation_teams_file = open('first_renovation_teams.txt', 'w+')
first_purchases_file = open('first_purchases.txt', 'w+')
first_workers_supervise_purchases_file = open('first_supervise_purchase.txt', 'w+')
second_renovations_file = open('second_renovations.txt', 'w+')
second_real_estate_file = open('second_real_estates.txt', 'w+')
second_purchases_file = open('second_purchases.txt', 'w+')
second_workers_supervise_purchases_file = open('second_supervise_purchase.txt', 'w+')
renovation_info_excel = open('renovation_info.csv', 'w+')
renovation_teams_excel = open('renovation_team.csv', 'w+')

