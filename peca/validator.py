from django.core.exceptions import ValidationError


def validateNoDigits(value):
	if all(n.isdigit() for n in value):
		raise ValidationError('Este campo não aceita letras')

	else:
		return value


def validateNome(value):
    if len(value)<3:
        raise ValidationError('O nome deve possuir três ou mais caracteres')
    
    elif value.isdigit()==True:
        raise ValidationError('O nome não deve possuir números')
    
    else:
        return value
    
def validateCodBarras(value):
    if value.isdigit()==False:
        raise ValidationError('O Código de Barras não deve possuir letras')
    else:
        return value
      
def validatePreco(value):
    if int(value) <= 0:
        raise ValidationError('O valor da peça não pode ser negativo e ZERO')
    else:
         return value