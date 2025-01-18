# Table Detection and OCR with Transformers

This project is a Streamlit app for detecting tables in images, cropping them, detecting cells within the cropped tables, and applying OCR (Optical Character Recognition) to extract the table data into a CSV file.

## Directory Structure

The project is structured as follows:


streamlit_table_app/

├── app.py

├── requirements.txt

├── utils/

│ ├── model.py

│ ├── preprocessing.py

│ ├── detection.py

│ ├── visualization.py

│ ├── ocr.py


### app.py

This file is the main entry point for the Streamlit app. It handles the user interface, image upload, and the sequence of steps from table detection to OCR and saving results.

### Main Features:
- Upload an image containing a table.
- Detect and visualize tables in the image.
- Crop detected tables and visualize them.
- Detect and visualize cells within the cropped tables.
- Perform OCR on the cells to extract table data.
- Save the extracted data as a CSV file.

### requirements.txt

This file lists all the dependencies required for the project.

#### Dependencies:
- streamlit
- transformers
- torch
- Pillow
- huggingface_hub
- matplotlib
- easyocr
- tqdm
- pandas

### utils/model.py

This file contains functions for loading the table detection and structure recognition models.

#### Functions:
- `load_detection_model()`: Loads the table detection model.
- `load_structure_model(device)`: Loads the structure recognition model.

### utils/preprocessing.py

This file contains functions for preparing images to be compatible with the models.

#### Functions:
- `prepare_image(image, device)`: Prepares and normalizes the image for the table detection model.
- `prepare_cropped_image(cropped_image, device)`: Prepares and normalizes the cropped table image for the structure recognition model.

### utils/detection.py

This file contains functions for detecting tables and cells in the images.

#### Functions:
- `detect_tables(model, pixel_values)`: Uses the table detection model to detect tables.
- `detect_cells(model, pixel_values)`: Uses the structure recognition model to detect cells within cropped tables.

### utils/visualization.py

This file contains functions for visualizing detected tables and cells.

#### Functions:
- `visualize_detected_tables(img, det_tables)`: Visualizes tables detected in the image.
- `plot_results(cells, class_to_visualize)`: Visualizes detected cells within the cropped table.

### utils/ocr.py

This file contains functions for applying OCR and saving the results as a CSV.

#### Functions:
- `apply_ocr(cell_coordinates, cropped_table)`: Performs OCR on detected cells to extract text.
- `save_csv(data)`: Saves the extracted table data into a CSV file.

## Installation

```sh
cd streamlit_table_app      # Navigate to the project directory
pip install -r requirements.txt  # Install dependencies

