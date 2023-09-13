import os
import shutil

# Define the source and destination folders
source_folder = r'C:\Users\Mahadi Saym\Desktop\imran\images'
destination_folder = r'F:\after delete place it here'

# List of image file names to move
image_files_to_move = [
    "IMG_20230726_145841.jpg",
    "IMG_20230715_173559.jpg",
    "IMG_20230715_174157.jpg",
    "IMG_20230619_121427.jpg",
    "IMG_20230610_125707.jpg",
    "IMG_20230715_174145.jpg",
    "IMG_20230611_183949.jpg",
    "IMG_20230715_173932.jpg",
    "IMG_20230715_172748.jpg",
    "IMG_20230715_173220.jpg",
    "IMG_20230714_205001.jpg",
    "IMG_20230619_084947.jpg",
    "IMG_20230715_173924.jpg",
    "IMG_20230715_173308.jpg",
    "IMG_20230715_172822.jpg",
    "IMG_20230715_172825.jpg",
    "IMG_20230715_172820.jpg",
    "IMG_20230715_172845.jpg",
    "IMG_20230715_174025.jpg",
    "IMG_20230619_084656.jpg",
    "IMG_20230715_173935.jpg",
    "IMG_20230619_121430.jpg",
    "IMG_20230715_173311.jpg",
    "IMG_20230610_125720.jpg",
    # Add more file names here
]

try:
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through the image files and move them
    for image_file in image_files_to_move:
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(destination_folder, image_file)
        
        # Check if the file exists in the source folder before moving
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Moved: {image_file}")
        else:
            print(f"File not found in source folder: {image_file}")

    print("All selected images have been moved.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
