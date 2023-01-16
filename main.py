import rendelo

rend = rendelo.Rendelo()
ret = rend.feltolt(3)

print("Rendelt Garfield palacsinták:", rend.garfield_db())
print("A kiszolgáláshoz szükséges tányérok száma:", rend.tanyerok())
