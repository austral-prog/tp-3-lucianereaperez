def slice_simple():
    texto = "Awesome"
    low = texto.lower()
    print(low[0:3])
    print(low[2:5])
    print(low[0:7])

slice_simple()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
