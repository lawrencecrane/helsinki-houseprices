from oikotie import scrape_pages


def insert_to_db(data, host):
    print(data, host)

if __name__ == '__main__':
    for x in scrape_pages():
        insert_to_db(x, "localhost")
        # after the page contains ads that we already have, we can:
        break
