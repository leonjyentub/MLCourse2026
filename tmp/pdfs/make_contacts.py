from pathlib import Path
from PIL import Image, ImageDraw


for folder in ("qa_01", "qa_02", "qa_03"):
    source = Path(__file__).parent / folder
    pages = sorted(source.glob("page-*.jpg"))
    thumb_w, thumb_h = 320, 180
    label_h, cols = 24, 5
    rows = (len(pages) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, page in enumerate(pages):
        image = Image.open(page).convert("RGB")
        image.thumbnail((thumb_w, thumb_h))
        x = (index % cols) * thumb_w
        y = (index // cols) * (thumb_h + label_h)
        sheet.paste(image, (x, y))
        draw.text((x + 4, y + thumb_h + 4), f"Page {index + 1}", fill="black")
    sheet.save(source / "contact.jpg", quality=90)
