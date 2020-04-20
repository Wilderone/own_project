from parse import drivers

#import DB_exchange
from flask import Flask, render_template, request

app = Flask('drivers')

driver_names = []
for person in drivers.keys():
    driver_names.append(person)


@app.route('/')
def drivers_list():
    return render_template('index.html', driver_list=driver_names)


@app.route('/', methods=['POST'])
def get_values():
    print('im in')
    dates = request.form.get('date')
    driver = request.form.get('drivers')
    gas = request.form.get('gas')
    wash = request.form.get('wash')
    cash_given = request.form.get('cash')
    other_spends = request.form.get('other')
    shifts = request.form.get('shift')
    spends = [dates, shifts, driver, gas, wash, cash_given, other_spends]
    with open(f'D://webdata.txt', 'a') as f:
        for row in spends:
            f.write('\n' + row)
    return render_template('index.html', driver_list=driver_names)
