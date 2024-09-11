from django import forms
from .models import *
from account.forms import FormSettings


class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ['phone']
        labels = {
            'phone': 'Téléphone',
        }
        


class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']
        labels = {
            'name': 'Nom du poste',
            'max_vote': 'Nombre de vote maximum',
        }


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']
        labels = {
            'fullname': 'Nom',
            'bio': 'Biographie',
            'position': 'Poste',
            'photo': 'Photo',
        }
        
