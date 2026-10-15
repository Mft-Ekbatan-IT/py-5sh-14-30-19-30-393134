


from food_kabab import *

from cafe_cofee import * 

from chay import *

while True:
    menu=input("1.foood 2.cafe  3.exit:")
    
    while True:
        match menu:
            case "1":
                menu_food=input("1.kabab  2.exit:")
                match menu_food:
                    case "1":
                        num_kabab = int(input("how many:"))
                        mablagh=int(input("mablagh:"))
                        food_kabab(num_kabab,mablagh)
                    case "2":
                        break
                    
            case "2":
                menu_cafe=input("1.cofee 400  2.chay 200 3.exit :")  
                match menu_cafe:
                    case "1":
                        num_cofee=int(input("num cofee:"))
                        mablagh_cofee=int(input("mablagh cofee:"))
                        cofee(num_cofee,mablagh_cofee)
                        break
                    case "2":
                        
                        num_chay=int(input("num chay:"))
                        mablagh_chay=int(input("mablagh chay:"))
                        chayeeee(num_chay,mablagh_chay)
                        break      

                
                