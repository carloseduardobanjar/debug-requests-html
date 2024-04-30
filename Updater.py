import pandas as pd
import requests_html
import time
import sys

__headers = {
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

def __get_response_from_session(url, session):
    retry_number = 0
    while True:
        try:
            response = session.get(url, headers=__headers)
            return response, False
        except RuntimeError:
            sys.exit()
        except Exception as e:
            print("Something went wrong...", flush=True)
            if retry_number == 2:
                return None, True
            time.sleep(2)
            retry_number += 1
            continue

def github(response):
    date = None
    try:
        response_html = response.html
        dateList = response_html.find('relative-time')
    except Exception as e: 
        print("Something went wrong:", e, flush=True)
    return date

def main():
    df_links = pd.read_csv('links2.csv', index_col=0)
    df_links.reset_index(inplace=True, drop=True)

    session = requests_html.HTMLSession()

    try:
        for i in range(7757, len(df_links.index)):
            url = df_links.iloc[i]['hyperlink']
            print(f"[{i}/{len(df_links.index)}]: {url}", flush=True)
            response, over_retry = __get_response_from_session(url, session)
            if not over_retry:
                try:
                    status_code = response.status_code
                    if status_code != 404:
                        date = github(response)
                except Exception as e:
                    print("Something went wrong...", flush=True)
    except Exception as e:
        print("Something went wrong...", flush=True)

if __name__ == "__main__":
    main()