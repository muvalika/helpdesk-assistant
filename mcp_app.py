from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("IT-Management")
@mcp.tool()
def reset_password(email: str) -> dict: """
Triggers a password reset for a specific user email. 
Args:
email: The corporate email address of the employee. 
"""
  # Logic to interface with your IT system
success = True if "@" in email else False

return {
  "reset_password_sucess": success,
  "message": "Instructions sent" if you success else "Invalid email"
}
if__name__ == "__main__":
mcp.run()
end code()
