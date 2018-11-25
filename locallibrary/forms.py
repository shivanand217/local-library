from django.core.exceptions import ValidationError
from django.utils.translation import ungettext_lazy as _
from django import forms

import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks from now. (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal cant be possible on past date.'))
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead.'))

        return data
        