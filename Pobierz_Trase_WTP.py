import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Pobranie linku od użytkownika
url = input("Podaj link do strony z trasą: ")

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Błąd pobierania strony: {e}")
    exit()

# Parsowanie HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Pobranie wszystkich przystanków
stops = soup.find_all("a", class_="timetable-link timetable-route-point name active follow")
# Dodatkowo pobieramy przystanek końcowy, który jest w <div> z odpowiednią klasą
end_stops = soup.find_all("div", class_="timetable-route-point name active follow disabled")

# Pobranie wszystkich czasów przejazdu (występują w tej samej kolejności co przystanki)
delays = soup.find_all("div", class_="timetable-route-point delay")

# Pobranie tylko tagów <svg> z div o klasie "timetable-route"
timetable_route = soup.find_all("div", class_="timetable-route")
svg_tags = []
for div in timetable_route:
    svg_tags.extend(div.find_all("svg", role="img"))  # Dodajemy tylko svg w ramach div.timetable-route

# Tworzenie list do przechowywania danych do arkusza
stop_names = []
original_names = []
request_stops = []  # Lista przechowująca informacje o przystankach na żądanie
travel_times = []  # Lista czasów przejazdu

# Indeksowanie przystanków
for i, stop in enumerate(stops + end_stops):  # Łączymy przystanki i przystanki końcowe
    # Sprawdzanie, czy czas przejazdu istnieje
    travel_time = 0
    if i < len(delays):
        time = re.sub(r"\D", "", delays[i].text.strip())  # Usuwamy niecyfrowe znaki
        travel_time = int(time) if time else 0  # Przypisujemy czas przejazdu
    travel_times.append(travel_time)

    # Sprawdzanie, czy przystanek jest na żądanie, na podstawie tagu <svg>
    is_request_stop = 0  # Domyślnie uznajemy, że przystanek nie jest na żądanie
    if i < len(svg_tags):
        aria_label = svg_tags[i].get("aria-label", "")
        
        # Sprawdzamy, czy tag svg wskazuje "Przystanek na żądanie"
        if "Przystanek na żądanie" in aria_label:
            is_request_stop = 1  # Uznajemy, że przystanek jest na żądanie
    
    request_stops.append(is_request_stop)

    # Pobranie nazwy przystanku
    full_name = ""
    if stop.has_attr("aria-label"):
        full_name = stop["aria-label"].replace("Przystanek: ", "").strip()

    # Przekształcenie nazwy przystanku (usunięcie ostatnich cyfr)
    modified_name = re.sub(r"\d{2}$", "", full_name).strip()
    stop_names.append(modified_name)
    original_names.append(full_name)

# Zapis do pliku XLSX
df = pd.DataFrame({
    "Przystanek (bez końcówki)": stop_names,
    "Oryginalna nazwa": original_names,
    "Czas przejazdu (min)": travel_times,
    "Przystanek na żądanie": request_stops  # Dodanie kolumny z informacją o przystanku na żądanie
})

# Zapisanie do pliku XLSX
output_file = "trasa.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Zapisano trasę do pliku {output_file}")
