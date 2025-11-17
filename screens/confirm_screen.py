
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from utils.api import transaction_in, transaction_out, get_machines
from .utils import app_session

class ConfirmScreen(Screen):
    part_id = StringProperty("")
    transaction_type = StringProperty("")
    machine_map = {}   # name -> id mapping
    machines = []      # keep python list, NOT a Kivy ListProperty (important)

    def on_pre_enter(self):
        self.ids.part_id_input.text = self.part_id
        token = app_session.get("token")

        if self.transaction_type == "IN":
            self.ids.machine_box.opacity = 0
            self.ids.machine_box.disabled = True
            self.ids.machine_box.height = 0
        else:
            self.ids.machine_box.opacity = 1
            self.ids.machine_box.disabled = False
            self.ids.machine_box.height = 50

            # ✅ Get full machine list
            machines = get_machines(token)
            self.machines = machines   # this remains list of dicts

            # ✅ Create map name → id (so dropdown returns name)
            self.machine_map = {m["name"]: m["id"] for m in machines}

            # ✅ Spinner displays only names
            self.ids.machine_spinner.values = list(self.machine_map.keys())


    def submit(self):
        part_id = self.ids.part_id_input.text.strip()
        quantity = self.ids.quantity_input.text.strip()
        token = app_session.get("token")
        user_id = app_session.get("user_id")

        if not part_id or not quantity:
            print("Part ID & Quantity are required!")
            return

        if self.transaction_type == "IN":
            response = transaction_in(token, part_id, quantity, user_id)
        else:
            selected_name = self.ids.machine_spinner.text
            machine_id = self.machine_map.get(selected_name)

            if not machine_id:
                print("You must select a machine.")
                return

            response = transaction_out(token, part_id, quantity, machine_id, user_id)

        print("API RESPONSE:", response)
        self.manager.current = "dashboard"



