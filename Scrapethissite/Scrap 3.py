import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.scrapethissite.com/pages/forms/'
page_num = 1
result = []

while True:
    url = f"{BASE_URL}?page_num={page_num}&per_page=100"
    
    print(f"Fetching page {url}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="table")
    rows = table.find_all("tr", class_="team")

    if not rows:
        print(f"No more data found on page {page_num}")
        break

    for row in rows:
        team_name = row.find("td", class_="name").get_text(strip=True)
        year = row.find("td", class_="year").get_text(strip=True)
        pct = row.find("td", class_="pct").get_text(strip=True)

        result.append({
            "team_name": team_name,
            "year": year,
            "win_percentage": pct
        })

    page_num += 1  # pindah ke halaman berikutnya

# Tampilkan hasil
for item in result:
    print(f"Team: {item['team_name']}, Year: {item['year']}, Win %: {item['win_percentage']}")

# Simpan ke CSV
with open("countries.csv", "w", encoding="utf-8", newline='') as csv_file:
    fieldnames = ["name", "capital", "population"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)

print("Scraping selesai. File countries.csv sudah dibuat.")
