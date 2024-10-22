from blueprints.formula import CritDemage, Demage

ability = {"Normalatk1": 83.6, 
          "Normalatk2": 86.1, 
          "Normalatk3": 108.9, 
          "Normalatk4": 117.1, 
          "Normalatk5.1": 59.4, 
          "Normalatk5.2": 62.8, 
          "Normalatk6": 153.4, 
          "ChargeAtk": 242.6, 
          "PlungeLow": 233, 
          "PlungeHigh": 292}

burst = {"highHp": 494,
         "lowHp": 617}

crimson = {"PyroBonus": 15,
           "VapoMeltBonus": 15,
           "BOB": 40} #	Burning, Overloaded, Burgeon

res_enemy = 10

def skill(hp, atk, dmgbonus):
    new_atk = 0.0626*hp + atk #skill hutao
    new_dmgbonus = dmgbonus+(crimson["PyroBonus"]*0.5) #pasif crimsom

    return new_atk, new_dmgbonus

def lowHp(hp, atk, dmgbonus):
    new_atk = 0.01*hp + atk #pasif homa
    new_dmgbonus = dmgbonus + 33 #pasif hutao

    return new_atk, new_dmgbonus

def AllDemage(hp, atk, deff, em, cr, cdm, dmgbonus, lvlchar, lvlenemy, reaction, lowhp_active, skill_active):
    if lowhp_active:
        atk, dmgbonus = lowHp(hp, atk, dmgbonus)
        burstMultipler = burst["lowHp"]
    else:
        burstMultipler = burst["highHp"]

    if skill_active:
        atk, dmgbonus = skill(hp, atk, dmgbonus)
    else:
        dmgbonus = 0
    
    ability["Burst"] = burstMultipler

    datanoncrit = ability.copy()
    datacrit = ability.copy()

    for key in datanoncrit:
        abilitycorrect = datanoncrit[key]/100
        datanoncrit[key] = Demage(ability=abilitycorrect, scale=atk, baseMultipler=None, additiveBaseBonus=None, 
                                    dmgBonus=dmgbonus, dmgReduction=None, lvlchar=lvlchar, lvlenemy=lvlenemy, 
                                    defreduction=None, defignored=None, res=res_enemy, EM=em, reactionBonus=crimson["VapoMeltBonus"], 
                                    reactionType=reaction, typedmg="pyro")
        datacrit[key] = CritDemage(cdm/100, datanoncrit[key])

    data = {"nonCrit": datanoncrit,
            "Crit": datacrit}
    
    return data