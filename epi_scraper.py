# epi_scraper => script for scraping indicators from epi website and sending results to an email

import ssl
import pandas as pd
import win32com.client as win32

def epi_scraper(mail_to):
    try:
        url = "https://epi.yale.edu/epi-results/2020/component/epi"
        ssl._create_default_https_context = ssl._create_unverified_context

        df = pd.read_html(url)[0]
        excel_file_path = r'file_path\\EPI.xlsx'
        df.to_excel(excel_file_path,
                    index=False)

        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = mail_to
        mail.Subject = "Environmental Performance Index file"
        mail.HTMLBody = f"<h4 style=color:Tomato;> Data extracted from EPI website attached. </h4>"
        attachment = excel_file_path
        mail.Attachments.Add(attachment)
        mail.Send()

        print("EPI.xlsx has been extracted and sent via an email!")
    except Exception as e:
        print(f"Error: {e}")

epi_scraper('someemail@gmail/yahoo.com')
