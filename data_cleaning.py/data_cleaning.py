def clean_data(spark, file_path):
    """Main function to clean data and return cleaned DataFrame and logs."""
    logs = []

    try:
        # Read the input file
        logs.append(f"Reading input file: {file_path}")
        df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
    except Exception as e:
        logs.append(f"Error reading file: {e}")
        return None, logs

    # Apply data cleaning steps
    logs.append("Removing empty rows and columns.")
    df = remove_empty_rows_and_columns(df, logs)

    logs.append("Processing shorthand columns.")
    df = process_shorthand_columns(df, logs)

    logs.append("Formatting and filling values.")
    df = format_and_fill_values(df, logs)

    logs.append("Data cleaning completed successfully.")
    return df, logs
