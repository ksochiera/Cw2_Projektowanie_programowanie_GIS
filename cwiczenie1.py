"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 2
Zadanie 1
"""
with open("cwiczenie1.txt","r") as input1:       
    n_lines=input1.read()
    n_lines=n_lines.lower()
    n_lines=n_lines.replace(",","")
    n_lines=n_lines.replace(".","")
    lines_n=n_lines.split()
    slownik={}
    for i in lines_n:
        times=lines_n.count(i)
        slownik[i]=times
    print slownik
with open("statystyki.txt","w") as stat:
    for p in slownik.items():
        stat.write("%s:%s\n" % p)
