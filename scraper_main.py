import requests
import argparse
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}


def extract_article_info(url):
    response = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title_element = soup.find('h1')
    # title=title_element.text.strip()
    title = title_element.text.strip() if title_element else "Title not found"
    # print(title)

        # Extract author
    author_element = soup.find('a', {'class': 'css-n8ff4n e1jsehar0'})
    author = author_element.text.strip() if author_element else "Author not found"
    # print(author)

    #     # Extract date
    date_element = soup.find('div', {'data-testid': 'reading-time-module'})
    date = date_element.text.strip() if date_element else "Date not found"
    # print(date)

    #     # Extract content
    content_elements = soup.find_all('div', {'class': 'css-53u6y8'})
    content = "\n".join([element.text.strip() for element in content_elements])
    # print(content)

    
    article_info = {
            "title": title,
            "author": author,
            "date": date,
            "content": content
        }
    return article_info



def main():

    parser = argparse.ArgumentParser(description="Scrape news article information from The New York Times URL.")

    parser.add_argument("nytimes_url", help="URL of the news article from New York Times")
    args = parser.parse_args()
    article_info = extract_article_info(args.nytimes_url)

    # article_url = "https://www.nytimes.com/2023/10/03/sports/cricket/cricket-world-cup-explained.html?searchResultPosition=1"
    # article_info = extract_article_info(article_url)

    if article_info:
        print("Article Information:")
        print(f"\t\t\t\tTitle: {article_info['title']}")
        print(f"\tAuthor: {article_info['author']}",end=" ")
        print(f"\t\t\t\t\t\tDate: {article_info['date']}")
        print("\n\n\n\nContent:\n", article_info['content'])


if __name__ == "__main__":
    main()