# solutions/Yunus Evangeline/main.py

from email_generator import generate_email
from adb_controller import tap, input_text
from logger import log_step

def create_outlook_account(name, curp):
    email = generate_email(name, curp)
    log_step("generate_email", True, f"Generated email: {email}")

    # Step 1: Tap "Crear cuenta" (adjust coordinates if needed)
    tap(500, 1200)
    log_step("tap_crear_cuenta", True, "Tapped 'Crear cuenta' button")

    # Step 2: Enter username
    input_text(email.split("@")[0])
    log_step("input_username", True, f"Entered username: {email.split('@')[0]}")

    # Step 3: Tap "Siguiente"
    tap(800, 1600)
    log_step("tap_siguiente", True, "Tapped 'Siguiente' button")

if __name__ == "__main__":
    create_outlook_account("Gaston Galindo", "TOGG960224HDFRLS09")
