# Taksonomia, identyfikacja tekstu

Dany jest fragment hierarchii klasyfkacji tematycznej z Wikipedii (https://en.wikipedia.org/wiki/Category:Main_topic_classifications) w postaci pliku CSV.
Klasyfkacja jest grafem spójnym, gdzie węzły są tematami, a krawędzie reprezentują uszczegółowienie tematu.

Celem projektu jest zapropnowanie i przetestowanie mechanizmu automatycznej klasyfikacji tekstu Wejściem jest plik tekstowy w języku angielskim. Wyjściem jest zbiór węzłów w/w klasyfikacji tematycznej.

## Dane wejściowe

Dane wejściowe do zadania do graf spójny o 225765 węzłach, kady węzeł reprezentuje jedną kategorię. Graf nie jest uporządkowanym drzewem, może również zawierać pętle.