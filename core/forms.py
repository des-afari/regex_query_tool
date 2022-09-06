from django import forms

class RegexForm(forms.Form):
    expression = forms.CharField(label='REGULAR EXPRESSION', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Type your regex here...'}))
    text = forms.CharField(label='TEXT', widget=forms.Textarea(attrs={'placeholder': 'Insert text here...'}))

