# Dataflow equations

Durch die Klassenhierarchie in `DataflowEq` gewurzelt kann man Datenflussanalyse ausführen.

#### DataFlowEq
- `abstractmethod name(self) -> str`: diese Funktion wird in die Nachkommenden Klassen entwickelt.
- `abstractmethod eval_aux(self, data_flow_env)-> set`: In dieser Funktion liegen die unvollständige Code, die die Studenten implementieren müssen. 
- `eval(self, data_flow_env) -> bool`: Die Hauptfunktion der Klasse und der Klassenhierarchie. Die Umgebung `data_flow_env` besteht aus einem Dictionary, das die Namen von `DataFlowEq`-Objekten nach ein Set.