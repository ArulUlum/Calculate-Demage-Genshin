def defMultipler(lvlchar, lvlenemy, reduction, ignored):
    if reduction == None:
        reduction = 0
    if ignored == None:
        ignored = 0
    defm = (lvlchar+100)/((1-reduction)*(1-ignored)*(lvlenemy+100)+(lvlchar+100))
    return defm

def resMultipler(res):
    if res < 0:
        resm = 1-(res/2)
    if res >= 0.75:
        resm = 1/(4*res+1)
    else:
        resm = 1-res

    return resm

def dmgBonusMultipler(dmgBonus, dmgReduction):
    if dmgReduction == None:
        dmgReduction = 0

    return 1+((dmgBonus-dmgReduction)/100)

def amplifyingMultipler(EM, reactionBonus, reactionType, typedmg):
    
    if reactionType == None or reactionType == "None":
        return 1

    if reactionBonus == None:
        reactionBonus = 0
    else:
        reactionBonus /= 100

    if reactionType.lower() == "melt" and typedmg.lower() == "pyro":
        reactionMultipler = 2
    elif reactionType.lower() == "melt" and typedmg.lower() == "cryo":
        reactionMultipler = 1.5
    elif reactionType.lower() == "vaporize" and typedmg.lower() == "hydro":
        reactionMultipler = 2
    elif reactionType.lower() == "vaporize" and typedmg.lower() == "pyro":
        reactionMultipler = 1.5
    else:
        reactionMultipler = 1

    EMAmplifying = 2.78*(EM/(EM+1400))
    return reactionMultipler*(1+EMAmplifying+reactionBonus)

def Demage(ability, scale, baseMultipler, additiveBaseBonus, dmgBonus, dmgReduction, lvlchar, lvlenemy, defreduction, 
           defignored, res, EM, reactionBonus, reactionType, typedmg):
    
    if baseMultipler == None:
        baseMultipler = 1

    if additiveBaseBonus == None:
        additiveBaseBonus = 0

    base = ability*scale
    defM = defMultipler(lvlchar, lvlenemy, defreduction, defignored)
    dmgBonusM = dmgBonusMultipler(dmgBonus, dmgReduction)
    resM = resMultipler(res)
    amplifiyingM = amplifyingMultipler(EM, reactionBonus, reactionType, typedmg)
    
    demage = ((base * baseMultipler)+additiveBaseBonus)*dmgBonusM*defM*resM*amplifiyingM


    # base artinya persen talent dikali atk (bisa hp atau yg lain tergantung darimana)
    # baseMultipler artinya peningkatan dmg dari base dmg (misal pasif nopal trigger reaksi elemen)
    # additiveBaseBonus artinya bonus demage dari base dmg (misal pasif cinnabar weapon, meningkatkan skill)
    # dmgBonusM artinya perhitungan elemen bonus dan reduction elemen musuh
    # defM artinya perhitungan deff musuh
    # resM artinya perhitungan resistan musuh
    # amplifiyingM artinya perhitungan EM khusus peningkatan dmg (misal vapo dan melt, spread dan aggregative masuk ke additiveBaseBonus)

    return round(demage, 0)

def CritDemage(cdm, demage):
    return round(demage*(1+cdm))
