import threading
import requests
import logging

from bs4 import BeautifulSoup

from models import SessionLocal, Product


# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_page(product_url):
    '''
    Scrape product details from a given URL and save the data to the database.
    Args:
        product_url (str): The URL of the product page to scrape.
    '''
    try:
        logging.info(f"Starting the scraping process for URL: {product_url}")

        # Fetch and parse the webpage content
        response = requests.get(product_url)
        response.raise_for_status()
        logging.info('HTTP request successful, data fetched from URL')

        product_page = BeautifulSoup(response.text, 'html.parser')
        logging.info('HTML content parsed successfully')

        # Extract product details
        product_title = product_page.find_all('h1')[0].string
        logging.info(f'Product title extracted: {product_title}')

        product_price = product_page.find('p', class_='price_color')
        product_price = product_price.string[2:] if product_price else None
        logging.info(f'Product price extracted: {product_price}')

        product_rating = product_page.find('p', class_='star-rating')
        product_rating = product_rating['class'][-1] if product_rating else None
        logging.info(f'Product rating extracted: {product_rating}')

        review_count = product_page.find('tr', class_='reviews')
        review_count = review_count.find('td').text.strip() if review_count else 0
        logging.info(f'Review count extracted: {review_count}')

        # Convert rating to a number if it is a string
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        product_rating = rating_map.get(product_rating, 0) if product_rating in rating_map else product_rating

        # Create a Product object and save it to the database
        product = Product(
            name=product_title,
            price=product_price,
            rating=product_rating,
            review_count=review_count,
            url=product_url
        )
        session = SessionLocal()
        session.add(product)
        session.commit()
        session.close()
        logging.info('Product data saved to the database successfully')



    except requests.HTTPError as e:
        logging.error(f'HTTP error occurred while fetching data from URL: {product_url} - {e}')
    except requests.RequestException as e:
        logging.error(f'Request exception occurred while accessing URL: {product_url} - {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred while processing URL: {product_url} - {e}')



def main(product_urls):
    '''
    Create and manage threads for scraping multiple product URLs.
    Args:
        product_urls (list): List of product URLs to scrape.
    '''
    threads = []
    for url in product_urls:
        thread = threading.Thread(target=scrape_page, args=(url,))
        threads.append(thread)
        thread.start()
        logging.info(f'Started scraping thread for URL: {url}')

    for thread in threads:
        thread.join()
        logging.info(f'Thread for URL completed: {thread.name}')



if __name__ == "__main__":
    product_urls = [
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
        "https://books.toscrape.com/catalogue/soumission_998/index.html",
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
        "https://books.toscrape.com/catalogue/the-requiem-red_995/index.html",
        "https://books.toscrape.com/catalogue/the-black-maria_991/index.html",
        "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html",
        "https://books.toscrape.com/catalogue/olio_984/index.html",
    ]
    main(product_urls)
