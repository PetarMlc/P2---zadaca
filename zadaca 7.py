def rekurzivna(a):
    if a == '':
        return ''
    return rekurzivna(a[1:]) + a[0]

unos = input('Unesite neki string: ')
print(rekurzivna(unos))
