def prepare_datasets():
    import os
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Define paths for datasets
    sms_data_path = 'path/to/sms_dataset.csv'  # Update with actual path
    image_data_path = 'path/to/image_dataset.csv'  # Update with actual path

    # Load SMS dataset
    sms_data = pd.read_csv(sms_data_path)
    sms_train, sms_test = train_test_split(sms_data, test_size=0.2, random_state=42)

    # Save prepared SMS datasets
    sms_train.to_csv('path/to/prepared_sms_train.csv', index=False)  # Update with actual path
    sms_test.to_csv('path/to/prepared_sms_test.csv', index=False)  # Update with actual path

    # Load image dataset
    image_data = pd.read_csv(image_data_path)
    image_train, image_test = train_test_split(image_data, test_size=0.2, random_state=42)

    # Save prepared image datasets
    image_train.to_csv('path/to/prepared_image_train.csv', index=False)  # Update with actual path
    image_test.to_csv('path/to/prepared_image_test.csv', index=False)  # Update with actual path

    print("Datasets prepared and saved successfully.")

if __name__ == "__main__":
    prepare_datasets()