def cliente(informacion:dict):
  id_cliente = informacion["id_cliente"]
  nombre = informacion["nombre"]
  edad = int(informacion["edad"])
  primer_ingreso = bool(informacion["primer_ingreso"])
    
  if edad > 18:
    apto = True
    atraccion = "X-Treme"
    if primer_ingreso == True:
      total_boleta = 20000 - (20000*0.05)
    else:
      total_boleta = 20000

  elif edad >= 15 and edad <=18:
    apto = True
    atraccion = "Carros chocones"
    if primer_ingreso == True:
      total_boleta = 5000 - (5000*0.07)
    else:
      total_boleta = 5000

  elif edad >=7 and edad <15:
    apto = True
    atraccion = "Sillas voladoras"
    if primer_ingreso == True:
      total_boleta = 10000 - (10000*0.05)
    else:
      total_boleta = 10000
  else:
    atraccion = "N/A"
    apto = False
    total_boleta = "N/A"
  #para cargar todo el diccionario
  diccionario = {
    "nombre":nombre,
    "edad": edad,
    "atraccion":atraccion,
    "apto":apto,
    "primer_ingreso":primer_ingreso,
    "total_boleta":total_boleta
  }
  return diccionario


  
#para prueba
informacion = {
  "id_cliente":3,
  "nombre":"Tatiana Suarez",
  "edad":8,
  "primer_ingreso":True,
}

print(cliente(informacion))
