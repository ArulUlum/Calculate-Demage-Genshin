from blueprints.formula import CritDemage, Demage

ability = {"Normalatk1": 83.6, 
          "Normalatk2": 86.1, 
          "Normalatk3": 108.9, 
          "Normalatk4": 117.1, 
          "Normalatk5.1": 59.4, 
          "Normalatk5.2": 62.8, 
          "Normalatk6": 153.4, 
          "ChargeAtk": 116.7, 
          "PlungeLow": 233, 
          "PlungeHigh": 292,
          "BurstHighHp": 494,
          "BurstLowHp": 617}

crimson = {"PyroBonus": 15,
           "VapoMeltBonus": 15}

res_enemy = 0.1

def skill(hp, atk, dmgbonus):
    new_atk = 0.0626*hp+atk
    new_dmgbonus = dmgbonus+(crimson["PyroBonus"]*0.5)

    return round(new_atk, 0), new_dmgbonus

def AllDemage(hp, atk, deff, em, cr, cdm, dmgbonus, lvlchar, lvlenemy, reaction):

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