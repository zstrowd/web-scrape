# Web Scraping Light Novel Data

This project scrapes novel data from a website using Beautiful Soup, processes it, and stores the data in a CSV file for further use, such as building a machine learning model.

## Project Overview

The purpose of this project is to extract information about light novels from a website and save it in a structured format (CSV file). This data can later be used for analysis or building recommendation models, sentiment analysis, or other machine learning tasks.

### Key Features

- **Web Scraping**: Extracts novel information, including:
  - Novel title
  - Image URL
  - Status (e.g., Completed)
  - Rating (e.g., 5.0)
  - Categories (e.g., Action, Adventure, Horror, etc.)
- **Data Storage**: Stores the extracted data in a CSV file for further processing or machine learning model training.

## Tech Stack

- **Python**: Programming language used.
- **Beautiful Soup**: A Python library used for parsing HTML and web scraping.
- **CSV**: Data storage format used for organizing the scraped data.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- BeautifulSoup4
- Requests

You can install the required libraries using the following command:

```bash
pip install beautifulsoup4 requests
