import os
import re

base_path = r"c:\Users\emila\Desktop\Aliagha\stitch_aghasolutions_site_rebuild\stitch_aghasolutions_site_rebuild"

# Read home config
with open(os.path.join(base_path, "home_aghasolutions", "code.html"), "r", encoding="utf-8") as f:
    home_content = f.read()

colors_match = re.search(r'("colors":\s*\{.*?\n\s*\})', home_content, re.DOTALL)
if not colors_match:
    print("Failed to find colors in home")
    exit(1)
home_colors = colors_match.group(1)
# Remove the closing brace to append more colors
home_colors = home_colors.rstrip().rstrip('}') + ','

# Fix Clients
clients_path = os.path.join(base_path, "clients_aghasolutions", "code.html")
with open(clients_path, "r", encoding="utf-8") as f:
    clients_content = f.read()

# In clients, replace `colors: {` with `home_colors` + `green: { ...`
# Actually, the tailwind config is just javascript.
clients_content = re.sub(r'colors:\s*\{', home_colors + '\n', clients_content)

with open(clients_path, "w", encoding="utf-8") as f:
    f.write(clients_content)

# Fix Contact
contact_path = os.path.join(base_path, "contact_aghasolutions", "code.html")
with open(contact_path, "r", encoding="utf-8") as f:
    contact_content = f.read()

contact_content = re.sub(r'colors:\s*\{', home_colors + '\n', contact_content)

with open(contact_path, "w", encoding="utf-8") as f:
    f.write(contact_content)

print("Successfully injected colors.")
