from pathlib import Path
from PIL import Image
import io

with Image.open('C:/Users/Shirin Sabuwala/Desktop/Shirin/IITM/Diploma Level/TDS/compressed image 1.png') as img:
    # Convert RGBA to RGB if needed
    if img.mode == 'RGBA':
        img = img.convert('RGB')
        # Optimize for web
    img.save('C:/Users/Shirin Sabuwala/Desktop/Shirin/IITM/Diploma Level/TDS/compressed image.png', 'WEBP', lossless=True, optimize=True)