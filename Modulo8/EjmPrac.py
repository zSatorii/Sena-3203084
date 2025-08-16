def f():
    raise OSError('operación fallida')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Ocurrió en la Iteración {i+1}')
        excs.append(e)

raise ExceptionGroup('Tenemos algunos problemas', excs)
