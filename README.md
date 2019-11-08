# BSI-Lab2
Bezpieczństwo Systemów Informatycznych
## Spis treści
- [Użycie klasy](#Użycie-klasy "Przejdź do użycia klasy")
- [Technologie](#Technologie "Przejdź do wykorzystanych Technologii")
- [Przygotowanie środowiska](#Przygotowanie-środowiska "Przejdź do konfiguracji środowiska")
- [Uruchomienie testów](#Uruchomienie-testów "Przejdź do uruchomienia testów")
---
## Użycie klasy
```python
from src.calculator import Calculator
calc = Calculator()
print(calc.addition(1, 2))
```
---
## Technologie
- [Python 3.6](https://docs.python.org/3.6/ "Dokumentacja Python'a")
- [pytest 5.2.2](https://docs.pytest.org/en/latest/contents.html "Dokumentacja pytest'a")
---
## Przygotowanie środowiska
```console
$ python3 -m venv .env
```
```console
$ . .env/bin/activate
```
```console
$ pip install -U -r test-requirements.txt
```
---
## Uruchomienie testów
- uruchomienie testów:
    ```console
    $ pytest
    ```
- pokrycie kodu w testach:
    ```console
    $ pytest --cov-report term --cov=src
    ```
