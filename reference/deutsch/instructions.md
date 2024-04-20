## Implementation
Alle Anweisungen stammen von der `Inst`-Klasse ab.  Von dieser Klasse werden 2 weitere Klassen abgeleitet: `Bt` und `BinOp`, indem die letzte weiter in 4 Anweisungen abgeteilt wird:

#### Inst
Die Wurzelklasse implementiert `add_next` und `get_next`, die nur bei `Bt` überschrieben werden müssen.

#### BinOp
Definiert die `__init__`-Funktion aller binären Operationen. Weiterhin werden die Funktionen `definition` und `uses` implementiert.

#### Add, Mul, Lth, Geq
Jede Anweisung implementiert ihre eigene `eval`-Funktion.

#### Bt
Implementiert sowohl die `eval`-Funktion als auch ihre eigene Funktionen, die ihr die folgende Anweisungen anhängen. In dieser Klasse ist die gemeinsame Variable `NEXTS` als eine Liste festgelegt, deren Werte jeweils die Adressen der `True` und `False` Ziele sind.
	- `add_next` fügt die Adresse des `False`-Zieles hinzu.
	- `add_true_next` fügt die Adresse  des `True`-Zieles hinzu.

#resource