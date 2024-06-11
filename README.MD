# Multi-threaded Web Scraper

## Overview
This project is a multithreaded web scraper developed in Python. It scrapes data from a publicly available e-commerce website and stores the extracted information in a PostgreSQL database. The scraper is designed to efficiently handle multiple pages concurrently using threading and ensures robust error handling and logging throughout the process.



## Setup

### Step 1: Clone the Repository

Clone the project repository from GitHub to your local machine:

```sh
git clone https://github.com/Akshayparihar07/Multithreaded_Web_Scraper.git
cd multithreaded_web_scraper
```

### Step 2: Set up a Virtual Enviornment (optional)

Create and activate a virtual environment to manage project dependencies:

```sh
python -m venv venv
source venv\Scripts\activate
```

### Step 3: Install Dependencies

#### Necessary Dependencies
1. `BeautifulSoup`
2. `Requests`
3. `SQLAlchemy`
4. `Logging`
5. `Threading`

**Install Necessay Dependencies**: 
```sh
pip install BeautifulSoup Requests SQLAlchemy Logging Threadig
```

Install All the other required Python packages listed in the `requirements.txt` file:

```sh
pip install -r rquirements.txt
```

### Step 4: Configure the PostgreSQL database

Set up a PostgreSQL database and updates the `DATABASE_URL` in `models.py` with their database credentials:

```python
DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/<db_name>"
```

### Step 5: Execute the scraper script

Run the scraper script to start scraping data:

```sh
python scraper.py
```
*Note: You can Modify the URLs as Per you need in the `scraper.py` file*

### Step 6: Reviewing the Output in the PostgreSQL database

Open PGAdmin4 or You Prefered Database management tool and run the following command in the SQL console:

```sql
SELECT * FROM products;
```

## Project Features and Functionalities

### Code Quality:
- The Code Base Follows all the [PEP8](https://peps.python.org/pep-0008/) Guidelines that are mentioned in the [Python's Offical Documentation](https://www.python.org/doc/) with Clear and Consice Appropriate Comments and Meaningful variable Names 
- Creation of Data Models using `SQLAlchemyy` in a Saperate File

### Functionality:
- Ensured multithreading with proper usage of Downtimes using 'threading' module.
- Presistent Data Storage in the PostgresSQL database

### Logging
- Logging Every Step from Model Creation to Scraping Data - Every Detail of the Scraping Process will be Recorded in the `logs.log` file

### Robustness:
- Comprehensive and Selfexplainatory errors to ensure robust Error Handeling
- Testing: Testing Assertion for Null values, Invalid URLs and None Data feilds

## Project Author
[Akshay Parihar](https://www.github.com/Akshayparihar07)