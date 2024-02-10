# This script is mostly generated by chatgpt. As this project is about
# neural networks, I want to spend time working on the network, and not
# in a program that generates training data.
# The objective of this script is to generate images of circles and
# squares with different positions and sizes, so I can train the neural
# network.

from PIL import Image, ImageDraw
import os
from math import ceil
import random

res = 16  # The image will be res x res pixels

def generate_shapes(shape, number_of_images):
    base_path = os.path.join(os.getcwd(), "training", shape + f"{res}x{res}")
    os.makedirs(base_path, exist_ok=True)

    for i in range(1, number_of_images + 1):
        img = Image.new('RGB', (res, res), 'black')
        draw = ImageDraw.Draw(img)

        if shape == 'squares':
            # Randomly determine size (2 to res / 2 pixels)
            size = random.randint(2, int(res / 2))
            # Ensure the square fits within the image bounds
            max_offset = res - size
            offset_x = random.randint(1, max_offset - 1)
            offset_y = random.randint(1, max_offset - 1)
            shape_outline = [offset_x, offset_y, offset_x + size, offset_y + size]
            draw.rectangle(shape_outline, outline='white', fill='white')
        
        elif shape == 'circles':
            # Randomly determine radius (2 to res / 4 pixels)
            radius = random.randint(max(1, ceil(res / 12)), int(res / 4))
            # Ensure the circle fits within the image bounds fully
            offset_x = random.randint(radius + 1, res - radius - 1)
            offset_y = random.randint(radius + 1, res - radius - 1)
            shape_outline = [offset_x - radius, offset_y - radius, offset_x + radius, offset_y + radius]
            draw.ellipse(shape_outline, outline='white', fill='white')

        filename = f"{shape}{i:04}.png"
        img.save(os.path.join(base_path, filename))

# Parameters
number_of_images_per_shape = 200  # Specify the desired number of images

generate_shapes('squares', number_of_images_per_shape)
generate_shapes('circles', number_of_images_per_shape)

print("Images generated successfully.")
