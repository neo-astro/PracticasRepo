from django.forms import TextInput
from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


class tpi(models.Model):
    Nomt = models.CharField(max_length=50)

    def __str__(self):
        fila01 =  self.Nomt 
        return fila01

class carrera(models.Model):
    Nomc = models.CharField(max_length=100)


    def __str__(self):
        fila02 = self.Nomc
        return fila02

class pais(models.Model):
    Nomp = models.CharField(max_length=100,primary_key=True) 


    def __str__(self):
        fila02 = self.Nomp
        return fila02

class provincia(models.Model):
    Nompai = models.ForeignKey(pais, on_delete=models.SET_NULL,null=True) 
    Nomprov = models.CharField(max_length=100,primary_key=True)   


    def __str__(self):
        fila03 = self.Nomprov
        return fila03


class ciudad(models.Model):
    Nomprov = models.ForeignKey(provincia, on_delete=models.SET_NULL,null=True)
    Nomcant = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        fila04 = self.Nomcant
        return fila04



class usuarios(models.Model):
    Nombre           = models.CharField(max_length=50,null=False)
    Apellido_P       = models.CharField(max_length=50,null=False)
    Apellido_M       = models.CharField(max_length=50,null=False)
    Fecha_Nac        = models.DateField(null=False)
    Telf_Celular     = models.CharField(max_length=15,null=False)
    Usu_Django       = models.CharField(max_length=50,null=False)
    N_Identificacion = models.CharField(max_length=13, primary_key=True, null=False)
    T_Identificacion = models.ForeignKey(tpi,   on_delete=models.CASCADE, null=False ) 
    Pais             = models.ForeignKey(pais,  on_delete=models.CASCADE, null=False )
    Provincia        = models.ForeignKey(provincia,  on_delete=models.CASCADE, null=False )
    Ciudad           = models.ForeignKey(ciudad,     on_delete=models.CASCADE, null=False)  
    

    def __str__(self):
        fila1 = "Numero de Identificacion: " + self.N_Identificacion 
        return fila1


class profesores(models.Model):
    usup = models.ForeignKey(usuarios,  on_delete=models.SET_NULL, null=True,blank=True,error_messages={'required': 'Selecione al estudiante'}) 
    Fecha_Inic = models.DateField(blank=True, error_messages={'invalid': 'Ingrese una fecha válida.'})
    Estado = models.BooleanField(default=False)

class profesoresForm(forms.ModelForm):
    usup = forms.IntegerField( label='usua') 
    Fecha_Inic = models.DateField(blank=True, error_messages={'invalid': 'Ingrese una fecha válida.'})
    Estado = models.BooleanField(default=False)
    class Meta:
        model =profesores
        fields = ['usup','Fecha_Inic','Estado']


class alumnos(models.Model):
    usua = models.ForeignKey(usuarios,  on_delete=models.SET_NULL, null=True,blank=True,error_messages={'required': 'Selecione al estudiante'})
    Nom_carr = models.ForeignKey(carrera,  on_delete=models.SET_NULL, null=True,blank=True,error_messages={'required':'Seleciona la carrera'})
    Fecha_Inici = models.DateField(blank=True, error_messages={'invalid': 'Ingrese una fecha válida.'})

# formularios
# widget=forms.Select(attrs={'disabled': 'disabled'})
class alumnosForm(forms.ModelForm):
    #usua       = forms.IntegerField(    label='usua')
    usua       =  forms.IntegerField( label='usua')
    # usua         = forms.ModelChoiceField(queryset=usuarios.objects.all(),   label='usua')
    # usua = forms.ChoiceField(choices=[(item.pk, item.usua) for item in alumnos.objects.all()])
    Nom_carr     =  forms.ModelChoiceField(queryset=carrera.objects.all(),      required=True ,empty_label="Seleccione una Carrera", label='Carrera', error_messages={'required': 'Selecciona el tipo de carrera que pertenece.','required': 'Este campo es requerido'}   ,       )
    Fecha_Inici  = forms.DateField(                                             required=True , label="Fecha de inicio",error_messages={'invalid': 'Ingrese una fecha válida.','required':'El campo es requerido'})
     
    class Meta:
        model = alumnos
        fields = ['usua', 'Nom_carr', 'Fecha_Inici']


class usuariosForm(forms.ModelForm):
  Nombre           = forms.CharField(max_length=50,                           label='Nombre',required=True ,validators=[RegexValidator(r'^[a-zA-Z]*$','Solo se permiten letras en este campo.'),MinLengthValidator(3,'Minimo 3 letras')],  error_messages={'required': 'Este campo es requerido'})
  Apellido_P       = forms.CharField(max_length=50,                           label='Apellido Paterno',required=True ,validators=[RegexValidator(r'^[a-zA-Z]*$','Solo se permiten letras en este campo.'),MinLengthValidator(3,'Minimo 3 letras')],  error_messages={'required': 'Este campo es requerido'})
  Apellido_M       = forms.CharField(max_length=50,                           label='Apellido Materno',required=True ,validators=[RegexValidator(r'^[a-zA-Z]*$','Solo se permiten letras en este campo.'),MinLengthValidator(3,'Minimo 3 letras')],  error_messages={'required': 'Este campo es requerido'})
  Fecha_Nac        = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),                                         label='Fecha de nacimiento',required=True ,error_messages={'invalid': 'Ingrese una fecha válida.','required':'El campo es requerido'})
  Telf_Celular     = forms.CharField(max_length=15,                           label='Telefono Celular',required=True ,validators=[RegexValidator(r'^0\d{9}$','Comprube el numero por favor'),], error_messages={'required': 'Este campo es requerido'})
  Usu_Django       = forms.CharField(max_length=50,                           label='Nombre de Usuario',required=True ,validators=[RegexValidator(r'^[a-zA-Z0-9]*$','No debe tener espacios'),], error_messages={'required': 'Este campo es requerido'})
  N_Identificacion = forms.CharField(max_length=13,                           label='Numero de Identificacion',required=True ,error_messages={'invalid': 'Compruebe su identificacion.','required': 'Este campo es requerido'},validators=[RegexValidator(r'^0[\d]{9,12}$','Comprube el numero por favor')] )
#   N_Identificacion = forms.CharField(max_length=13,                           label='Numero de Identificacion',error_messages={'invalid': 'Compruebe su identificacion.'},validators=[RegexValidator(r'^0[\d]{9,12}$','Comprube el numero por favor')] )
  T_Identificacion = forms.ModelChoiceField(queryset=tpi.objects.all(),       label='Tipo de Identificacion',required=True ,error_messages={'required': 'Selecciona el tipo de identificaion.',},empty_label="Tipo de identificacion" ) 
  Pais             = forms.ModelChoiceField(queryset=pais.objects.all(),      required=True ,empty_label="Seleccione el País",  error_messages={'required': 'Selecciona el tipo de identificaion.','required': 'Este campo es requerido'}   ,       )    
  Provincia        = forms.ModelChoiceField(queryset=provincia.objects.none(), required=True ,empty_label="Seleccione la Provincia",error_messages={'required': 'Compruebe su identificaion.','required': 'Este campo es requerido'},       )
  Ciudad           = forms.ModelChoiceField(queryset=ciudad.objects.none(),    required=True ,empty_label="Seleccione la Ciudad",         error_messages={'required': 'Selecciona el tipo de identificaion.','required': 'Este campo es requerido'}, )
  
  class Meta:
    model = usuarios
    fields = ['Nombre', 'Apellido_P', 'Apellido_M', 'Fecha_Nac', 'Telf_Celular', 'Usu_Django', 'N_Identificacion', 'T_Identificacion', 'Pais', 'Provincia', 'Ciudad']


  def clean(self):
    cleaned_data = super().clean()
    tpi = cleaned_data.get("T_Identificacion")
    numero_tpi = cleaned_data.get("N_Identificacion")
    
    #funciona valida que no se repita la pk
    # if usuarios.objects.filter(N_Identificacion=numero_tpi).exists():
    #     self.add_error('N_Identificacion', 'El numero de identificacion ya ha sido registrado.')

    
    if tpi and numero_tpi:
        if tpi.id == 1 and len(numero_tpi) != 13:
            self.add_error("N_Identificacion", "Su Ruc debe tener 13 dígitos.")
        elif tpi.id != 1 and len(numero_tpi) != 10:
            self.add_error("N_Identificacion", "Su identificacion debe tener 10 dígitos.")

    # if self.instance:
    #  self.fields.pop('N_Identificacion')


    # pk = cleaned_data.get("pk")
    # if pk is None and not self.instance.pk:
    #     raise forms.ValidationError("El campo pk es obligatorio.")


    # if self.instance:
    #     if usuarios.objects.filter(N_Identificacion=numero_tpi).exclude(N_Identificacion=self.instance.pk).exists():
    #         raise forms.ValidationError("Ya existe un registro con este código")
    #     else:
    #         if usuarios.objects.filter(N_Identificacion=numero_tpi).exists():
    #             raise forms.ValidationError("Ya existe un registro con este código")
    #     return numero_tpi


    # def __init__(self, *args, **kwargs):
    #     super(usuarios, self).__init__(*args, **kwargs)
    #     self.fields['Pais'].choices[0] = ('', 'Select an option', {'disabled': True})  
  



    # def clean(self):
    #     cleaned_data = super().clean()
    #     t_identificacion = cleaned_data.get('T_Identificacion')
    #     n_identificacion = cleaned_data.get('N_Identificacion')

    #     if t_identificacion and t_identificacion.codigo == 'Ruc' and len(n_identificacion) != 13:
    #         self.add_error('N_Identificacion', 'Para el tipo de identificación Ruc, el número de identificación debe tener 13 dígitos.')
    #     elif t_identificacion and t_identificacion.codigo != 'Ruc' and len(n_identificacion) != 10:
    #         self.add_error('N_Identificacion', 'Para los demás tipos de identificación, el número de identificación debe tener 10 dígitos.')