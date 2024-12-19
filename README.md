# Automated Data Cleaning Application

## Overview
The **Automated Data Cleaning Application** is a robust and user-friendly tool designed to streamline the process of cleaning and validating large datasets. Built with **Streamlit** for the frontend and **PySpark** for backend processing, this application provides advanced data cleaning capabilities, seamless file validation, and detailed logging to ensure high-quality datasets.

---

## Features

### 1. File Upload and Validation
- Supports multiple file formats: **CSV**, **JSON**, **Parquet**, and **ORC**.
- Validates file size (maximum limit of 500MB).
- Ensures compatibility by checking file extensions.

### 2. Data Cleaning Capabilities
- **Handling Missing Values**:
  - Replaces invalid integers with `-1`.
  - Replaces invalid strings with "invalid".
- **Shorthand Conversion**:
  - Converts numeric shorthand (e.g., `1.2k`, `4M`) into full numeric values.
  - Removes commas from numeric fields (e.g., `1,000` to `1000`).
- **Whitespace Trimming**:
  - Strips leading and trailing whitespaces in text fields.
- **Duplicate Removal**:
  - Identifies and drops duplicate rows.
- **Case Standardization**:
  - Converts all text fields to lowercase.
- **Date Formatting**:
  - Converts date fields into `YYYY-MM-DD` format while logging invalid date values.
- **Empty Rows and Columns Handling**:
  - Removes rows and columns that are completely empty.
- **Invalid Value Normalization**:
  - Dynamically replaces invalid or inconsistent values with appropriate placeholders.

### 3. Logging and Downloadable Outputs
- Generates detailed cleaning logs for user review.
- Allows users to preview cleaned data directly in the app.
- Enables downloading of cleaned files and logs.

---

## How It Works

### 1. Upload Your File
- Use the upload section to select a file in supported formats.

### 2. Validate and Clean Data
- Click the "Validate and Clean" button.
- The application validates the file and cleans it using PySpark, ensuring:
  - Removal of irrelevant data.
  - Consistent and normalized column data types.

### 3. Download Results
- Once cleaning is complete, preview the first 50 rows of the cleaned dataset.
- Download the cleaned file and logs for further review.

---

## Technical Details

### Frontend
- **Streamlit**: Provides an intuitive web-based interface.

### Backend
- **PySpark**: Handles large-scale data processing and cleaning.

### Directory Structure
```
project_root/
|
|-- app.py                # Main application script
|-- utils/
|    |-- file_validation.py # File validation logic
|    |-- data_cleaning.py   # Data cleaning logic
|    |-- logging_utils.py   # Log generation logic
|
|-- uploads/             # Directory for uploaded files
|-- downloads/           # Directory for cleaned files and logs
```

---

## Prerequisites
- **Python 3.7+**
- **PySpark**
- **Streamlit**

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at `http://localhost:8501`.

---

## Future Enhancements
- Add support for more file formats.
- Integrate machine learning for anomaly detection in datasets.
- Expand cleaning options to include advanced statistical techniques.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.


