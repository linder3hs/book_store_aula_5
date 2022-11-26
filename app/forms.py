from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Titulo", validators=[DataRequired()])
    author = StringField("Autor", validators=[DataRequired()])
    description = TextAreaField("Descripcción", validators=[DataRequired()])
    pages = IntegerField("# de páginas", validators=[DataRequired()])
    publish_date = DateField("Fecha de publicación", validators=[DataRequired()])
    isbn = StringField("ISBN", validators=[DataRequired()])
    submit = SubmitField("Crear libro")
