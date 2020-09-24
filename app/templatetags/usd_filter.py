from django import template

register=template.Library()


@register.filter(name='low')#register.filter('low',lower)
def lower(value):
    return value.lower()

#register.filter('low',lower)


#replacing characters from hai hello how r u doing

@register.filter()
def replace_char(value,arg):
    return value.replace('H',arg)

