# solutions/Yunus Evangeline/batch_runner.py

import pandas as pd
from main import run_agent  # Your agent logic
from curp_parser import parse_dob_from_curp

# Load Excel
df = pd.read_excel("curp_list.xlsx")

for index, row in df.iterrows():
    curp = row["CURP"]
    apellido_paterno = row["Apellido Paterno"]
    apellido_materno = row["Apellido Materno"]
    nombre1 = row["1er. Nombre"]
    nombre2 = row["2do. Nombre"] if pd.notna(row["2do. Nombre"]) else ""

    full_name = f"{nombre1} {nombre2} {apellido_paterno} {apellido_materno}".strip()

    print(f"\n🚀 Running agent for: {full_name} ({curp})")

    try:
        run_agent(full_name, curp)
    except Exception as e:
        print(f"❌ Failed for {full_name}: {e}")
