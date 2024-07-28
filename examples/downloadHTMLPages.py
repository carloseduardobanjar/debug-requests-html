import requests_html
from requests_html import HTML
import pandas as pd

df_links = pd.read_csv('../links.csv')
session = requests_html.HTMLSession()
for i in range(0, 7760):
    url = df_links.iloc[i]['hyperlink']
    try:
        response = session.get(url)
        if response.status_code == 200:
            html_content = response.html.html
            with open(f'../files/response_{i}.html', 'w', encoding='utf-8') as file:
                file.write(html_content)
    except Exception as e:
        print(f"Error processing URL {url}: {e}")