import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.scrapethissite.com/pages/forms/")
soup = BeautifulSoup(response.text, "html.parser")  
table = soup.find("table", class_="table")
rows = table.find_all("tr", class_="team")

results = []
for row in rows:
    team_name = row.find("td", class_="name").get_text(strip=True)
    year = row.find("td", class_="year").get_text(strip=True)
    pct = row.find("td", class_="pct").get_text(strip=True)

    results.append({
        "Team_name": team_name,
        "year": year,
        "win_percentage": pct
    })
    
    for item in results:
        print(f"Team: {item['Team_name']}, Year: {item['year']}, Win Percentage: {item['win_percentage']}")
        
        # Simpan ke CSV
with open("scrapping-2.csv", "w", encoding="utf-8", newline='') as csv_file:
    fieldnames = ["name", "capital", "population"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)

print("Scraping selesai. File countries.csv sudah dibuat.")
