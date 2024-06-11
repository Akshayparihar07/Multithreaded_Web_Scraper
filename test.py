import unittest
from scraper import scrape_page


class TestScraper(unittest.TestCase):
    """
    Test case for the scrape_page function.
    """

    def test_scrape_page_success(self):
        """
        Test successful scraping of a page.
        """
        url = 'https://books.toscrape.com/catalogue/soumission_998/index.html'
        result = scrape_page(url)
        self.assertIsNotNone(result)

    def test_scrape_page_invalid_url(self):
        """
        Test scraping with an invalid URL.
        """
        url = 'https://invalidurl.com'
        result = scrape_page(url)
        self.assertIsNone(result)

    def test_scrape_page_missing_price(self):
        """
        Test scraping a page where the price is missing.
        """
        url = 'https://books.toscrape.com/catalogue/some-product-without-price.html'
        result = scrape_page(url)
        self.assertIsNotNone(result)

    def test_scrape_page_missing_rating(self):
        """
        Test scraping a page where the rating is missing.
        """
        url = 'https://books.toscrape.com/catalogue/some-product-without-rating.html'
        result = scrape_page(url)
        self.assertIsNotNone(result) 

    def test_scrape_page_missing_review_count(self):
        """
        Test scraping a page where the review count is missing.
        """
        url = 'https://books.toscrape.com/catalogue/some-product-without-reviews.html'
        result = scrape_page(url)
        self.assertIsNotNone(result)  

    def test_scrape_page_invalid_content(self):
        """
        Test scraping a page with invalid HTML content.
        """
        url = 'https://books.toscrape.com/catalogue/some-product-with-invalid-html.html'
        result = scrape_page(url)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
