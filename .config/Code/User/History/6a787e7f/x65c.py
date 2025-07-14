import requests

def calcular_distancia(origen, destino, transporte):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{origen}, Chile", f"{destino}, Argentina"],
        "vehicle": transporte,
        "key": "62103c1e-fb53-480d-8857-0d9d4fee6bdc"
    }
    response = requests.get(url, params=params).json()
    distancia_km = response["paths"][0]["distance"] / 1000
    distancia_millas = distancia_km * 0.621371
    duracion = response["paths"][0]["time"] / 3600  # en horas
    print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
    print(f"Duración: {duracion:.2f} horas")
    print("Ruta:", response["paths"][0]["instructions"])

while True:
    origen = input("Ciudad de Origen (Chile): ")
    destino = input("Ciudad de Destino (Argentina): ")
    transporte = input("Transporte (car/bike/foot): ")
    calcular_distancia(origen, destino, transporte)
    if input("¿Salir? (s/n): ").lower() == "s":
        break