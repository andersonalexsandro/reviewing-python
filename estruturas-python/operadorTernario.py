logged_user = True

if logged_user:
    print("usuario loggado")

else:
    print("usuario não loggado")

############## Operador ternario ##############

msg = "usuario loggado" if logged_user else "usuario não loggado"

print(msg)