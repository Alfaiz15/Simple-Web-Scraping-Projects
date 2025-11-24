import requests
from bs4 import BeautifulSoup
import csv

# Request halaman web
response = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(response.text, "html.parser")

# Ambil semua blok data country
county_blocks = soup.find_all("div", class_="col-md-4 country")

result = []

for block in county_blocks:
    name_element = block.find("h3", class_="country-name")
    country_name = name_element.get_text(strip=True)

    capital_element = block.find("span", class_="country-capital")
    capital_name = capital_element.get_text(strip=True)

    population_element = block.find("span", class_="country-population")
    population_name = population_element.get_text(strip=True)

    result.append({
        "name": country_name,
        "capital": capital_name,
        "population": population_name
    })

# Simpan ke CSV
with open("countries.csv", "w", encoding="utf-8", newline='') as csv_file:
    fieldnames = ["name", "capital", "population"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)

print("Scraping selesai. File countries.csv sudah dibuat.")
