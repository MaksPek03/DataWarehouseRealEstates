import random
from random import randrange, randint, choice, choices, shuffle, uniform, sample
from datetime import timedelta
from possibleData import *


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

def random_date_establish(start_date, end_date):
    # Obliczenie różnicy w dniach między datami
    delta = end_date - start_date
    # Wygenerowanie losowej liczby dni w zakresie dat
    random_days = random.randint(0, delta.days)
    # Dodanie wylosowanej liczby dni do daty początkowej
    random_date = start_date + timedelta(days=random_days)
    # Zwrócenie wylosowanej daty (bez godziny)
    return random_date.date()

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


# Generation of 500 rows about firms that take care of the renovation
def generate_renovation_teams():
    for generation in range(number_of_renovation_teams):
        nip = generate_nip()
        while nip in generated_nips or len(generated_nips) > 100_000_000:
            nip = generate_nip()
        generated_nips.append(nip)
        generated_company_name = generate_company_name()
        name = choice(possible_names)
        sex = "Male" if check_if_it_is_woman(name) else "Female"
        surname = choice(possible_female_surnames) if sex == "Male" else choice(possible_male_surnames)
        construction_manager = name + " " + surname
        renovation_team = (generation + 1, nip, generated_company_name, construction_manager)
        renovation_teams_list.append(renovation_team)
        renovation_teams_file.write(", ".join(str(s) for s in renovation_team) + '\n')
        company_name = generated_company_name.replace(" ", "").lower()
        email = f"{company_name}@gmail.com"
        excel_result = (generation + 1, generated_company_name, nip, construction_manager, email, randint(100_000_000, 999_999_999),
                        specializations[randint(0, len(specializations) - 1)], possible_establish_years[randint(0,len(possible_establish_years) - 1)], possible_number_workers[randint(0, len(possible_number_workers) - 1)],
                        possible_certifications[randint(0, len(possible_certifications) - 1)]
                        , possible_certifications_range[randint(0, len(possible_certifications_range) - 1)], 
                        possible_finished_renovation_number[randint(0, len(possible_finished_renovation_number) - 1)])
        renovation_teams_excel.write(", ".join(str(s) for s in excel_result) + '\n')

    renovation_teams_file.close()
    renovation_teams_excel.close()


# Generation of 200 rows about workers of our company
def distribute_positions_across_list():
    for position, count in positions_distribution.items():
        if count is not None:
            positions_list.extend([position] * count)


sum_of_positions = sum(count for count in positions_distribution.values() if count is not None)
remaining_positions = first_number_of_workers - sum_of_positions
positions_list.extend(choices(["researcher", "analyst", "supervisor"], k=remaining_positions))

shuffle(positions_list)


def generate_workers():
    def generate_unique_pesel(sex):
        max_attempts = 1000
        attempts = 0
        year = randint(1960, 2003)
        month = randint(1, 12)  # Months range from 1 to 12
        while attempts < max_attempts:
            if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day = randint(1, 29)  # February in a leap year
            else:
                day = randint(1, 28) if month == 2 else randint(1, 31)
            pesel = generate_pesel(day, month, year, sex)
            if pesel not in generated_pesels:
                generated_pesels.append(pesel)
                return pesel
            attempts += 1
        raise RuntimeError("Unable to generate unique PESEL after multiple attempts")

    def generate_ceo():
        pesel = generate_unique_pesel("Male")
        worker_info = (1, pesel, "George", "Charpak", "CEO")
        workers_file.write(", ".join(map(str, worker_info)) + '\n')

    generate_ceo()
    for idx, worker_position in enumerate(positions_list, start=1):
        name = choice(possible_names)
        sex = "Male" if check_if_it_is_woman(name) else "Female"
        surname = choice(possible_female_surnames) if sex == "Male" else choice(possible_male_surnames)

        pesel = generate_unique_pesel(sex)

        worker_info = (idx+1, pesel, name, surname, worker_position)
        if worker_position == "supervisor":
            supervisors_list.append(worker_info)
        workers_file.write(", ".join(map(str, worker_info)) + '\n')
    workers_file.close()


# Generation of 60 000 rows about the real estate"""
def generate_real_estate():
    for generation in range(first_number_of_real_estate):
        street = choice(possible_street)
        generated_area = round(uniform(min_area, max_area))
        type_property = possible_type_property[randint(0, len(possible_type_property) - 1)]
        production_year = randint(min_production_year, first_max_production_year)
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
        result = (generation + 1, street, generated_area, type_property, possible_production_range[randint(0,len(possible_production_range) - 1)], flat_number,
                  developer, number_of_floor, which_floor, location_foreign_key)
        first_real_estate_file.write(", ".join(map(str, result)) + '\n')
    first_real_estate_file.close()


# Generation of 100 000 rows about the purchases of the real estate made by our company
def generate_purchases():
    for generation in range(first_number_of_purchases):
        generated_purchase_date = random_date(first_min_purchase_year, first_max_purchase_year)
        generated_purchase_price = round(randint(min_purchase_price, max_purchase_price), -2)
        generated_phone_number = randint(111_111_111, 999_999_999)
        purchase_result = (
            generation + 1, generated_purchase_price, generated_purchase_date.date().strftime('%Y-%m-%d'),
            generated_phone_number)
        purchase_list.append(purchase_result)
        first_purchases_file.write(", ".join(str(s) for s in purchase_result) + '\n')

        """Add a worker that took care of the purchase"""
        worker_foreign_key = supervisors_list[randint(1, len(supervisors_list) - 1)][0]
        worker_purchase_result = (generation, worker_foreign_key)
        first_workers_supervise_purchases_file.write(", ".join(str(s) for s in worker_purchase_result) + '\n')
    first_workers_supervise_purchases_file.close()
    first_purchases_file.close()


# Generation of 300 rows about the locations of the real estate
def generate_locations():
    for generation in range(number_of_locations):
        city = random.choice(list(cities.keys()))
        district = random.choice(cities[city])
        residential_area = random.choice(residential_areas)
        combination = (generation + 1, city, district, residential_area)
        locations_file.write(", ".join(str(s) for s in combination) + '\n')
    locations_file.close()


# Generating 300 000 rows about renovation of the real estate
def generate_renovations():
    for generation in range(first_number_of_renovations):
        # Generate the startDate of the renovation
        generated_start_date = random_date(first_min_purchase_year, first_renovation_end_date)
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
        worker_random = randint(0, len(supervisors_list) - 1)
        worker_foreign_key = supervisors_list[worker_random][0]
        # Generate the renovation team that took care of the work
        renovation_team_random = randint(0, number_of_renovation_teams - 1)
        renovation_team_foreign_key = renovation_teams_list[renovation_team_random][0]
        # Generate the ID of the real estate
        real_estate_foreign_key = randint(1, first_number_of_real_estate)

        results_tuple = (generation + 1, generated_start_date.date().strftime('%Y-%m-%d'),
                         generated_end_date.date().strftime('%Y-%m-%d'), generated_deadline.date().strftime('%Y-%m-%d'),
                         generated_price, renovation_team_foreign_key, real_estate_foreign_key, worker_foreign_key)
            
        days_of_delay = (generated_end_date - generated_deadline).days
        days_of_delay = days_of_delay if days_of_delay > 0 else 0
        number_of_renovated_rooms = randint(1, 10)
        supervisor_name = supervisors_list[worker_random][1]
        renovation_team_name = renovation_teams_list[renovation_team_random][0]
        reason_for_delay = reasons_for_delay[randint(0, len(reasons_for_delay) - 1)]
        delay_id = junk_ID(reason_for_delay)
        excel_result = ((generation // 100)+1, renovation_team_name, days_of_delay, generated_price, supervisor_name,
                        reason_for_delay,delay_id,  number_of_renovated_rooms)
        renovation_info_excel.write(", ".join(str(s) for s in excel_result) + '\n')

        first_renovations_file.write(", ".join(str(s) for s in results_tuple) + '\n')
    first_renovations_file.close()
    renovation_info_excel.close()



