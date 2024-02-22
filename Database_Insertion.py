from flask import Flask, render_template, redirect, request, url_for
from Forms import CreateCardForm, UpdateCardForm

import sqlite3

def sqlquery(query):
    con = sqlite3.connect('card.db')
    cur = con.cursor()
    cur.execute(query)
    if "SELECT" in query.upper():  # Convert to uppercase for case-insensitive check
        res = cur.fetchall()
    else:
        res = None
    con.commit()
    cur.close()  # Close cursor before closing connection
    con.close()
    return res



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_card_form = CreateCardForm(request.form)
    if request.method == 'POST' and create_card_form.validate():
        sqlquery(f"""
    INSERT INTO cards(Card_set, Name, Type, Subtype, Cost, Ability, Flavour, Attack, Defense, Speed, Art, Designer)
    VALUES ('{create_card_form.set.data}', '{create_card_form.name.data}', '{create_card_form.type.data}', '{create_card_form.subtype.data}', '{create_card_form.cost.data}', '{create_card_form.ability.data}', '{create_card_form.flavor.data}', '{create_card_form.attack.data}', '{create_card_form.defend.data}', '{create_card_form.spd.data}', NULL, '{create_card_form.designer.data}');
"""
)
        return redirect(url_for('view'))
    return render_template('createcard.html', form=create_card_form)

@app.route('/view')
def view():
    Cards = sqlquery("SELECT * FROM cards")
    Cards_List = [i for i in Cards]
    return render_template('readcard.html', card_list = Cards_List, count= len(Cards_List))

@app.route('/update/<int:id>', methods=["POST", "GET"])
def edit(id):
    create_card_form = UpdateCardForm(request.form)
    if request.method == 'POST':
        query = 'UPDATE cards SET '
        if create_card_form.set.data:
            query += f"Card_set = '{create_card_form.set.data}',"
        
        if create_card_form.name.data:
            query += f"Name = '{create_card_form.name.data}',"

        if create_card_form.type.data:
            query += f"Type = '{create_card_form.type.data}',"
        
        if create_card_form.ability.data:
            query += f"Ability = '{create_card_form.ability.data}',"
        
        if create_card_form.subtype.data:
            query += f"Subtype = '{create_card_form.subtype.data}',"
        
        if create_card_form.cost.data:
            query += f"Cost = '{create_card_form.cost.data}',"
        
        if create_card_form.flavor.data:
            query += f"Flavour = '{create_card_form.flavor.data}',"
        
        if create_card_form.attack.data:
            query += f"Attack = {create_card_form.attack.data},"
        
        if create_card_form.defend.data:
            query += f"Defense = {create_card_form.defend.data},"
        
        if create_card_form.spd.data:
            query += f"Speed = {create_card_form.spd.data},"

        if create_card_form.art.data:
            query += f"Art = '{create_card_form.art.data}',"
        
        if create_card_form.designer.data:
            query += f"Designer = '{create_card_form.designer.data}'"
        
        query += f"WHERE Id = {id};"
        sqlquery(query)
        return redirect(url_for('view'))
    else:
        Card = sqlquery(f"SELECT * FROM cards WHERE Id = {id}")
        Card_Attirbute = [create_card_form.set.data, create_card_form.name.data,create_card_form.type.data,create_card_form.subtype.data,create_card_form.cost.data,create_card_form.ability.data,create_card_form.flavor.data,
                          create_card_form.attack.data, create_card_form.defend.data, create_card_form.spd.data, create_card_form.art.data, create_card_form.designer.data]
        for i in range(1, 12):
            Card_Attirbute[i] = Card[0][i]
        return render_template('editcard.html', form =create_card_form)

@app.route('/delete/<int:id>/', methods = ["POST"])
def delete(id):
    sqlquery(f"DELETE FROM cards WHERE Id = {id}")
    return redirect(url_for('view'))


if  __name__ == "__main__":
    app.run(debug=True)
