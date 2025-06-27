from PIL import Image
import pandas as pd

# === CONFIG ===
image_path = "a12.webp"       # The full 5x5 scrambled image
mapping_file = "a12_mapping.tsv"            # CSV with original vs current positions
output_path = "reconstructed_image.png" # Output image
grid_size = 5

# === Load Image & Mapping ===
img = Image.open(image_path).convert("RGB")
mapping = pd.read_csv(mapping_file, sep = "\t")
print(mapping)

# Calculate piece size
piece_width = img.width // grid_size
piece_height = img.height // grid_size
#print(piece_width, piece_height)

# Create a blank canvas for the output image
reconstructed = Image.new("RGB", (img.width, img.height))

# === Rebuild ===
for index, row in mapping.iterrows():
    orig_row, orig_col = int(row['Original Row']), int(row['Original Column'])
    curr_row, curr_col = int(row['Scrambled Row']), int(row['Scrambled Column'])

    # Crop the current tile from the scrambled image
    left = curr_col * piece_width
    upper = curr_row * piece_height
    right = left + piece_width
    lower = upper + piece_height
    tile = img.crop((left, upper, right, lower))

    # Paste it into its original position
    x_dest = orig_col * piece_width
    y_dest = orig_row * piece_height
    reconstructed.paste(tile, (x_dest, y_dest))

# Save the reassembled image
reconstructed.save(output_path, format='PNG')
print(f"✅ Reconstructed image saved to: {output_path}")
