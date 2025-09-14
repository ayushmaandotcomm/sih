import os
import requests
from tqdm import tqdm

def download_images(image_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in tqdm(image_urls, desc="Downloading images"):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an error for bad responses
            filename = os.path.join(save_dir, url.split("/")[-1])
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")

def main():
    # Example list of image URLs (replace with actual URLs)
    image_urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        # Add more URLs as needed
    ]
    save_dir = "downloaded_images"
    download_images(image_urls, save_dir)

if __name__ == "__main__":
    main()