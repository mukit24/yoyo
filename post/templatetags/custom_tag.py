from django import template
from home.models import Volunteer_Profile,Contributer_Profile
register = template.Library()

@register.filter(name='react_check')
def react_check(value, arg):
    for x in value:
        if x.author == arg:
            return True
    else:
        return False


@register.filter(name='vol_rank')
def vol_rank(value):
    all_vol = Volunteer_Profile.objects.all().order_by('-total_points')
    rank = 0
    for x in all_vol:
        rank = rank +1
        if x.user == value:
            break
    return rank


@register.filter(name='con_rank')
def con_rank(value):
    all_con = Contributer_Profile.objects.all().order_by('-total_money')
    rank = 0
    for x in all_con:
        rank = rank +1
        if x.user == value:
            break
    return rank

@register.filter(name='silver_badge')
def silver_badge(value):
    if value.volunteer.total_points > 150.00:
        return True
    else:
        return False


