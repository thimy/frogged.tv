from django import template

register = template.Library()


@register.simple_tag
def submission_score(obj):
    return obj.get_score()
