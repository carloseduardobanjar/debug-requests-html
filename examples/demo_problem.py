import pandas as pd
import requests_html
import os
from requests_html import HTML

# def main():
#     df_links = pd.read_csv('./links.csv')

#     session = requests_html.HTMLSession()

#     for i in range(0, len(df_links.index)):
#         url = df_links.iloc[i]['hyperlink']
#         print(f"[{i}/{len(df_links.index)}]: {url}", flush=True)
#         try:
#             response = session.get(url)
#             if response.status_code == 200:
#                 response_html = response.html
#                 dateList = response_html.find('relative-time')
#         except Exception as e:
#             print(f"Something went wrong: {e}", flush=True)

# if __name__ == "__main__":
#     main()

pasta = './files'
arquivos = sorted(os.listdir(pasta))

for filename in arquivos :
    filepath = os.path.join(pasta, filename)
    print(f"[{filename}]", flush=True)
    
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content = file.read()
    html = HTML(html=html_content)

    dateList = html.find('relative-time')