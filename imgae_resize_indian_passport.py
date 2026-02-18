# Resizing and compressing uploaded image to 630x810 pixels and under 240KB
from PIL import Image
import os

# Define input and output paths
input_path = "C:\\Users\\sgidd\\Desktop\\Passport\\2026-01-26 - sgidd.jpg"
output_path = "C:\\Users\\sgidd\\Desktop\\Passport\\Someshwarpassport-resized_upload.jpg"

# Open the image
img = Image.open(input_path)

# Resize the image
#resized_img = img.resize((630, 810), Image.LANCZOS)

# Compress the image to be under 240KB
quality = 95
while True:
    img.save(output_path, format="JPEG", quality=quality)
    if os.path.getsize(output_path) <= 240 * 1024 or quality <= 20:
        break
    quality -= 5

print(f"Image resized to 630x810 and compressed to under 240KB. Saved as {output_path}")

