from django import forms



class FilterForm(forms.Form):
    category_choice = [
    ('1','Sub-junior(Cadet)10-11'),
    ('2','Sub-junior(Cadet)12-13'),
    ('3','Junior(Youth)14-15'),
    ('4','Junior(Youth)16-17'),
    ('5','Senior 18-37'),
    ]
    sex_choice = [
    ('Male','Male'),
    ('Female','Female'),
    ]
    
    category = forms.CharField(label="Category",widget = forms.Select(choices = category_choice))
    sex = forms.CharField(label="Sex",widget=forms.Select(choices = sex_choice))
    weight_cat = forms.CharField(label = "Weight Category")
    weight_min = forms.CharField(label="Min Weight")
    weight_max = forms.CharField(label="Max Weight")
