# Extracting-Youtube-channel-Data

**Project Description**

**Title:** YouTube Channel Data Extractor

**Description:**

This Python project automates the extraction of valuable data from YouTube channels, specifically focusing on video titles, upload dates (video age), view counts, and video links. 

**Key Features:**

* **Reliable Data Extraction:** Utilizes the well-established BeautifulSoup library to parse YouTube channel HTML content effectively.
* **Efficient Scrolling:** Incorporates Selenium WebDriver (Edge in this example) for simulating user actions like scrolling down the page, ensuring all videos on the page are captured.
* **Clean and Organized Output:** The extracted data is stored in a well-formatted Pandas DataFrame, making it easy to export to a CSV file for further analysis or use in other applications.
* **View Count Conversion:** The script intelligently handles view counts that are displayed in abbreviated formats like "1.2K" or "3.4M," converting them to numerical values for easier manipulation.

**Benefits:**

* **Save Time and Effort:** This script automates the data extraction process, saving you significant time compared to manual data collection.
* **Improved Accuracy:** By automating the process, you can minimize the risk of errors that might occur during manual data entry.
* **Gain Valuable Insights:** The extracted data can be used for various purposes, such as analyzing video performance trends, identifying popular content, or conducting competitor research.

**Technical Specifications:**

* **Libraries Used:** BeautifulSoup, Selenium, Pandas
* **Output Format:** CSV file

**Example Usage:**

1. Replace the `website` variable with the URL of the specific YouTube channel you want to extract data from.
2. Make sure you have the necessary Selenium WebDriver executable (e.g., `msedgedriver.exe` for Edge) downloaded and placed in the appropriate location. Update the `path` variable accordingly.
3. Run the Python script.

**Customization:**

This script can be easily modified to accommodate different YouTube channel layouts and data extraction requirements. Feel free to adjust selectors and data parsing logic as needed.

**Note:**

* Be mindful of YouTube's Terms of Service regarding data scraping. Consider using the official YouTube Data API for larger-scale data extraction or if you need to comply with stricter usage guidelines.

I hope this enhanced description effectively highlights the project's functionalities and value proposition for potential clients on freelance platforms.
