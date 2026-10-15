




from vorode_nomarat import *


while True:
   
    
    menu_nomarat_miyangin=input("1.vared kardan nomarat 2.exit")
    while True:
        match menu_nomarat_miyangin:
            case"1":
                nom_riyazi=float(input("nom riyazi ra vared konid:"))
                nom_tarikh=float(input("nom tarikh ra vared konid:"))
                nom_zist=float(input("nom zist ra vared konid:"))
                nomarat_miyangin(nom_riyazi,nom_tarikh,nom_zist)
                
                break
            case "2":
                break

