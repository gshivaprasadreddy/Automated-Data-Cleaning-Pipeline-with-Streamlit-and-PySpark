import os

def validate_file(file_path):
    max_size_mb = 500  # Maximum file size in MB
    allowed_extensions = ["csv", "json", "parquet", "orc"]  # Supported file types

    # Check file size
    if os.path.getsize(file_path) > max_size_mb * 1024 * 1024:
        return False, "File size exceeds the maximum limit of 500MB."

    # Check file extension
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        return False, "Unsupported file type. Please upload a .csv, .json, .parquet or .orc file."

    return True, None
