def score(risk_factors=[],ejection_fraction=None, nyha_class=None, systolic_blood_pressure=None,creatinine=None, bmi=None,age=None):
    
    assert(type(ejection_fraction)==type(0)) #ejection_fraction should be an integer
    
    assert(type(nyha_class)==type(0)) #nyha_class should be an integer
    
    assert(nyha_class>=1 and nyha_class <=4) #nyha_class should be 1 through 4
    
    assert(type(systolic_blood_pressure)==type(0)) #systolic_blood_pressure should be an integer
    
    assert(type(creatine)==type(0)) #creatine should be an integer
    
    assert(type(bmi)==type(0)) #bmi should be an integer
    
    assert(type(age)==type(0)) #age should be an integer
    
    points=0
    points+=risk_factors_score(risk_factors)
    
    if ejection_fraction<20:
        points+=7
    elif ejection_fraction<=24:
        points+=6
    elif ejection_fraction<=29:
        points+=5
    elif ejection_fraction<=34:
        points+=3
    elif ejection_fraction<=39:
        points+=2
    points+=(0,2,6,8)[nyha_class-1]
   
    if creatinine>=90:
        if creatinine<=109:
            points+=1
        elif creatinine<=129:
            points+=2
        elif creatinine<=149:
            points+=3
        elif creatinine<=169:
            points+=4
        elif creatinine<=209:
            points+=5
        elif creatinine<=249:
            points+=6
        else:
            points+=8
            
    if bmi<15:
        points+=6
    elif bmi<=19:
        points+=5
    elif bmi<=24:
        points+=3
    elif bmi<29:
        points+=2
    
    if systolic_blood_pressure<110:
        if ejection_fraction<30:
            points+=5
        elif ejection_fraction<=39:
            points+=3    
        else:
            points+=2
    elif systolic_blood_pressure<=119:
        if ejection_fraction<30:
            points+=4
        elif ejection_fraction<=39:
            points+=2
        else:
            points+=1
            
    elif systolic_blood_pressure<=129:
        if ejection_fraction<30:
            points+=3
        elif ejection_fraction<=39:
            points+=1
        else:
            points+=1
    elif systolic_blood_pressure<=139:
        if ejection_fraction<30:
            points+=2
        elif ejection_fraction<=39:
            points+=1
    elif systolic_blood_pressure<=149:
        if ejection_fraction<30:
            points+=1
    if ejection_fraction<30:
        if age>=55:
            if age<=59:
                points+=1
            elif age<=64:
                points+=2
            elif age<=69:
                points+=4
            elif age<=74:
                points+=6
            elif age<=79:
                points+=8
            else:
                points+=10
    elif ejection_fraction<=39:
        if age>=55:
            if age<=59:
                points+=2
            elif age<=64:
                points+=4
            elif age<=69:
                points+=6
            elif age<=74:
                points+=8
            elif age<=79:
                points+=10
            else:
                points+=13
    else:
        if age>=55:
            if age<=59:
                points+=3
            elif age<=64:
                points+=5
            elif age<=69:
                points+=7
            elif age<=74:
                points+=9
            elif age<=79:
                points+=12
            else:
                points+=15
                     
    return points
def risk_factor_score (risk_factors):
    score=0
    for factor in risk_factors:
        factor=factor.lower()
        if factor in ("male","smoker"):
            score+=1
        if factor=="diabetic":
            score+=3
        if factor=="copd":
            score+=2
        if 
            
        
      # if male in risk_factors: 
def ejection_fraction_score(ejection_fraction):