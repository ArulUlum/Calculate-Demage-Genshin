from flask import Flask, flash,redirect,url_for,render_template,request
import blueprints.hutao as hutao

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        return render_template("calculate.html")
    # Jika GET request, form diisi dengan nilai kosong
    return render_template("calculate.html")

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method == 'POST':
        try:
            # Ambil data dari form
            data = request.form
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

            alldemage = hutao.AllDemage(hp_value, atk_value, def_value, em_value, cr_value, cdm_value, dmgbonus_value, 
                                        lvlchar_value, lvlenemy_value, reaction, lowhp_active, skill_active)
            namedemage =  list(alldemage['Crit'].keys())

            # Jika permintaan AJAX, hanya kirim bagian hasilnya
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render_template('result_partial.html', 
                                    alldemage=alldemage, 
                                    namedemage=namedemage)

            # Return agar angka dalam input box tetap
            return render_template('calculate.html',
                                hp_value=hp_value,
                                atk_value=atk_value,
                                def_value=def_value,
                                em_value=em_value,
                                cr_value=cr_value,
                                cdm_value=cdm_value,
                                dmgbonus_value=dmgbonus_value,
                                lvlchar_value=lvlchar_value,
                                lvlenemy_value=lvlenemy_value,
                                alldemage = alldemage,
                                namedemage = namedemage,
                                submitted=True)
        except ValueError:
            # Tangani error 
            return redirect("/calculate")
    
    # Saat pertama kali halaman dimuat, form harus tetap tampil
    return render_template('calculate.html', submitted=False)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)