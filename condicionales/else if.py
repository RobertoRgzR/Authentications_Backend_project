ingreso_mensual = 7000
ContraseñaRegistrada = "Victoradir10"
contraseña_escrita = "Victoradir10"

if ingreso_mensual >= 11000 :    
    print("Eres clase media")
elif ingreso_mensual < 11000 :
    print ("Eres clase baja")
elif ingreso_mensual <= 18000 :
    print ("Eres clase media alta")
elif ingreso_mensual > 75000 :
    print ("Eres clase alta")

if ContraseñaRegistrada == contraseña_escrita :
    print ("Iniciando sesion")
elif ContraseñaRegistrada != contraseña_escrita :
    print ("Contraseña incorrecta, por favor intente otra vez")

