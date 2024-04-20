# Model Language
Die Modellsprache enthält geringene Anweisung, die jedoch ausreichend sind, ein
Turing-komplett Programm zu bauen. Sie besteht erstens aus 5 Befehle:
    - `Add(x, a, b)`: implementiert x = a + b
    - `Mul(x, a, b)`: implementiert x = a * b
    - `Lth(x, a, b)`: implementiert x = (a < b) ? 1 : 0
    - `Geq(x, a, b)`: implementiert x = (a >= b) ? 1 : 0
    - `Bt(x, i0, i1)`: Wenn x != 0, führe Anweisung i0 aus, sonst führe i1 aus.

Durch all die Aufgaben werden Programme als ein Python-List von Anweisungen
repräsentiert werden. Eine besondere Funktion, `interp(instruction, environment)`,
ist dafür zuständig, Programme auszuführen. Sie benötigt nicht nur das Programm
selbst, sondern auch einen Zustand. Dieser wird als ein Dict[str, int] angegeben.

[[instructions|Implementation]]

#resource 