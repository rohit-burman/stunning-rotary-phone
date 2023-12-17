# New York Times News Scraper

This Python script allows you to scrape information from news articles on The New York Times website. It extracts details such as the article title, author, date, and its content.

## Usage
open terminal and replace news_url with any nytimes article url.

Example url `https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html`
         `https://www.nytimes.com/2023/10/03/sports/cricket/cricket-world-cup-explained.html`
         
```bash
python scraper_main.py news_url
```
### Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `argparse`

Install the required packages using:

```bash
pip install requests beautifulsoup4
```
