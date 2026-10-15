

list_nomarat=[] 
list_miyangin=[]

def nomarat_miyangin (riazi:float,tarikh:float ,zist:float)->float:
    """میانگین نمرات و نمرات هر درس 

    Args:
        riazi (float): نمره ریاضی 
        tarikh (float): نمره تاریخ
        zist (float): نمره زیست 

    Returns:
        float: میانگین و لیست نمرات 
    """
    
    list_nomarat.append(riazi)
    list_nomarat.append(tarikh)
    list_nomarat.append(zist)
    print(list_nomarat)
                        
                    
    jame_nom=sum(list_nomarat)
    miu=jame_nom/len(list_nomarat)
    print(miu)
    


