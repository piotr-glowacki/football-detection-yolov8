import os
from pycocotools.coco import COCO

folders = ["train", "test", "val"]

for fol in folders:
    # Path to the COCO JSON file
    coco_json_path = f'data/{fol}/_annotations.coco.json'
    # Directory where the YOLO formatted annotation files will be stored
    yolo_annots_dir = f'data/{fol}/labels/'

    # Initialize COCO api for instance annotations
    coco = COCO(coco_json_path)

    # Get all image ids and load their information
    image_ids = coco.getImgIds()
    images = coco.loadImgs(image_ids)

    for image in images:
        filename = image['file_name']
        image_id = image['id']
        ann_ids = coco.getAnnIds(imgIds=image_id)
        annotations = coco.loadAnns(ann_ids)

        # Open a new file in the annots directory for this image
        with open(os.path.join(yolo_annots_dir, filename.replace('.jpg', '.txt')), 'w') as f:
            for ann in annotations:
                # COCO to YOLO Conversion:
                # Calculate x_center, y_center, width, and height
                x_center = (ann['bbox'][0] + ann['bbox'][2]/2) / image['width']
                y_center = (ann['bbox'][1] + ann['bbox'][3]/2) / image['height']
                width = ann['bbox'][2] / image['width']
                height = ann['bbox'][3] / image['height']

                # Write to file
                f.write(f"{ann['category_id']} {x_center} {y_center} {width} {height}\n")

    print(f"Conversion completed for {fol} folder.")
