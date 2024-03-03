import tkinter as tk
from PIL import Image, ImageTk
import os
import itertools
import random  # Import the random module

def update_image():
    global img_label, image_files, root

    # Move to the next image
    img_path = next(image_files)
    
    # Open the image file
    img = Image.open(img_path)

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Resize the image to fit the screen while maintaining aspect ratio
    img.thumbnail((screen_width, screen_height), Image.Resampling.LANCZOS)

    photo = ImageTk.PhotoImage(img)

    # Update the label with the new image
    img_label.configure(image=photo)
    img_label.image = photo

    # Set the timer to update the image after 5 seconds
    root.after(5000, update_image)

def exit_fullscreen(event):
    root.destroy()  # Closes the application

# Initialize Tkinter
root = tk.Tk()
root.title('Slideshow')

# Remove the window title bar and border, making it borderless and fullscreen
root.overrideredirect(True)  # This removes the title bar and makes the window borderless
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Bind the Escape key to exit the fullscreen mode
root.bind('q', exit_fullscreen)
root.bind('Q', exit_fullscreen)

# Create a label to display images
img_label = tk.Label(root)
img_label.pack(expand=True, fill='both')

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
