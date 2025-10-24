from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1400, 900
BG = (255, 255, 255)
BOX_FILL = (247, 249, 252)
FOLDER_FILL = (230, 242, 255)
ENV_FILL = (255, 240, 246)
OUTLINE = (59, 130, 246)
TEXT_COLOR = (15, 23, 42)
SMALL = (71, 85, 105)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
d = ImageDraw.Draw(img)

# fallback font
try:
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    font = ImageFont.truetype("DejaVuSans.ttf", 14)
    font_small = ImageFont.truetype("DejaVuSans.ttf", 12)
except Exception:
    font_title = ImageFont.load_default()
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()


def rect(x, y, w, h, fill, outline=(70, 70, 70)):
    d.rounded_rectangle(
        [x, y, x + w, y + h], radius=8, fill=fill, outline=outline, width=2
    )


def text(x, y, t, f=font, fill=TEXT_COLOR):
    d.text((x, y), t, font=f, fill=fill)


# Title
text(30, 18, "MedPal — Project Structure", font_title)

# Left column: medPalBot and Data
rect(40, 60, 320, 100, BOX_FILL)
text(60, 80, "medPalBot.py", font)
text(
    60,
    102,
    "(Python Telegram bot; uses agent)",
    font_small,
)

rect(40, 180, 320, 300, BOX_FILL)
text(60, 200, "Data / Datasets", font)
text(60, 225, "medical_health_facilities.csv", font_small)
text(60, 245, "medical_health_facilities.json", font_small)
text(60, 265, "kenya_chemists_data.csv", font_small)
text(60, 285, "kenya_chemists_data.json", font_small)
text(60, 305, "riders_data.csv", font_small)
text(60, 325, "emergency_medical_services.csv", font_small)

# Center: Engine and AgentTools
rect(420, 60, 500, 200, FOLDER_FILL, outline=OUTLINE)
text(440, 80, "Engine/", font)
text(440, 102, "__init__.py · agent.py · index.py", font_small)

rect(460, 140, 420, 260, BOX_FILL)
text(480, 160, "AgentTools/", font)
text(480, 185, "findDeliveryServices.py", font_small)
text(480, 205, "findHealthFacilities.py", font_small)
text(480, 225, "findMedicalProfessionals.py", font_small)
text(480, 245, "findMedicalEmergencyServices.py", font_small)
text(480, 265, "findPharmaceuticals.py", font_small)
text(480, 285, "makeTransaction.py", font_small)
text(480, 305, "sendMail.py · sendWhatsappMessage.py", font_small)

# Right: Virtualenv
rect(960, 60, 360, 110, ENV_FILL, outline=(190, 24, 93))
text(980, 90, "MedPalEnv/", font)
text(980, 110, "(virtualenv - ignored)", font_small)

# Right-bottom: Config / meta
rect(420, 440, 900, 160, BOX_FILL)
text(440, 460, "Docs & Config", font)
text(440, 485, "README.md", font_small)
text(440, 505, "requirements.txt", font_small)
text(440, 525, ".gitignore", font_small)

# Elasticsearch DB box
rect(960, 220, 320, 120, BOX_FILL)
text(980, 245, "Elasticsearch (central data store)", font)
text(980, 270, "All tools query this DB", font_small)

# arrows from AgentTools -> Elasticsearch
arrow_color = (15, 23, 42)
# arrow line
d.line([(880, 260), (960, 260)], fill=arrow_color, width=3)
# arrowhead
d.polygon([(955, 255), (965, 260), (955, 265)], fill=arrow_color)

# arrows from AgentTools -> Data (dashed)
for i, y in enumerate([230, 260, 290]):
    d.line([(760, 320 + i * 10), (360, 320 + i * 10)], fill=(100, 100, 100), width=1)

# Legend
rect(60, 520, 360, 240, BOX_FILL)
text(80, 545, "Legend", font)
text(80, 570, "Folder / package: blue background", font_small)
text(80, 590, "Files / modules: light background", font_small)
text(80, 610, "Virtualenv: pink background (ignored)", font_small)
text(80, 630, "Note: app.py is intentionally omitted", font_small)

# small border
d.rectangle([2, 2, WIDTH - 3, HEIGHT - 3], outline=(220, 220, 220))

# Save
img.save("project_structure.png")
print("project_structure.png written")
