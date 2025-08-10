nota = 85

if nota >= 90:
    print("Excelente, sacaste una A.")
elif nota >= 80:
    # Se evalúa solo si la nota NO fue >= 90
    print("Muy bien, sacaste una B.")
elif nota >= 70:
    # Se evalúa solo si la nota NO fue >= 90 Y NO fue >= 80
    print("Bien, sacaste una C.")
else:
    # Se evalúa solo si NINGUNA de las anteriores fue verdadera
    print("Necesitas mejorar, sacaste una D o F.")
