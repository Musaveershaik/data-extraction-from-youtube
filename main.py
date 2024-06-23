# Import necessary libraries
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Define the path to your Edge WebDriver executable (adjust accordingly)
path = "C:/Users/Musaveer/Downloads/edgedriver_win64/msedgedriver.exe"

# Target YouTube channel URL (replace with the desired channel)
website = "https://www.youtube.com/@Channel_Name/videos"

# Set browser options for maximized window
edge_options = Options()
edge_options.add_argument("--start-maximized")

# Create Edge service object
service = Service(executable_path=path)

# Initialize Edge WebDriver with options
driver = webdriver.Edge(service=service, options=edge_options)

# Open the target YouTube channel page
driver.get(website)

# Scroll down the page twice to ensure all videos are loaded
total_scrolls = 2
for _ in range(total_scrolls):
    # Find the body element and simulate user scrolling to the bottom
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    # Wait for 3 seconds to allow content loading after each scroll
    time.sleep(3)

# Get the entire page source code
html = driver.page_source

# Close the browser window (optional)
driver.quit()  # Uncomment this line to close the browser after scraping

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Identify video elements using the appropriate selector (adjust if needed)
videos = soup.find_all('div', {"id": "dismissible"})

# Create an empty list to store extracted data
master_list = []

# Iterate through each video element
for video in videos:
    # Create a dictionary to store video data
    data_dict = {}

    # Extract video title using a clear selector (adjust if needed)
    data_dict['video_title'] = video.find('a', {"id": "video-title-link"}).text.strip()

    # Construct the full video URL using base YouTube URL and extracted link
    data_dict['video_url'] = 'https://www.youtube.com' + video.find('a', {"id": "video-title-link"})['href']

    # Find the metadata container using a descriptive selector (adjust if needed)
    meta = video.find('div', {'id': 'metadata-line'}).find_all('span')

    # Extract and clean view count (consider error handling for non-numeric cases)
    views_text = meta[0].text.strip()
    if 'K' in views_text:
        views = float(views_text.split('K')[0]) * 1000
    elif 'M' in views_text:
        views = float(views_text.split('M')[0]) * 1000000
    else:
        views = int(views_text)  # Handle cases without "K" or "M" (may need adjustment)
    data_dict['views'] = views

    # Extract and clean video upload date (consider handling different formats)
    data_dict['video_Age'] = meta[1].text.strip()

    # Append the extracted data dictionary to the master list
    master_list.append(data_dict)

# Create a Pandas DataFrame from the extracted data
youtube_dataframe = pd.DataFrame(master_list)

# Specify the CSV file path for saving the data (adjust as needed)
file_path = 'FileName.csv'

# Save the DataFrame to a CSV file
youtube_dataframe.to_csv(file_path, index=False)

# Optional: Add functionality for handling view count abbreviations within DataFrame

print("Data extraction complete! Check the CSV file for results.")
