import sqlite3
import scrape_vuokraovi
from functools import partial


def main():
    conn = sqlite3.connect('/data/html.db')
    cur = conn.cursor()

    try:
        scrape_vuokraovi.scrape_ads_from_first_page(
            partial(insert_to_db, cur, lambda _a, _b: None)
        )

        scrape_vuokraovi.scrape_ads_from_start_to_last_page(
            partial(insert_to_db, cur, raise_duplicate_error),
            2
        )
    except (DuplicateValueError, scrape_vuokraovi.StartEndError) as error:
        # We just want to exit gracefully, as we have encountered a duplicate
        # or we don't have more than 1 page
        return
    finally:
        conn.close()


def insert_to_db(conn, duplicate_callback, url, html):
    with conn:
        # Assume urls are unique for a year, and find if duplicate exists:
        conn.execute("""
        select count(1) from etuovi
        where insert_ts > datetime(CURRENT_TIMESTAMP, '-365 days')
        and url = ?
        """, url)

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
