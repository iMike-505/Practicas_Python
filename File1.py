## Listas ##
Lista_1 = list()
Lista_2 = []

print(len(Lista_1))
Lista_1 = [12, 22, 8, 78, 66, 30, 75]

print(Lista_1)
print(len(Lista_1))

Lista_2 = [94, 21, 40, 85, 30, "Apolo", "Artemis"]

# En una lista podemos acceder a los elementos por separado
print(Lista_2[5])

print(Lista_2[0])
print(Lista_2[6])
print(Lista_2[-1])
print(Lista_2[-7])

# Podemos concatenar listas
print(Lista_1 + Lista_2)

# Para aniadir otros elementos se usa append e insert
Lista_2.append("Gojo")
print(Lista_2)

Lista_2.insert(0, "Purpura")
print(Lista_2)

Lista_2.insert(1, "Rojo")
print(Lista_2)

#Para eliminar elemento en la lista se usa remove, para eliminar todo, se usa clear 
Lista_2.remove("Apolo")
print(Lista_2)

print(Lista_2.pop())
print(Lista_2)

Lista_3 = Lista_2.copy()
print(Lista_3)

# Ordena la lista al reves
Lista_3.reverse()
print(Lista_3)

