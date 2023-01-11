from django import forms

class formUsuarios(forms.Form):
  N_Identificacion = forms.CharField(label='n_identificacion', max_length=15)
  T_Identificacion= forms.CharField(label='t_identificacion', max_length=1)
  Nombre= forms.CharField(label='nombre', max_length=100)
  Apellido_P= forms.CharField(label='apellido_p', max_length=100)
  Apellido_M= forms.CharField(label='apellido_m', max_length=100)
  Fecha_Nac= forms.CharField(label='fecha_nac', max_length=100)
  Usu_Django= forms.CharField(label='usuario_django', max_length=100)
  Canton= forms.CharField(label='canton', max_length=100)
  Telf_Celular= forms.CharField(label='telefono', max_length=15)
  