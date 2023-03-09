from django import forms
from .models import ConcreteModel


class CreateSchemaForm(forms.ModelForm):
    class Meta:
        model = ConcreteModel
        fields = ['name', 'separator', 'string_character']

    new_column_name = forms.CharField(max_length=255, required=False)
    new_column_type = forms.ChoiceField(choices=(
        ('CharField', 'CharField'),
        ('IntegerField', 'IntegerField'),
        ('FloatField', 'FloatField'),
        ('BooleanField', 'BooleanField'),
        ('DateTimeField', 'DateTimeField'),
    ), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_column_name'] = forms.CharField(max_length=255, required=False)
        self.fields['new_column_type'] = forms.ChoiceField(choices=(
            ('CharField', 'CharField'),
            ('IntegerField', 'IntegerField'),
            ('FloatField', 'FloatField'),
            ('BooleanField', 'BooleanField'),
            ('DateTimeField', 'DateTimeField'),
        ), required=False)