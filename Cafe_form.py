from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(message="Invalid URL!")])
    open_time = StringField('Opening Time ex. 6AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time ex. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating',
                                choices=
                                    [('✘','✘'),
                                     ('☕️', '☕️'),
                                     ('☕️☕️','☕️☕️'),
                                     ('☕️☕️☕️','☕️☕️☕️'),
                                     ('☕️☕️☕️☕️','☕️☕️☕️☕️'),
                                     ('☕️☕️☕️☕️☕️','☕️☕️☕️☕️☕️')],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=
                                    [('✘','✘'),
                                     ('💪️', '💪️'),
                                     ('💪️💪️','💪💪'),
                                     ('💪️💪️💪️','💪💪💪'),
                                     ('💪️💪️💪️💪️','💪💪💪💪'),
                                     ('💪️💪️💪️💪️💪️','💪💪💪💪💪')],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability',
                               choices=
                                    [('✘','✘'),
                                     ('🔌', '🔌'),
                                     ('🔌🔌','🔌🔌'),
                                     ('🔌🔌🔌','🔌🔌🔌'),
                                     ('🔌🔌🔌🔌','🔌🔌🔌🔌'),
                                     ('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')
