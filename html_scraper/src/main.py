import os
import sqlite3
from scraper_vuokraovi import VuokraoviScraper
from scraper_vuokraovi import VuokraoviDriver
from scraper_vuokraovi import VuokraoviParser
from functools import partial


def main():
    vuokraovi_url = os.environ['VUOKRAOVI_URL']

    conn = sqlite3.connect('/data/html.db')
    cur = conn.cursor()

    try:
        with VuokraoviDriver(vuokraovi_url) as driver:
            VuokraoviScraper.scrape_ads(
                driver,
                partial(insert_to_db, cur, lambda _a, _b: None),
                1,
                1
            )

            end_page = min(
                VuokraoviParser.get_max_pagenumber(driver.get_page(1)),
                100
            )

            if end_page > 1:
                VuokraoviScraper.scrape_ads(
                    driver,
                    partial(insert_to_db, cur, raise_duplicate_error),
                    2,
                    end_page
                )
    except DuplicateValueError as error:
        # We just want to exit gracefully, as we have encountered a duplicate
        return
    finally:
        conn.commit()
        conn.close()


def insert_to_db(conn, duplicate_callback, url, html):
    # Assume urls are unique for a year, and find if duplicate exists:
    conn.execute("""
    select count(1) from etuovi
    where insert_ts > datetime(CURRENT_TIMESTAMP, '-365 days')
    and url=?
    """, (url,))

    if conn.fetchone()[0] > 0:
        duplicate_callback(url, html)
    else:
        conn.execute("insert into etuovi (url, html) values (?, ?)",
                     (url, html))


def raise_duplicate_error(_a, _b):
    raise DuplicateValueError


class DuplicateValueError(Exception):
    pass


if __name__ == '__main__':
    main()
