import os
import requests
import zipfile
import pandas as pd

def download_sms_dataset(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded dataset to {save_path}")
    else:
        print(f"Failed to download dataset from {url}")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

def prepare_sms_data(extracted_folder):
    # Assuming the dataset contains a CSV file named 'sms_data.csv'
    csv_file = os.path.join(extracted_folder, 'sms_data.csv')
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        # Perform any necessary preprocessing here
        print("Prepared SMS data:")
        print(df.head())
        return df
    else:
        print(f"No CSV file found in {extracted_folder}")
        return None

def main():
    sms_dataset_url = "https://example.com/path/to/sms_dataset.zip"  # Replace with actual URL
    zip_save_path = "sms_dataset.zip"
    extract_folder = "sms_data"

    download_sms_dataset(sms_dataset_url, zip_save_path)
    extract_zip(zip_save_path, extract_folder)
    sms_data = prepare_sms_data(extract_folder)

if __name__ == "__main__":
    main()