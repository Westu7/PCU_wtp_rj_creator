# Pobierz_Trase_Wtp.py

## Opis
Skrypt `Pobierz_Trase_Wtp.py` służy do pobierania nazw przystanków z rozkładów jazdy WTP i zapisywania ich w pliku `trasa.xlsx`. Dodatkowo skrypt rejestruje informacje o czasie przejazdu między przystankami oraz oznacza przystanki na żądanie.

## Wymagania
- Python (zalecana wersja 3.x)
- Połączenie z internetem
- Program do obsługi plików Excel (np. Microsoft Excel, LibreOffice Calc) **(pliku `trasa.xlsx` nie można mieć otwartego podczas działania skryptu)**
- Zainstalowane biblioteki:
  
  ```sh pip install requests beautifulsoup4 pandas openpyxl```


## Instalacja
1. Umieść plik `Pobierz_Trase_Wtp.py` w głównym katalogu Pythona.
2. Upewnij się, że masz wszystkie wymagane biblioteki Pythona.

## Użycie
1. Uruchom skrypt w konsoli:
   ```sh python Pobierz_Trase_Wtp.py```
   

2. Po uruchomieniu, skrypt poprosi o podanie linku do strony z trasą WTP.
3. Skrypt pobierze dane z podanej strony i zapisze je w pliku `trasa.xlsx` w tym samym folderze.
4. W pliku `trasa.xlsx` znajdziesz:
   - **Przystanek (bez końcówki)** – nazwa przystanku z usuniętą końcówką cyfrową,
   - **Oryginalna nazwa** – pełna nazwa przystanku,
   - **Czas przejazdu (min)** – liczba minut przejazdu od poprzedniego przystanku,
   - **Przystanek na żądanie** – wartość `1`, jeśli przystanek jest na żądanie, `0` w przeciwnym razie.
5. Po wygenerowaniu danych otwórz plik `ZTM WAWA ROUTE GEN.xlsx` i odnieś się do `trasa.xlsx` w arkuszu `DANE PRZYSTANKÓW ZTM`.
6. W arkuszu `DANE PRZYSTANKÓW ZTM` zdefiniuj nazwy przystanków zgodne z pobranymi danymi oraz przypisz im odpowiednie kody zapowiedzi.

## Przykładowy link do pobierania rozkładu
Skrypt korzysta z poniższego formatu linku do pobierania rozkładów:
[https://www.wtp.waw.pl/rozklady-jazdy/?wtp_dt=2025-03-21&wtp_md=3&wtp_ln=111&wtp_st=2148&wtp_pt=01&wtp_dr=A&wtp_vr=0&wtp_dy=5&wtp_dc=1](https://www.wtp.waw.pl/rozklady-jazdy/?wtp_dt=2025-03-21&wtp_md=3&wtp_ln=111&wtp_st=2148&wtp_pt=01&wtp_dr=A&wtp_vr=0&wtp_dy=5&wtp_dc=1)

## Aktualność danych
Baza przystanków w pliku `ZTM WAWA ROUTE GEN.xlsx` jest aktualna na dzień **21.03.2025**. 
Aby odświeżyć dane, należy ponownie uruchomić skrypt i otworzyć wygenerowany plik `trasa.xlsx`.

## Uwagi
- Plik `trasa.xlsx` **nie może być otwarty** podczas działania skryptu.
- Skrypt wymaga dostępu do internetu, aby pobrać aktualne dane z serwisu WTP.
- Jeśli dane nie są poprawnie pobierane, sprawdź poprawność linku i strukturę strony źródłowej.
- Skrypt obsługuje przystanki na żądanie, identyfikując je na podstawie ikon `svg` w kodzie strony.

## Autor
Projekt powstał w oparciu o aktualne rozkłady jazdy WTP.

