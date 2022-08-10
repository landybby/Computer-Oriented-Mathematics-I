def roots(a, b, c, d, e, f):
    count = 0  # Anzahl von Vorzeichenwechseln
    c4 = a * d  # 2. Koeffizienten zu x^4
    c3 = a * e + b * d  # 3. Koeffizienten
    c2 = a * f + b * e + c * d  # 4. Koeffizienten
    c1 = b * f + c * e  # 5. Koeffizienten
    c0 = c * f  # Konstant am Ende des Polynoms
    coef = [1, c4, c3, c2, c1, c0]  # coef[1] = 1, da c5*x^5 static
    # if c4 < 0:
    # count += 1
    for i in range(len(coef)):
        if coef[i] < 0:
            coef[i] = -1
        if coef[i] > 0:
            coef[i] = 1
        if coef[i] == 0:
            del coef[i]
    prove = coef[0]
    for i in range(len(coef) - 1):
        if prove != coef[i + 1] and (not coef[i + 1] == 0):
            count += 1
            prove = coef[i + 1]
    if count % 2 == 0 or count == 0:
        return 'Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.'
    else:
        return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.'