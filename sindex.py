import folium
from geopy.distance import geodesic

# Coordenadas dos clientes e da casa da vendedora
coordenadas = [
    (-25.43758890555044, -49.207303066945926),  # Coordenadas da casa da vendedora
    (-25.450444135844883, -49.10508749854356),  # Coordenadas do cliente 1
    (-25.37179704615577, -49.05314411021365),  # Coordenadas do cliente 2
    (-25.45887339183854, -49.18020928887305),  # Coordenadas do cliente 3
    (-25.367797053462276, -49.076986410983174),  # Coordenadas do cliente 4
    (-25.454808432989363, -49.077871813964144),  # Coordenadas do cliente 5
    (-25.536521203956593, -49.15399518887147),  # Coordenadas do cliente 6
    (-25.452393766418442, -49.07146084938508),  # Coordenadas do cliente 7
    (-25.368420527907105, -49.07652393858306),  # Coordenadas do cliente 8
    (-25.39466744852508, -49.050874046547605),  # Coordenadas do cliente 9
    (-25.438860268712602, -49.1592450042199),  # Coordenadas do cliente 10
    (-25.423629910769804, -49.04969879113288),  # Coordenadas do cliente 11
    (-25.423649290442857, -49.0494412990716),  # Coordenadas do cliente 12
    (-25.4451163444424, -49.06458779217729),  # Coordenadas do cliente 13
    (-25.46136893468821, -49.141584646546214),  # Coordenadas do cliente 14
    (-25.44852972724144, -49.051969146807885)  # Coordenadas do cliente 15
]

# Função para calcular a distância total da rota
def calcular_distancia_total(coordenadas):
    distancia_total = 0
    for i in range(len(coordenadas) - 1):
        distancia_total += geodesic(coordenadas[i], coordenadas[i + 1]).kilometers
    return distancia_total

# Função para criar o mapa com a rota
def criar_mapa_rota(coordenadas):
    mapa = folium.Map(location=coordenadas[0], zoom_start=13)

    # Adiciona marcadores para os clientes
    for i, coord in enumerate(coordenadas[1:]):
        folium.Marker(location=coord, popup=f"Cliente {i + 1}").add_to(mapa)

    # Adiciona uma linha para representar a rota
    folium.PolyLine(locations=coordenadas, color='blue').add_to(mapa)

    # Calcula a distância total da rota
    distancia_total = calcular_distancia_total(coordenadas)

    # Adiciona a distância total como uma camada de texto no canto superior direito do mapa
    folium.map.Marker(
        [coordenadas[0][0] + 0.01, coordenadas[0][1] - 0.01],  # Ajusta a posição do texto
        icon=folium.DivIcon(html=f'<div style="font-size: 16pt">Distância Total: {distancia_total:.2f} km</div>'),
        tooltip="Distância Total"
    ).add_to(mapa)

    # Adiciona a casa da vendedora com uma marcação diferente
    folium.Marker(location=coordenadas[0], popup="Casa da Vendedora", icon=folium.Icon(color='red', icon='home')).add_to(mapa)

    return mapa

# Cria o mapa com a rota
mapa_rota = criar_mapa_rota(coordenadas)

# Salva o mapa como um arquivo HTML
mapa_rota.save("rota_vendedora_corrigida.html")

# Abre o mapa no navegador
import webbrowser

webbrowser.open("rota_vendedora_corrigida.html")
