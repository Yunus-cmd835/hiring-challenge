#solutions/Yunus Evangeliine/curp_parser.py

def parse_dob_from_curp(curp):
    dob_part = curp[4:10]  # Extract YYMMDD
    year = "19" + dob_part[0:2]  # Assuming 1900s for now
    month = dob_part[2:4]
    day = dob_part[4:6]

    # Convert month number to Spanish name
    month_names = {
        "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril",
        "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto",
        "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }
    month_name = month_names.get(month, "Mes inválido")

    return day, month_name, year

day, month, year = parse_dob_from_curp("TOGG960224HDFRLS09")
print(day, month, year)  # Output: 24 Febrero 1996
