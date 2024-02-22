from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators,  StringField, FileField
from wtforms.fields import EmailField, DateField

class CreateCardForm(Form):
    set = StringField('Set Name', [validators.DataRequired()])
    name = StringField('Card Name', [validators.DataRequired()])
    type = SelectField('Card Type', [validators.DataRequired()], choices=[('', 'Select'), ('Creature', 'Creature'), ('Spell', 'Spell'),('Item', 'Item'),('Zone', 'Zone')], default='')
    subtype = StringField('Subtype')
    cost = StringField('Cost of Card')
    ability = StringField('Ability Text of Card')
    flavor = StringField('Flavour Text of Card')
    attack = StringField('Attack of Card (if needed)')
    defend = StringField('Defend of Card (if needed)')
    spd = StringField('Speed of Card (if needed)')
    art = FileField('Image of Card')
    designer = RadioField('Designer', choices=[('M', 'Marcus'), ('XK', 'Xuan Kai')], default='XK')


class UpdateCardForm(Form):
    set = StringField('Set Name')
    name = StringField('Card Name')
    type = SelectField('Card Type', choices=[('', 'Select'), ('Creature', 'Creature'), ('Spell', 'Spell'),('Item', 'Item'),('Zone', 'Zone')], default='')
    subtype = StringField('Subtype')
    cost = StringField('Cost of Card')
    ability = StringField('Ability Text of Card')
    flavor = StringField('Flavour Text of Card')
    attack = StringField('Attack of Card (if needed)')
    defend = StringField('Defend of Card (if needed)')
    spd = StringField('Speed of Card (if needed)')
    art = FileField('Image of Card')
    designer = RadioField('Designer', choices=[('M', 'Marcus'), ('XK', 'Xuan Kai')], default='XK')