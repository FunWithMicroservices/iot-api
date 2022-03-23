import random


def get_random_Lat_long_data():
    return random.randint(10**16, 99*10**16)

def get_random_speed_data():
    return random.randint(10, 230)

def get_random_dangerous_event():
    return bool(random.randint(0, 1))

def get_random_customer_id():
    # TODO
    pass

