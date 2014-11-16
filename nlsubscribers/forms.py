from django.forms import ModelForm
from nlsubscribers.models import Nlsubscriber

class NlsubscriberForm(ModelForm):
    class Meta:
        model = Nlsubscriber