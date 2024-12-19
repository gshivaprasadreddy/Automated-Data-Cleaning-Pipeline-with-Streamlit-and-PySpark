import os
import streamlit as st
from pyspark.sql import SparkSession
from utils.file_validation import validate_file
from utils.data_cleaning import clean_data
from utils.logging_utils import log_changes

# Constants
UPLOAD_FOLDER = "uploads/"
DOWNLOAD_FOLDER = "downloads/"

# Create necessary folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Cleaning App") \
    .getOrCreate()

# Streamlit App
st.title("Automated Data Cleaning Application")

# File Upload Section
st.header("1. Upload File")
uploaded_file = st.file_uploader("Upload a .csv, .json, .parquet or .orc file", type=["csv", "json", "parquet", "orc"])
if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"File {uploaded_file.name} uploaded successfully!")

# Validation and Cleaning Section
if st.button("Validate and Clean"):
    if uploaded_file:
        # Validate file
        validation_result, error = validate_file(file_path)
        if not validation_result:
            st.error(error)
        else:
            # Read and clean data using PySpark
            try:
                cleaned_data, logs = clean_data(spark, file_path)

                log_file_path = os.path.join(DOWNLOAD_FOLDER, "cleaning_log.txt")
                cleaned_file_path = os.path.join(DOWNLOAD_FOLDER, "cleaned_file.csv")

                # Convert PySpark DataFrame to Pandas for Streamlit display
                cleaned_data_pd = cleaned_data.toPandas()

                # Save cleaned data and logs
                cleaned_data_pd.to_csv(cleaned_file_path, index=False)
                with open(log_file_path, "w") as log_file:
                    log_file.write("\n".join(logs))

                st.success("Data cleaned successfully!")
                st.write("Preview of cleaned data:")
                st.dataframe(cleaned_data_pd.head(50))

                st.download_button("Download Cleaned File", open(cleaned_file_path, "rb"), file_name="cleaned_file.csv")
                st.download_button("Download Log File", open(log_file_path, "rb"), file_name="cleaning_log.txt")
            except Exception as e:
                st.error(f"Error during cleaning: {e}")
    else:
        st.error("Please upload a file first!")
