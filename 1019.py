# horas	3600
# restante	60
# restante do restante	

tempo = int(input())
horas = tempo // 3600
restante = tempo % 3600
minutos = restante // 60
segundos = restante % 60

print('{0}:{1}:{2}'.format(horas, minutos, segundos))
