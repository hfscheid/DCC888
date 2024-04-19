# Parsing Solution

Die ganze Lösung kann in der Funktion selbst gemacht werden.
- Ein Python-Dict wurde erstellt, dessen Schlüsseln den Befehle entsprechen. Die damit verbundene Werte sind die Typen der entsprechenden Klassen.
- Jede Linie wird tokenisiert. Das erste Token muss überprüft werden, ob es "bt" oder eine binäre Anweisung inst.
	-  Falls es eine binäre Anweisung ist, wird das Dict verwendet, um den Typ des neues `Inst` zu ermitteln. Das Objekt wird erstellt mithilfe der anderen Tokens.
	- Falls einer "bt"-Anweisung wird das `Bt`-Objekt auch erstellt mit den Tokens, die `Bt`-Anweisung wird jedoch auch in eine spezifische Liste hinzugefügt, die später dazu gebraucht wird, den Anweisungen korrekte Folgern zu versorgen. Dazu wird die `add_true_next`-Funktion verwendet, die innen der `Bt`-Klasse [definiert wird](model-language-de.md#Bt).

Nachdem diese Aufgabe abgeschlossen wird, wird die Lösung bei den folgenden Aufgaben.

#solution
#resource