from reader import reddit
from extractor import ext
from edgar_allen_poe import write2file
from edgar_allen_poe import write2array
from edgar_allen_poe import array2list

[haus,gogn]=reddit("VIN02010.csv",";")

alls=ext(gogn,haus.index("Starfsstétt"),"Alls") #Starfsstétt: "Alls"
alls_karlar=ext(alls,haus.index("Kyn"),"Karlar") #Karlar í starfsflokki "Alls"
alls_konur=ext(alls,haus.index("Kyn"),"Konur") #Konur í starfsflokki "Alls"

write2file(haus,alls_karlar,haus.index("Regluleg laun - fullvinnandi Meðaltal"),"nidurstodur.txt","w")
write2file(haus,alls_konur,haus.index("Regluleg laun - fullvinnandi Meðaltal"),"nidurstodur.txt","a")

arr_alls_karlar=write2array(alls_karlar,haus.index("Regluleg laun - fullvinnandi Meðaltal"))
arr_alls_konur=write2array(alls_konur,haus.index("Regluleg laun - fullvinnandi Meðaltal"))

fix=array2list(arr_alls_karlar)
print(fix)