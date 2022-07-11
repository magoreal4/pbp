from django import template

register = template.Library()

@register.filter(name="rst2")
def replace_spc_to_20(value):
    return value.replace(" ","%20")

@register.filter(name="fechas_datepicker")
def fechas(value):
    fecha = value[:10] 
    ano = fecha[:4]
    mes = int(fecha[5:7])-1
    dia = int(fecha[8:10])
    return ano+","+str(mes)+","+str(dia)

