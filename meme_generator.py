from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_meme(template_path, caption, output_path):
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("impact.ttf", size=40)
    except:
        font = ImageFont.load_default()

    # Wrap text
    wrapped = textwrap.fill(caption, width=25)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]


    # Center text horizontally
    x = (img.width - text_width) / 2
    # Position text at bottom
    y = img.height - text_height - 20

    # Draw text with outline
    draw.multiline_text((x, y), wrapped, font=font, fill='white',
                        stroke_width=2, stroke_fill='black')

    img.save(output_path)
    print(f"Meme saved to {output_path}")
