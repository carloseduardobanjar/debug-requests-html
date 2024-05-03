import pandas as pd
import requests_html

def main():
    df_links = pd.read_csv('links2.csv', index_col=0)

    session = requests_html.HTMLSession()

    try:
        for i in range(0, len(df_links.index)):
            url = df_links.iloc[i]['hyperlink']
            print(f"[{i}/{len(df_links.index)}]: {url}", flush=True)
            response = session.get(url)
            status_code = response.status_code
            if status_code == 200:
                response_html = response.html
                dateList = response_html.find('relative-time')
    except Exception as e:
        print("Something went wrong...", flush=True)

if __name__ == "__main__":
    main()