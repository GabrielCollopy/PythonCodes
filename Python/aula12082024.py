def getHora():
    import datetime as data
    horaAtual = data.datetime.now()
    hora = horaAtual.strftime('%H:%M')
    return hora

print(getHora())
