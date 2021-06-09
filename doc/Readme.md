# Taksonomia, identyfikacja tekstu

Rozwiązanie problemu automatycznej klasyfikacji artykułów Wikipedii przy użyciu `doc2vec`, `NER` oraz algorytmów analizy grafu. 

## Repozytorium

### Notatniki

* `notebooks/01-tti-classify.ipynb` główny plik Jupyter Notebook przedstawiający rozwiązanie zadania,
* `notebooks/01-tti-prepare-document.ipynb`  notatnik przedstawiający proces ściągania oraz przygotowania arytkułu do klasyfikacji,
* `notebooks/01-tti-training-set-generate.ipynb` plik generujący wektory reprezentacji numerycznej poszczególnych kategorii

### Dodatkowe moduły

`TTI/*`

# Dokumentacja projektu

## Wymagania
Celem projektu jest zaproponowane i przetestowanie mechanizmu automatycznej klasyfikacji tekstu gdzie wejściem jest treść artykułu w postaci tekstu (w języku angielskim) bez informacji o kategorii. Wyjściem jest zbiór węzłów w/w klasyfikacji tematycznej. Oczekiwanym wyjściem z algorytmu jest zbiór nazw kategorii, do których z największym prawdopodobieństwem może zostać przypisany artykuł wejściowy.

Graf kategorii Wikipedii jest wyjątkowo duży, co powoduje trudności dla twórców artykułów w ich poprawnym przyporządkowaniu do odpowiedniej kategorii. System automatycznej klasyfikacji mógłby wspomóc twórcę przez zaproponowanie sugerowanej listy kategorii.

Dane wejściowe do zadania to graf spójny o 225 765 węzłach (339 250 krawędzi), każdy węzeł reprezentuje jedną kategorię. Graf nie jest uporządkowanym drzewem, może również zawierać pętle. Wielkość grafu powoduje brak możliwości zastosowania tradycyjnego algorytmu uczenia maszynowego.

## Hipoteza
Dla każdej kategorii istnieje możliwość stworzenia zbioru słów charakteryzujących daną kategorię zawierającego nazwę tej kategorii oraz zbiór nazw sąsiednich węzłów grafu.

Istnieje możliwość przeprowadzenia klasyfikacji przy użyciu porównania wektorów reprezentacji numerycznej `doc2vec` zbioru słów reprezentujących kategorię oraz zbioru najczęściej występujących słów w artykule.

## Etapy prac
1. Wczytanie grafu kategorii.
2. Implementacja scrappera artykułów danej kategorii (z powodu zmiany koncepcji nie został wykorzystany).
3. Implementacja metod tworzących wektory `doc2vec`.
4. Implementacja generacji wektorów dla wszystkich kategorii i ich eksport do bazy danych.
5. Próba implementacji algorytmu klasteryzacji kategorii (pomysł został zastąpiony przez porównanie geometryczne wektorów `doc2vec`).
6. Implementacja interfejsu zwracającego zbiór najczęściej występujących słów dla artykułu o podanej nazwie z wykorzystaniem API Wikipedii.
7. Implementacja finałowego rozwiązania i eksperymenty.

## Wyniki
Przykładowe wyniki:

```
"Maxwell's equations": 
[('Dirac equation', 0.47262195755523584),
 ('Units of electrical conductance', 0.5105260627377728),
 ('Units of electrical resistance', 0.5201984424947701),
 ('Quantum electrodynamics', 0.5211182432355765),
 ('Magnetic monopoles', 0.524841188862891)]
 ```

 ```
"COVID-19": 
[('Elder law', 0.565619938441521),
 ('Risk factors', 0.5676282560972064),
 ('Cross-sectional analysis', 0.5794792989270499),
 ('Medical law journals', 0.5802471747474864),
 ('Observational study', 0.5815167426234842)]
 ```

 ```
 "Machine learning": 
[('Machine learning researchers', 0.4397311011007218),
 ('Logic programming researchers', 0.4412704569362673),
 ('Loss functions', 0.4591873063314801),
 ('Expert systems', 0.46839583850828126),
 ('Markov models', 0.4742454348302344)]
 ```

 ```
 "React Native": 
[('Web frameworks', 0.5893907456203118),
 ('Ajax (programming)', 0.5933646821684826),
 ('Component-based software engineering', 0.5971404285860622),
 ('Web developers', 0.5978359344648014),
 ('Audio to video synchronization', 0.6031584457844819)]
 ```
Więcej szczegółów można znaleźć w notebooku `01-tti-classify.ipynb` w folderze `notebooks`.
## Wnioski
Projekt udowodnij  możliwość przeprowadzenia poprawnej klasyfikacji przy użyciu porównania wektorów reprezentacji numerycznej `doc2vec`. Uzyskane efektu okazały się wystarczające. Istnieje możliwość przeprowadzenia dalszych eksperymentów polegających na próbie optymalizacji parametrów algorytmu: ilości słów reprezentujących kategorię oraz najczęściej występujących słów w artykule.