# Tercera pre entrega de curso coder python 40425

## credenciales de user:

    usr: admin
    pw: 1234

## Urls declaradas:
    {URL}/admin/ → Se utiliza para acceder al módulo de admin con las credenciales anteriormente mencionadas. Están todos los modelos activos disponibles para ABM
    
    {URL}/notas/ → Lista todas las notas sin filtro
    {URL}/notas/create  → Alta de registros de notas en la BD
    {URL}/notas/list → Lista todas las notas con filtro

    {URL}/usuarios/ →  Lista todos los usuarios sin filtro
    {URL}/usuarios/create → Alta de registros de usuarios en la BD
    {URL}/usuarios/list → Lista todas las notas con filtro

    {URL}/elementos/ →  Lista todos los elementos sin filtro
    {URL}/elementos/create → Alta de registros de elementos en la BD
    {URL}/elementos/list → Lista todas las notas con filtro

## Pasos para probar.
1. Realizar una carga de registros por admin o por {URL}/{modulo}/create, ej:  {URL}/notas/create
2. Verificar si el registro se cargó correctamente con {URL}/{modulo}, ej: {URL}/notas/
3. Buscar registros deseados dentro de la BD con {URL}/{modulo}/list, ej: {URL}/notas/list

## Models:
Se pueden visualizar todas las clases

## Views:
Se pueden visualizar todas las vistas y sus respectivos metodos

## Templates:
Dentro de templates se encuentra cada uno de los html a mostrar dependiendo la llamada realizada

## Forms:
Se pueden visualizar los formularios declarados.