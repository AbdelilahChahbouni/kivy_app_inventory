
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.api import login
from .utils import app_session

class LoginScreen(Screen):
    email = StringProperty("")
    password = StringProperty("")
    print(email , password)

    def do_login(self):
        resp = login(self.email, self.password)

        if resp.get("success"):
            # Save the session values
            app_session["token"] = resp["token"]
            app_session["user_id"] = resp["user_id"]



            # Redirect to dashboard
            self.manager.current = "dashboard"

        else:
            # Show error message
            self.ids.login_msg.text = resp.get("message", "Login failed")
