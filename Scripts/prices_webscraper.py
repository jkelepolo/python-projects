from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = "https://www.amazon.com/s?k=gaming"
session = HTMLSession()

response = session.get(URL)
response.html.render()

soup = BeautifulSoup(response.html.html, "lxml")

results = soup.find_all(class_="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", href=True) # returns an array

max_price = 10
for result in results:
    link = f"amazon.com{result['href']}"
    price = float(result.find(class_="a-offscreen").get_text().split("$")[-1].replace(",", ""))

    if price < max_price:
        print(f"-----\nLink: {link} \nPrice: {price}")


session.close()
