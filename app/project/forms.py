from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class NewProjectForm(FlaskForm):
    project_name = StringField('Project name', validators=[DataRequired()])
    project_desc = TextAreaField('Project description', validators=[DataRequired()])

    # team_members = SelectMultipleField('Invite Members', )
    submit = SubmitField('New Project')
