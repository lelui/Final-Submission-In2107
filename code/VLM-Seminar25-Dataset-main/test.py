import json
import os
import random
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

# ====== Configuration ======
FOLDER = './chest_xrays'
ANNOTATIONS_PATH = os.path.join(FOLDER, 'annotations_len_50.json')
IMAGES_PATH = os.path.join(FOLDER, 'images')
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # fallback to default if not found
FONT_SIZE = 32
FIG_SIZE = (10, 5)
BASE_COLORS = ['#ff9999', '#99ccff', '#99ff99', '#ffcc99', '#cc99ff', '#99ffff', '#ff99ff', '#ffff99']


# ====== Helper Functions ======
def draw_text(draw, pos, text, font, color, outline=2):
    for dx in [-outline, outline]:
        for dy in [-outline, outline]:
            draw.text((pos[0] + dx, pos[1] + dy), text, font=font, fill='black')
    draw.text(pos, text, font=font, fill=color)


def get_color(label, color_map):
    if label not in color_map:
        if len(color_map) < len(BASE_COLORS):
            color_map[label] = BASE_COLORS[len(color_map)]
        else:
            color_map[label] = tuple(np.random.rand(3, ))
    return color_map[label]


def visualize_sample(img_id, ann, color_map):
    img_file = os.path.join(IMAGES_PATH, img_id + '.png')
    if not os.path.exists(img_file):
        print(f"Image not found: {img_file}")
        return None

    img = Image.open(img_file).convert("RGB")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    for x1, y1, x2, y2, label in ann.get('bbox_2d', []):
        color = get_color(label, color_map)
        for w in range(6):
            draw.rectangle([x1 - w, y1 - w, x2 + w, y2 + w], outline=color)
        bbox_text = draw.textbbox((0, 0), label, font=font)
        text_w = bbox_text[2] - bbox_text[0]
        text_h = bbox_text[3] - bbox_text[1]
        text_pos = (x1, y2 + 10) if y1 < 50 else (x1, y1 - text_h - 10)
        draw_text(draw, text_pos, label, font, color)

    return img


# ====== Main Execution ======
with open(ANNOTATIONS_PATH) as f:
    annotations = json.load(f)

healthy_keys = [k for k, v in annotations.items() if v['status'] == 'healthy']
unhealthy_keys = [k for k, v in annotations.items() if v['status'] == 'unhealthy']

sample_keys = []
if healthy_keys:
    sample_keys.append(random.choice(healthy_keys))
if unhealthy_keys:
    sample_keys.append(random.choice(unhealthy_keys))

color_map = {}

fig, axes = plt.subplots(1, len(sample_keys), figsize=FIG_SIZE)
if len(sample_keys) == 1:
    axes = [axes]

for i, key in enumerate(sample_keys):
    ann = annotations[key]
    img = visualize_sample(key, ann, color_map)
    if img:
        axes[i].imshow(img)
        gd = ann.get('global_disease')
        gd_text = ', '.join(gd) if gd else 'null'
        axes[i].set_title(f"ID: {key}\nStatus: {ann['status']}\nGlobal Disease: {gd_text}", fontsize=16)
        axes[i].axis('off')

plt.tight_layout()
plt.show()