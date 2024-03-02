from django import template

register=template.Library()


@register.simple_tag(name="getstatus")
def getstatus(status):
    status -= 1
    status_array=['Confirmed','Processed','Delivered','Rejected']
    return status_array[status]
        
    