import os
import random

# Define the path to your image directory
image_dir = "./data/test/image"
type_data = image_dir.split("/")[-2]

# List all files in the directory
image_files = os.listdir(image_dir)

# Create a text file to write the output
output_file = f"./data/{type_data}_pairs.txt"

# Open the text file for writing
with open(output_file, "w") as file:
    # Create a list of image indices
    indices = list(range(len(image_files)))
    random.shuffle(indices)  # Shuffle the indices randomly

    for i in range(len(image_files)):
        # Calculate the index for the corresponding image name
        corresponding_index = indices[i]
        
        # Get the image names corresponding to the shuffled indices
        image_name1 = image_files[i]
        image_name2 = image_files[corresponding_index]
        
        # Write the pair to the text file
        file.write(f"{image_name1}  {image_name2}\n")

# Print a confirmation message
print(f"Output written to {output_file}")