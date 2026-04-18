from mcrcon import MCRcon
from rasa_sdk import Action

class ActionAutoFixLag(Action):
    def name(self):
        return "action_fix_lag"

    def run(self, dispatcher, tracker, domain):
        with MCRcon(os.getenv("MC_HOST"), os.getenv("MC_RCON_PASS")) as mcr:
            # 1. Clear dropped items to reduce lag
            mcr.command("/kill @e[type=item]")
            # 2. Trigger a garbage collection (if supported by plugins)
            mcr.command("/gc")
            
        dispatcher.utter_message(text="I've cleared dropped entities and optimized memory. Is the performance better now?")
        return []
      //fixes-it when server is laggy
