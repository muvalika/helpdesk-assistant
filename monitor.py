import time
import requests
from mcstatus import JavaServer

# Configuration
MC_SERVER_ADDRESS = "mc-server:25565"
RASA_WEBHOOK_URL = "http://localhost:5005/conversations/{conversation_id}/trigger_intent"
CONVERSATION_ID = "admin_user" # The ID of the user to notify

def check_server():
    try:
        server = JavaServer.lookup(MC_SERVER_ADDRESS)
        server.status()
        return True
    except:
        return False

last_status = True

while True:
    current_status = check_server()
    if last_status and not current_status:
        # Server just went down! Trigger Rasa alert
        payload = {"intent": "external_server_down", "entities": {}}
        requests.post(RASA_WEBHOOK_URL.format(conversation_id=CONVERSATION_ID), json=payload)
    
    last_status = current_status
    time.sleep(60) # Check every minute
