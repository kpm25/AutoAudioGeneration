import os
from PIL import Image, ImageDraw, ImageFont

# List of words
words = ["elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "panda", "koala", "kangaroo", "hippopotamus"]

# Directory to save images
images_directory = "generated_images"
os.makedirs(images_directory, exist_ok=True)

# Function to clear the images directory
def clear_images_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Warning and user confirmation
print(f"Warning: This will clear all files in the '{images_directory}' directory.")
confirmation = input("Do you want to continue? (yes/no): ").strip().lower()

if confirmation == 'yes':
    clear_images_directory(images_directory)
    print(f"Cleared the '{images_directory}' directory.")
else:
    print("Operation cancelled.")
    exit()

# Function to generate an image with text
def generate_image(text, path):
    # Create a blank image with white background
    img = Image.new('RGB', (200, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Use a basic font
    font = ImageFont.load_default()

    # Position the text in the center
    text_bbox = d.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # Add text to image
    d.text(position, text, fill=(0, 0, 0), font=font)

    # Save the image
    img.save(path)

# Generate images for each word
for word in words:
    filename = f"{images_directory}/{word}.png"
    generate_image(word, filename)
    print(f"Generated: {filename}")