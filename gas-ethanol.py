ethanol = float(input())
gas = float(input())

delta = ethanol / gas

if (delta <= 0.73):
    print("ETANOL")
else:
    print("GASOLINA")
