import json
import csv

# Load the JSON data
with open('_annotations.coco.json', 'r') as f:
    data = json.load(f)

# Maps image_id -> {file_name, width, height}
image_map = {img['id']: img for img in data['images']}

# Maps category_id -> name
category_map = {cat['id']: cat['name'] for cat in data['categories']}

# The CSV output path
output_csv = 'shoe_annotations.csv'

# Process annotations and write to CSV
with open(output_csv, mode='w', newline='') as f:
    writer = csv.writer(f)
    
    # Define header
    writer.writerow(['filename', 'image_width', 'image_height', 'class', 'xmin', 'ymin', 'width', 'height'])

    for ann in data['annotations']:
        image_info = image_map.get(ann['image_id'])
        category_name = category_map.get(ann['category_id'])
        
        # COCO bbox format is [xmin, ymin, width, height]
        bbox = ann['bbox']
        xmin = int(float(bbox[0]))
        ymin = int(float(bbox[1]))
        width = int(float(bbox[2]))
        height = int(float(bbox[3]))

        writer.writerow([
            image_info['file_name'].split('.')[0].replace('_jpeg', '.jpeg').replace('_jpg', '.jpg'),  # Get just the filename
            image_info['width'],
            image_info['height'],
            category_name,
            xmin,
            ymin,
            width,
            height
        ])

print(f"Successfully created {output_csv} with {len(data['annotations'])} entries.")