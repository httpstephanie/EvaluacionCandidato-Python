#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
#"Cumples con los requisitos para postularte"
#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
#"Para postularte, necesitas tener conocimientos de inglés"
#"Para postularte, necesitas saber programar en Python"
habla_ingles = True
sabe_python = False
 
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")