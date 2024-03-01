# pip install pillow
# pip install tk

import tkinter as tk
from PIL import Image, ImageTk
import os
import itertools
import random  # Import the random module

# Function to update the image
def update_image():
    global img_label, image_files, root

    # Move to the next image
    img_path = next(image_files)
    
    # Open the image file
    img = Image.open(img_path)
    img = img.resize((500, 500), Image.Resampling.LANCZOS)  # Resize the image to fit the label
    photo = ImageTk.PhotoImage(img)

    # Update the label with the new image
    img_label.configure(image=photo)
    img_label.image = photo

    # Set the timer to update the image after 5 seconds
    root.after(5000, update_image)

# Initialize Tkinter
root = tk.Tk()
root.title('Slideshow')

# Set the geometry of the window
root.geometry("600x600")

# Create a label to display images
img_label = tk.Label(root)
img_label.pack()

# Specify the directory containing images
image_dir = 'ads/'
# List all image files in the directory
image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f)) and (f.endswith('.jpg') or f.endswith('.png'))]
# Shuffle the list of image paths
random.shuffle(image_paths)
# Create a cycle iterator from the shuffled list
image_files = itertools.cycle(image_paths)

# Start the slideshow
update_image()

# Start the Tkinter event loop
root.mainloop()

