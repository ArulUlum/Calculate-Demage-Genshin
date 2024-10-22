from blueprints import hutao


def calculate(data):
    try:
        hp_value = float(data['hp'])
        atk_value = float(data['atk'])
        def_value = float(data['def'])
        em_value = float(data['em'])
        cr_value = float(data['cr'])
        cdm_value = float(data['cdm'])
        dmgbonus_value = float(data['dmgbonus'])
        lvlchar_value = float(data['lvlchar'])
        lvlenemy_value = float(data['lvlenemy'])
        skill_active = data.get('skill_active') == 'on'
        lowhp_active = data.get('lowhp_active') == 'on'
        reaction = data.get('reaction', 'None')

        new_atk_value = atk_value
        new_dmgbonus_value = dmgbonus_value
        if lowhp_active:
            new_atk_value, new_dmgbonus_value = hutao.lowHp(hp_value, atk_value, dmgbonus_value)
            burst = 617
        else:
            burst = 494

        if skill_active:
            new_atk_value, new_dmgbonus_value = hutao.skill(hp_value, new_atk_value, new_dmgbonus_value)
        else:
            new_dmgbonus_value = 0

        alldemage = hutao.AllDemage(hp_value, new_atk_value, def_value, em_value, cr_value, cdm_value, 
                                    new_dmgbonus_value, lvlchar_value, lvlenemy_value, reaction, burst)
        
        return alldemage    
    except:
        return False