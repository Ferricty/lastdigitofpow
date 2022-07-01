def last_number_of_pow(base,exponent):
    base=int(str(base)[-2:])
    '''
    Es posible hallar la cifra de las unidades de la potencia de dos numeros
    conociendo solamente la cifra de las unidades de la base y las dos ultimas
    del exponente. En eso consiste el codigo. Explicando:
        Si el exponente es 0 el resultado siempre sera 1.
            -Si la cifra de las unidades de la base es 0,1,5,6 la cifra de las 
            unidades del resultado de base**exponente siempre sera 0,1,5,6 
            respectivamente. 
            
            -Si la cifra de las unidades de la base es 4 o 9 la cifra de las 
            unidades del resultado de base**exponente siempre sera 6 o 4; 1 o 9
            si el exponente es par se escoge la primera opcion, de ser impar
            le corresponde la segunda respectivamente.
            
            -Si la cifra de las unidades de la base es 2,3,7,8 es necesario 
            analizar la cifra de las decenas del exponente tal como se muestra
            en el codigo. 
            
    Este codigo fue realizado por @Ferricty
            
    
    '''

    if base<0 or exponent<0:
        return "La base y el exponente deben ser >=0"
    
    if exponent==0:
        return 1
    
    
    if exponent==1:
        return base%10
    
#    if base==0 and exponent==0:
#        return 1
    
    if base%10==0:
        return 0
    
#    if base%10==1:
#        return 1
    
    exponent=int(str(exponent)[-2:])
    
    if base%10==2:
        if exponent%10==0 and ((exponent%100-exponent%10)/10)%2!=0:
            return 4
        if exponent%10==0 and ((exponent%100-exponent%10)/10)%2==0:
            return 6
        
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2!=0:
            return 8
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2==0:
            return 2
        
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2!=0:
            return 6
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2==0:
            return 4
        
        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2!=0:
            return 2
        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2==0:
            return 8
        
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2!=0:
            return 4
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2==0:
            return 6
        
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2!=0:
            return 8
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2==0:
            return 2
        
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2!=0:
            return 6
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2==0:
            return 4
        
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2!=0:
            return 2
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2==0:
            return 8
        
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2!=0:
            return 4
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2==0:
            return 6
        
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2!=0:
            return 8
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2==0:
            return 2
        
    if base%10==3:
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2!=0:
            return 7
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2==0:
            return 3
        
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2!=0:
            return 1
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2==0:
            return 9

        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2!=0:
            return 3
        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2==0:
            return 7
        
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2!=0:
            return 9
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2==0:
            return 1
        
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2!=0:
            return 7
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2==0:
            return 3
        
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2!=0:
            return 1
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2==0:
            return 9
        
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2!=0:
            return 3
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2==0:
            return 7
        
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2!=0:
            return 9
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2==0:
            return 1
        
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2!=0:
            return 7
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2==0:
            return 3
    
    if base%10==4:
        if (exponent%10)%2==0:
            return 6
        else: 
            return 4
        
    if base%10==5:
        return 5
    
    if base%10==6:
        return 6
    
    if base%10==7:
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2!=0:
            return 3
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2==0:
            return 7
        
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2!=0:
            return 1
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2==0:
            return 9

        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2!=0:
            return 7
        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2==0:
            return 3
        
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2!=0:
            return 9
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2==0:
            return 1
        
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2!=0:
            return 3
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2==0:
            return 7
        
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2!=0:
            return 1
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2==0:
            return 9
        
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2!=0:
            return 7
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2==0:
            return 3
        
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2!=0:
            return 9
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2==0:
            return 1
        
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2!=0:
            return 3
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2==0:
            return 7
        
    if base%10==8:
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2!=0:
            return 2
        if exponent%10==1 and ((exponent%100-exponent%10)/10)%2==0:
            return 8
        
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2!=0:
            return 6
        if exponent%10==2 and ((exponent%100-exponent%10)/10)%2==0:
            return 4

        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2!=0:
            return 8
        if exponent%10==3 and ((exponent%100-exponent%10)/10)%2==0:
            return 2
        
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2!=0:
            return 4
        if exponent%10==4 and ((exponent%100-exponent%10)/10)%2==0:
            return 6
        
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2!=0:
            return 2
        if exponent%10==5 and ((exponent%100-exponent%10)/10)%2==0:
            return 8
        
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2!=0:
            return 6
        if exponent%10==6 and ((exponent%100-exponent%10)/10)%2==0:
            return 4
        
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2!=0:
            return 8
        if exponent%10==7 and ((exponent%100-exponent%10)/10)%2==0:
            return 2
        
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2!=0:
            return 4
        if exponent%10==8 and ((exponent%100-exponent%10)/10)%2==0:
            return 6
        
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2!=0:
            return 2
        if exponent%10==9 and ((exponent%100-exponent%10)/10)%2==0:
            return 8
    
    if base%10==9:  
        if exponent%2==0:
            return 1
        else:
            return 9
    

print(last_number_of_pow(0,2))   


    