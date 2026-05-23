# def generaPares(limite):
#     num=1
#     milista=[]
#     while num < limite:

#         #milista.append(num*2)
#         yield num*2
#         num+=1
#     #return milista

# devuelvePares=generaPares(10)
# #for i in devuelvePares:
# #print(i)

# print(next(devuelvePares))
# print ("Aqui podra ir mas codigo")
# print(next(devuelvePares))
# print ("Aqui podra ir mas codigo")
# print(next(devuelvePares))
# print ("Aqui podra ir mas codigo")


#print(generaPares(10))

def devuelvedeCiudades(Ciudades):
    for elemento in Ciudades:
        for subelemento in elemento:
           # yield subelemento
            yield elemento
        

ciudadesDevueltas=devuelvedeCiudades("Dusambe,Minsk,Taskent,Chisinau,Bishek,Kiev")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))