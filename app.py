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
            hp_value = float(request.form['hp'])
            atk_value = float(request.form['atk'])
            def_value = float(request.form['def'])
            em_value = float(request.form['em'])
            cr_value = float(request.form['cr'])
            cdm_value = float(request.form['cdm'])
            dmgbonus_value = float(request.form['dmgbonus'])
            lvlchar_value = float(request.form['lvlchar'])
            lvlenemy_value = float(request.form['lvlenemy'])
            skill_active = request.form.get('skill_active') == 'on'

            if skill_active:
                new_atk_value, new_dmgbonus_value = hutao.skill(hp_value, atk_value, dmgbonus_value)
            else:
                new_atk_value = atk_value
                new_dmgbonus_value = 0

            alldemage = hutao.AllDemage(hp_value, new_atk_value, def_value, em_value, cr_value, cdm_value, 
                                        new_dmgbonus_value, lvlchar_value, lvlenemy_value)
            namedemage =  list(alldemage['Crit'].keys())

            # Jika permintaan AJAX, hanya kirim bagian hasilnya
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render_template('result_partial.html', 
                                    alldemage=alldemage, 
                                    namedemage=namedemage)

            # Render template dan tampilkan hasilnya
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
            # Tangani error jika konversi gagal
            flash('Input tidak valid. Harap masukkan angka yang benar.')
            return redirect(request.url)
    
    # Saat pertama kali halaman dimuat, form harus tetap tampil
    return render_template('calculate.html', submitted=False)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)