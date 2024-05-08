import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_and_store(url, output_format):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the data you want to scrape
        # For example, let's say we want to scrape the titles of articles
        article_titles = soup.find_all('h2', class_='article-title')

        if output_format == 'csv':
            # Store data in CSV format
            with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Title'])  # Write header row
                for title in article_titles:
                    writer.writerow([title.text.strip()])  # Write title to CSV

            print("Data scraped and stored in data.csv")

        elif output_format == 'json':
            # Store data in JSON format
            data = {'articles': []}
            for title in article_titles:
                data['articles'].append({'title': title.text.strip()})

            with open('data.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, ensure_ascii=False, indent=4)

            print("Data scraped and stored in data.json")

        else:
            print("Unsupported output format. Please choose 'csv' or 'json'.")
    else:
        print("Error fetching URL:", response.status_code)

# Example usage
url = 'https://google.com'  # URL of the website to scrape
output_format = 'json'  # Output format: 'csv' or 'json'
scrape_and_store(url, output_format)
