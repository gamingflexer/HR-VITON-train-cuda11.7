import os
import itertools
import random
import sys
input_path = sys.argv[1]
pair_name = sys.argv[2] 
save_path = input_path.replace(f"{pair_name}/image","")

image_files = os.listdir(os.path.join(input_path))
print(image_files)
id_map = {}
for img in image_files:
  id = img.split("_")[0]
  if id not in id_map:
    id_map[id] = []
  id_map[id].append(img)

unique_pairs = [] 
for id, img_list in id_map.items():
  if len(img_list) > 1:
    pairs = list(itertools.combinations(img_list, 2))
    unique_pairs.extend(pairs)
  elif len(img_list) == 1:  
    unique_pairs.append(img_list*2)


output = []
unquine_images = image_files

for pair in unique_pairs:
    if pair[0] == pair[1]:
        replace = random.choice(unquine_images)
        if replace != pair[0]:
            output.append([pair[0], replace])
            unquine_images.pop(unquine_images.index(replace))
    else:
        output.append(pair)
        
# Write pairs 
with open(os.path.join(save_path, f'{pair_name}_pairs.txt'), 'w') as f:
  for pair in output:
    f.write(f"{pair[0]} {pair[1]}\n") 

print("Pairs file generated.")