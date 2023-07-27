

def get_float(prompt: str):
    try:
        return float(input(prompt))
    except ValueError:
        print('')


# FIRST UNIT
while True:
    unit = input('SELECT THE FIRST UNIT: KG / LB / OZ\n> ')
    if unit == "KG":
        first_unit = get_float('KG= ')
    elif unit == "LB":
        first_unit = get_float('LB= ')
    elif unit == "OZ":
        first_unit = get_float('OZ= ')
    else:
        continue
    break

# FINAL UNIT
while True:
    final_unit = input('SELECT THE FINAL UNIT: KG / LB / OZ\n> ')
    # CONVERTING

    if final_unit == "KG":
        print('KG')
        if unit == "LB":
            print('RIGHT HERER')
            second_unit = first_unit * 2.204622621848776  # KG to LB
        elif unit == "OZ":
            second_unit = first_unit * 35.27396195  # KG to OZ

    elif final_unit == "LB":
        print('LB')
        if unit == "KG":
            second_unit = first_unit / 2.204622621848776  # LB to KG
        elif unit == "OZ":
            second_unit = first_unit * 16  # LB to OZ

    elif final_unit == "OZ":
        print('OZ')
        if unit == "KG":
            second_unit = first_unit * 0.02834952  # OZ to KG
        elif unit == "LB":
            second_unit = first_unit / 16  # OZ to LB

    else:
        continue
    # RESULT
    print(first_unit, "is equal to", second_unit)
    break
exit()
