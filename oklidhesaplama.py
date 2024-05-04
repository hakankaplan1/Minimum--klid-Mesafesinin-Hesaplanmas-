import math

# Noktaları bir liste içinde  tanımlıyoruz. Her nokta bir demet (x, y) olarak ifade ediliyor.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# İki nokta arasındaki öklid mesafesini hesaplayan bir fonksiyon tanımlıyoruz.
def euclideanDistance(cordinate1, cordinate2):
    x1, y1 = cordinate1
    x2, y2 = cordinate2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Tüm nokta Çiftleri arasındaki meafeleri saklamak için boş bir liste oluşturuyoruz.
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        # Hesaplanan mesafeyi distances listesine ekliyoruz.
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Distances listesindeki en küçük meafeyi bulup yazdırıyoruz.
min_distance = min(distance)
print("Minimum Mesafe:", min_distance)

