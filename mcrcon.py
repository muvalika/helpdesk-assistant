from mcrcon import MCRcon

def restart_mc_server():
    with MCRcon("mc-server-ip", "rcon_password") as mcr:
        response = mcr.command("/restart")
        return response
