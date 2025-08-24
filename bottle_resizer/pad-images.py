from PIL import Image
import os

# --- CONFIG ---
input_folder = "input_images"
output_folder = "output_images"
target_width = 250       # final canvas width
target_height = 550      # final canvas height
bg_color = (255, 255, 255, 0)  # transparent background
save_as_png = True

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    img_path = os.path.join(input_folder, filename)
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size

    # --- create canvas with fixed size ---
    canvas = Image.new("RGBA", (target_width, target_height), bg_color)

    # --- calculate offsets ---
    x_offset = (target_width - w) // 2        # center horizontally
    y_offset = target_height - h              # align bottom

    # --- paste original image at bottom ---
    canvas.paste(img, (x_offset, y_offset), img)

    # --- save ---
    out_name = os.path.splitext(filename)[0] + (".png" if save_as_png else ".jpg")
    out_path = os.path.join(output_folder, out_name)

    if save_as_png:
        canvas.save(out_path, optimize=True)
    else:
        canvas.convert("RGB").save(out_path, quality=95, optimize=True)

    print(f"Saved {out_path}")

print("All images processed!")
