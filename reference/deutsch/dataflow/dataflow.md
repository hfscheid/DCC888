# Dataflow Analysis

In dieser Aufgabe müssen die Studenten ihre erste Datenflussanalyse implementieren. Die dazu ausgewählte Analyse ist [[deutsch/concepts/liveness|Liveness]].

Die Datenflussanalyse wurde als eine Klassenhierarchie implementiert, die die Klasse `DataFlowEq` zur Wurzelklasse hat. Aus dieser werden die Klassen `IN_Eq` un `OUT_Eq` abgeleitet.

Eine Beispiellösung wird schon vorgelegt, die [[concepts/reachingdefs|Reaching Definitions]] behandelt. Da können sich Studenten anschauen, wie man die Funktion `eval_aux` implementieren soll.
### Benötigt
- [[parsing-solution-file|Parsing]]
- [[deutsch/model-language|Modellsprache]]
### Ergibt
- [[dataflow-equations|Dataflow Gleichungen]]
- [[deutsch/dataflow/constraint-gen-function|Einschränkungserzeugendefunktion]]

#activity