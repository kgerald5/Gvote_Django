from django.contrib import admin
from .models import Candidate,Position,Voter
from .forms import CandidateForm,PositionForm,VoterForm

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm
class PositionAdmin(admin.ModelAdmin):
    form = PositionForm

class VoterAdmin(admin.ModelAdmin):
    form = VoterForm

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Voter, VoterAdmin)