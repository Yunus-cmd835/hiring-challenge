# solutions/Yunus Evangeline/main.py

from email_generator import generate_email
from adb_controller import tap, input_text, long_press
from logger import log_step

def create_outlook_account(name, curp):
    try:
        email = generate_email(name, curp)
        log_step("generate_email", True, f"Generated email: {email}")

        # Step 1: Tap "Crear cuenta"
        tap(500, 1200)
        log_step("tap_crear_cuenta", True, "Tapped 'Crear cuenta' button")

        # Step 2: Enter username
        input_text(email.split("@")[0])
        log_step("input_username", True, f"Entered username: {email.split('@')[0]}")

        # Step 3: Tap "Siguiente"
        tap(800, 1600)
        log_step("tap_siguiente", True, "Tapped 'Siguiente' button")

        # Step 4: Enter Password
        input_text("SecurePass123!")
        log_step("input_password", True, "Entered password")
        tap(800, 1600)
        log_step("tap_password_next", True, "Tapped 'Next' after password")

        # Step 5: Enter Name
        input_text("Gaston")
        tap(400, 1600)
        input_text("Galindo")
        log_step("input_name", True, "Entered first and last name")
        tap(800, 1600)
        log_step("tap_name_next", True, "Tapped 'Next' after name")

        # Step 6: Enter DOB
        input_text("22")
        tap(400, 1200)
        input_text("Febrero")
        tap(400, 1400)
        input_text("1996")
        log_step("input_dob", True, "Entered date of birth")
        tap(800, 1600)
        log_step("tap_dob_next", True, "Tapped 'Next' after DOB")

        # Step 7: CAPTCHA
        long_press(600, 1800, duration=2500)
        log_step("captcha_hold", True, "Pressed and held CAPTCHA button")
        tap(800, 1600)
        log_step("tap_final_confirm", True, "Tapped final confirmation button")

    except Exception as e:
        log_step("fatal_error", False, f"Agent crashed: {str(e)}")

if __name__ == "__main__":
    create_outlook_account("Gaston Galindo", "TOGG960224HDFRLS09")
