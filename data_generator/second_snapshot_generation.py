import random
from random import randrange, randint, choice, choices, shuffle, uniform
from datetime import timedelta
from possibleData import *
from first_snapshot_generation import supervisors_list


# Function to check whether the given person was old enough in given date to be supervisor
def check_if_person_is_old_enough_to_supervise(pesel, date):
    # Take the year of the birth from pesel
    year_of_birth = int(pesel[:2])
    # Check whether the person was born in 2000s or in 1900s
    if int(pesel[2]) >= 2:
        year_of_birth += 2000
    else:
        year_of_birth += 1900
    # Return whether the person was old enough to supervise
    return year_of_birth + 25 < date.year


# Function to generate the renovation company name
def generate_company_name():
    # Randomly choose words from the list
    first_word = random.choice(first_words)
    second_word = random.choice(second_words)

    # Generate the company name
    company_name = first_word + " " + second_word
    return company_name


# Function to generate a company's NIP
def generate_nip():
    first_block = randint(100, 999)
    second_block = randint(100, 999)

    nip_digits = [int(digit) for digit in str(first_block) + str(second_block)]

    # Wagi używane do obliczenia cyfry kontrolnej
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]

    # Obliczenie cyfry kontrolnej
    checksum = sum(x * y for x, y in zip(nip_digits, weights)) % 11
    if checksum == 10:
        checksum = 0
    nip_digits.append(checksum)

    # Formatowanie numeru NIP do postaci "XX-XXX-XX-XX"
    formatted_nip = '{:03d}-{:03d}-{:02d}-{:02d}'.format(first_block, second_block, *nip_digits[2:])
    return formatted_nip


# Function to generate a person's PESEL
def generate_pesel(day, month, year, sex):
    if year > 2000:
        month += 20

    three_random = str(randint(100, 999))
    if sex == 'Male':
        gender_number = randint(0, 4) * 2 + 1
    else:
        gender_number = randint(0, 4) * 2
    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day

    a = int(y[0])
    b = int(y[1])
    c = int(m[0])
    d = int(m[1])
    e = int(dd[0])
    f = int(dd[1])
    g = int(three_random[0])
    h = int(three_random[1])
    i = int(three_random[2])
    j = int(gender_number)

    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - check % 10

    pesel_number = str(f'{y}{m}{dd}{three_random}{gender_number}{last_digit}')

    return pesel_number


def check_if_it_is_woman(person_name):
    return person_name[-1] == 'a'


def random_date(start, end):
    """This function will return a random datetime between two datetime objects"""
    delta = end - start
    random_days = randrange(delta.days + 1)
    return start + timedelta(days=random_days)


# Generation of 40 000 rows about the real estate"""
def generate_real_estate2():
    for generation in range(second_number_of_real_estate):
        street = choice(possible_street)
        generated_area = round(uniform(min_area, max_area))
        type_property = possible_type_property[randint(0, len(possible_type_property) - 1)]
        production_year = randint(min_production_year, second_max_production_year)
        flat_number = randint(min_flat_number, max_flat_number)
        developer = possible_developer[randint(0, len(possible_type_property) - 1)]

        # Determine number of floors
        max_allowed_floors = {
            'Single-family home': 3,
            'tenement': 4,
            'twin': 3,
            'flat': max_nr_floor,
            'apartment': max_nr_floor
        }
        number_of_floor = randint(min_flat_number, max_allowed_floors.get(type_property, max_nr_floor))

        # Determine which floor
        which_floor = randint(min_flat_number, number_of_floor)
        location_foreign_key = randint(0, number_of_locations)
        result = (generation + 1 + first_number_of_real_estate, street, generated_area, type_property, possible_production_range[randint(0,len(possible_production_range) - 1)], flat_number,
                  developer, number_of_floor, which_floor, location_foreign_key)

        second_real_estate_file.write(", ".join(map(str, result)) + '\n')
        
    second_real_estate_file.close()


 
renovation_team_random = randint(0, number_of_renovation_teams - 1)
def junk_ID(delay_reason):
    if delay_reason == 'No delay':
        return 1
    elif delay_reason == 'Weather-related setbacks':
        return 2
    elif delay_reason == 'Material shortages':
        return 3
    elif delay_reason == 'Unexpected structural issues':
        return 4
    elif delay_reason == 'Changes in project scope':
        return 5
    elif delay_reason == 'Labor shortages':
        return 6
    elif delay_reason == 'Budgetary constraints':
        return 7
# Generation of 40 000 rows about the purchases of the real estate made by our company
def generate_purchases2():
    for generation in range(second_number_of_purchases):
        generated_purchase_date = random_date(second_min_purchase_year, second_max_purchase_year)
        generated_purchase_price = round(randint(min_purchase_price, max_purchase_price), -2)
        generated_phone_number = randint(111_111_111, 999_999_999)
        purchase_result = (
            generation + 1 + first_number_of_purchases, generated_purchase_price, generated_purchase_date.date().strftime('%Y-%m-%d'),
            generated_phone_number)
        purchase_list.append(purchase_result)
        second_purchases_file.write(", ".join(str(s) for s in purchase_result) + '\n')

        """Add a worker that took care of the purchase"""
        worker_foreign_key = supervisors_list[randint(1, len(supervisors_list) - 1)][0]
        worker_purchase_result = (generation + first_number_of_purchases, worker_foreign_key)
        second_workers_supervise_purchases_file.write(", ".join(str(s) for s in worker_purchase_result) + '\n')
    second_purchases_file.close()
    second_workers_supervise_purchases_file.close()


# Generating 200 000 rows about renovation of the real estate
def generate_renovations2():
    # Ensure the file is open before starting to write
    with open('renovation_info_excel.csv', 'w') as renovation_info_excel:
        with open('second_renovations_file.csv', 'w') as second_renovations_file:
            for generation in range(second_number_of_renovations):
                # Generate the startDate of the renovation
                generated_start_date = random_date(second_renovation_start_date, second_renovation_end_date)
                # Generate max end date of the renovation which can be no further than 6 months after the start
                max_end_date = generated_start_date + timedelta(days=180)
                # Generate the endDate of the renovation
                generated_end_date = random_date(generated_start_date, max_end_date)
                # Generate the deadline of the renovation which can be 30 days before or after the end date
                generated_deadline = random_date(generated_end_date - timedelta(days=30),
                                                 generated_end_date + timedelta(days=30))
                # Generate the price of the renovation
                generated_price = randint(int(min_renovation_price / 100), int(max_renovaiton_price / 100)) * 100
                # Generate the supervising worker
                worker_foreign_key = supervisors_list[randint(0, len(supervisors_list) - 1)][0]
                # Generate the renovation team that took care of the work
                renovation_team_foreign_key = renovation_teams_list[randint(0, number_of_renovation_teams - 1)][0]
                # Generate the ID of the real estate
                real_estate_foreign_key = randint(1, second_number_of_real_estate)

                results_tuple = (generation + 1 + first_number_of_renovations, generated_start_date.date().strftime('%Y-%m-%d'),
                                 generated_end_date.date().strftime('%Y-%m-%d'), generated_deadline.date().strftime('%Y-%m-%d'),
                                 generated_price, renovation_team_foreign_key, real_estate_foreign_key, worker_foreign_key)

                days_of_delay = (generated_end_date - generated_deadline).days
                days_of_delay = days_of_delay if days_of_delay > 0 else 0
                number_of_renovated_rooms = randint(1, 10)
                worker_random = randint(0, len(supervisors_list) - 1)
                worker_foreign_key = supervisors_list[worker_random][0]
                supervisor_name = supervisors_list[worker_random][1]
                renovation_team_name = renovation_teams_list[renovation_team_random][0]
                reason_for_delay = reasons_for_delay[randint(0, len(reasons_for_delay) - 1)]
                delay_id = junk_ID(reason_for_delay)
                excel_result = ((generation // 100) + 1, renovation_team_name, days_of_delay, generated_price, supervisor_name,
                                reason_for_delay, delay_id, number_of_renovated_rooms)

                # Write to the files
                renovation_info_excel.write(", ".join(str(s) for s in excel_result) + '\n')
                second_renovations_file.write(", ".join(str(s) for s in results_tuple) + '\n')

            # Files are closed automatically after the with block ends




