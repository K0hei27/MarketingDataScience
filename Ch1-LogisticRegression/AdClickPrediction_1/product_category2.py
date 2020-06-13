import pandas as pd

def productCatagory2(columns):
    product = columns[0]
    campaign = columns[1]
    webpage = columns[2]
    catagory = columns[3]
    
    if pd.isnull(catagory):
        
        if(product == 'H' and campaign == 404347  and webpage == 53587 ):
            return(235358.0)
        elif(product == 'C' and campaign == 404347  and webpage == 53587 ):
            return(234846.0)
        elif(product == 'A' and campaign == 404347  and webpage == 53587 ):
            return(234846.0)
        elif(product == 'F' and campaign == 404347  and webpage == 53587 ):
            return(301147.0)
        elif(product == 'H' and campaign == 404347  and webpage == 53587 ):
            return(99226.0)
        elif(product == 'B' and campaign == 404347  and webpage == 53587 ):
            return(408790.0)
        elif(product == 'D' and campaign == 404347  and webpage == 53587 ):
            return(146115.0)
        elif(product == 'E' and campaign == 404347  and webpage == 53587 ):
            return(146115.0)
        elif(product == 'G' and campaign == 404347  and webpage == 53587 ):
            return(327439.0)
        elif(product == 'I' and campaign == 404347  and webpage == 53587 ):
            return(419804.0)
        elif(product == 'J' and campaign == 404347  and webpage == 53587 ):
            return(450184.0)
        
        
        elif(product == 'B' and campaign == 414149  and webpage == 45962 ):
            return(143597.0)
        elif(product == 'C' and campaign == 414149  and webpage == 45962 ):
            return(254132.0)
        elif(product == 'D' and campaign == 414149  and webpage == 45962 ):
            return(254132.0)
        elif(product == 'E' and campaign == 414149  and webpage == 45962 ):
            return(254132.0)
        
        
        elif(product == 'A' and campaign == 396664  and webpage == 51181 ):
            return(143597.0)
        elif(product == 'F' and campaign == 396664  and webpage == 51181 ):
            return(18595.0)
        
        
        elif(product == 'C' and campaign == 98970  and webpage == 6970 ):
            return(270147.0)
        elif(product == 'I' and campaign == 98970  and webpage == 6970 ):
            return(327439.0)
        elif(product == 'B' and campaign == 98970  and webpage == 6970 ):
            return(202351.0)
        
        
        elif(product == 'C' and campaign == 359520  and webpage == 13787 ):
            return(408831.0)
        
        
        elif(product == 'A' and campaign == 118601  and webpage == 28529 ):
            return(82527.0)
        elif(product == 'B' and campaign == 118601  and webpage == 28529 ):
            return(82527.0)
        elif(product == 'H' and campaign == 118601  and webpage == 28529 ):
            return(82527.0)
        elif(product == 'G' and campaign == 118601  and webpage == 28529 ):
            return(82527.0)
        elif(product == 'I' and campaign == 118601  and webpage == 28529 ):
            return(82527.0)
        
        
        elif(product == 'B' and campaign == 82320  and webpage == 1734 ):
            return(235358.0)
        elif(product == 'G' and campaign == 82320  and webpage == 1734):
            return(255689.0)
        elif(product == 'H' and campaign == 82320  and webpage == 1734):
            return(255689.0)
        elif(product == 'I' and campaign == 82320  and webpage == 1734):
            return(18595.0)
        elif(product == 'C' and campaign == 82320  and webpage == 1734):
            return(18595.0)
        else:
            return(211061.500000)
            
        
    else:
        return(catagory)
