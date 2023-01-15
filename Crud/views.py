import datetime
import json
from django.shortcuts import HttpResponse, redirect, render,get_object_or_404
from django.forms import modelform_factory

from Crud.models import profesoresForm, tpi, usuarios, usuariosForm,provincia,ciudad,alumnosForm,alumnos,carrera

# from Crud.models import  usuarios,tpi

# Create your views here.
def home (request):
  return render(request, 'index.html')

def tasks(request):
  return render(request, 'tasks.html')

# def Estudiante(request):
#   formEstudiante = alumnosForm()
#   return render(request, '_estudiante.html',{'form': formEstudiante})
def Estudiante(request):
  formEstudiante = alumnosForm()
  return render(request, '_estudiante.html',{'form': formEstudiante})


#modelos para la vista
# usuariosForm = modelform_factory(usuarios,exclude=[])
# Tpi = modelform_factory(tpi,exclude=[])

def ApiProvincia(reques,nombre_pais):
  data = provincia.objects.filter(Nompai=nombre_pais)
  lista = json.dumps(list(data.values()))
  return HttpResponse(lista,content_type='application/json')
  

def ApiCiudad(reques,nombre_provincia):
  data = ciudad.objects.filter(Nomprov=nombre_provincia)
  lista = json.dumps(list(data.values()))
  return HttpResponse(lista,content_type='application/json')



def usuario(request):
  if request.method == 'POST':
    formUsuario = usuariosForm(request.POST)
    ciudadData = ciudad.objects.get(pk = request.POST.get('Ciudad'))
    provinciaData = provincia.objects.get(pk = request.POST.get('Provincia'))
    formUsuario.fields['Ciudad'].queryset = ciudad.objects.filter(pk=ciudadData.pk)
    formUsuario.fields['Provincia'].queryset = provincia.objects.filter(pk=provinciaData.pk)
    

    # print(f'Ingreso Post,  {formUsuario}')
    if formUsuario.is_valid():
      print('ingreso de validacion')
      formUsuario.save()
      print('guardado')
      form = usuariosForm()
      success='!Usuario creado con Exito!'
      listaUsuarios = usuarios.objects.all()
      return render(request, '_usuario.html',{'success':success,'form':form,'usuarios':listaUsuarios})

    else: 
      print('invalido')
      # form.cleaned_data['Provincia']
      # print(usuariosForm(request.POST))
      print(request.POST)
      error = "error"
      form = usuariosForm(request.POST)

      
      pais_pk = form['Pais'].data
      provincia_pk = form['Provincia'].data
      ciudad_pk = form['Ciudad'].data

      #si fuese un objeto del select o dropdow a pais_pk(que solo es un string en este caso) cuando no lo es debo poner .pk al final
      if pais_pk and provincia_pk ==None:
        form.fields['Provincia'].queryset = provincia.objects.filter(Nompai=pais_pk)

      if provincia_pk:
        provincia_seleccionada = provincia.objects.get(pk=provincia_pk)
        form.fields['Provincia'].queryset = provincia.objects.filter(pk=provincia_seleccionada.pk)

      if provincia and ciudad_pk==None:
        # ciudad_selecionada = ciudad.objects.get(pk=ciudad_pk)
        form.fields['Ciudad'].queryset = ciudad.objects.filter(Nomprov=provincia_pk)

      if ciudad_pk:
        ciudad_selecionada = ciudad.objects.get(pk=ciudad_pk)
        form.fields['Ciudad'].queryset = ciudad.objects.filter(pk=ciudad_selecionada.pk)

      # Actualizamos el queryset del campo Provincia con el valor seleccionado

      print(provincia_pk)

      form.fields['Provincia'].initial =request.POST.get('Provincia')
      form.fields['Ciudad'].initial = request.POST.get('Ciudad')


      listaUsuarios = usuarios.objects.all()
      return render(request, '_usuario.html',{'form':form,'error':error,'usuarios':listaUsuarios})
  form = usuariosForm()
  formProfesor = profesoresForm()
  formEstudiante = alumnosForm()
  listaUsuarios = usuarios.objects.all()
  return render(request, '_usuario.html',{'form':form,'usuarios':listaUsuarios,'formEstudiante':formEstudiante,'formProfesor':  formProfesor})






def updateUsuario(request, N_Identificacion):
  if request.method == 'POST':
    #hacen lo mismo
    # usuario = usuarios.objects.get(pk=N_Identificacion)
    # usuario = get_object_or_404(usuarios, pk=N_Identificacion) 
    # print('post', request.POST)
    # usuario = get_object_or_404(usuarios, pk=N_Identificacion) 
    # form = usuariosForm(instance = usuario)
    # print('instancia', form)
    # ciudadData = ciudad.objects.get(pk = request.POST.get('Ciudad'))
    # provinciaData = provincia.objects.get(pk = request.POST.get('Provincia'))
    # form.fields['Ciudad'].queryset = ciudad.objects.filter(pk=ciudadData.pk)
    # form.fields['Provincia'].queryset = provincia.objects.filter(pk=provinciaData.pk)
    print('el post',request.POST)
    # usuario = get_object_or_404(usuarios, pk=N_Identificacion) 
    # form = usuariosForm(instance = usuario)
    form = usuariosForm(request.POST)
    ciudadData = ciudad.objects.get(pk = request.POST.get('Ciudad'))
    provinciaData = provincia.objects.get(pk = request.POST.get('Provincia'))
    form.fields['Ciudad'].queryset = ciudad.objects.filter(pk=ciudadData.pk)
    form.fields['Provincia'].queryset = provincia.objects.filter(pk=provinciaData.pk)
    



    if form.is_valid():
      # usuario = form.save()
      return HttpResponse('update')
    else: 

      # usuario = get_object_or_404(usuarios, pk=N_Identificacion) 
      form = usuariosForm(request.POST)

      # formPost = usuariosForm(request.POST)
      
      print('invalidoooooo' ,request.POST)
      pais_pk =      form['Pais'].data
      provincia_pk = form['Provincia'].data
      ciudad_pk =    form['Ciudad'].data
            #si fuese un objeto del select o dropdow a pais_pk(que solo es un string en este caso) cuando no lo es debo poner .pk al final
      if pais_pk and provincia_pk ==None:
        form.fields['Provincia'].queryset = provincia.objects.filter(Nompai=pais_pk)

      if provincia_pk:
        provincia_seleccionada = provincia.objects.get(pk=provincia_pk)
        form.fields['Provincia'].queryset = provincia.objects.filter(pk=provincia_seleccionada.pk)

      if provincia and ciudad_pk==None:
        # ciudad_selecionada = ciudad.objects.get(pk=ciudad_pk)
        form.fields['Ciudad'].queryset = ciudad.objects.filter(Nomprov=provincia_pk)

      if ciudad_pk:
        ciudad_selecionada = ciudad.objects.get(pk=ciudad_pk)
        form.fields['Ciudad'].queryset = ciudad.objects.filter(pk=ciudad_selecionada.pk)

      # Actualizamos el queryset del campo Provincia con el valor seleccionado
      error = "error"
      form.fields['Ciudad'].queryset = ciudad.objects.filter(pk= form['Ciudad'].data)
      form.fields['Provincia'].queryset = provincia.objects.filter(pk=form['Provincia'].data)
      return render(request, '_usuarioUpdate.html',{'form':form,'error':error})






  # usuario = usuarios.objects.get(pk=N_Identificacion)
  usuario = get_object_or_404(usuarios, pk=N_Identificacion) #devuelve la ci
  form = usuariosForm(instance = usuario)
  print(f'dato ${form}')
  #form.fields['Fecha_Nac'].initial = usuario.Fecha_Nac.strftime('%Y-%m-%d') # ejemplo ia
  form.fields['Fecha_Nac'].initial = usuario.Fecha_Nac
  form.fields['Ciudad'].queryset = ciudad.objects.filter(pk=usuario.Ciudad)
  form.fields['Provincia'].queryset = provincia.objects.filter(pk=usuario.Provincia)
  
  return render(request,'_usuarioUpdate.html',{'form':form})


def deleteUser(request, N_Identificacion):
  usuario = usuarios.objects.get(pk=N_Identificacion)
  usuario.delete()
  return redirect('usuario')



  
def asignarEstudiante(request):
  if request.method == 'POST':
    print(request.POST)
    print("entro al post hp")
    usuario = usuarios.objects.get( pk = request.POST.get('usua'))
    carreraNombre = carrera.objects.get(pk=request.POST.get('Nom_carr'))
    print(f'datp {usuario} , {carreraNombre}')
    alumnos.objects.create(usua = usuario, Nom_carr=carreraNombre, Fecha_Inici=request.POST.get('Fecha_Inici', None))
    print('guardado')
    return HttpResponse('EXITOU')
    #return HttpResponse('Hola')
  else:
    print("no")
    return render(request, 'estudiante.html')
  # return render(request, 'index.html')
  
  
  
  