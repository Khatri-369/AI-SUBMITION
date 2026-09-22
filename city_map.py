# city_map.py
# Graph representation of Indian cities and road distances in kilometers
import math

road_network = {
    "Ahmedabad": [("Vadodara", 110), ("Rajkot", 215), ("Udaipur", 260), ("Indore", 400)],
    "Vadodara": [("Ahmedabad", 110), ("Surat", 155), ("Indore", 390), ("Udaipur", 330)],
    "Surat": [("Vadodara", 155), ("Mumbai", 285), ("Nashik", 260)],
    "Mumbai": [("Surat", 285), ("Nashik", 170), ("Pune", 150)],
    "Pune": [("Mumbai", 150), ("Nashik", 210), ("Solapur", 250), ("Hyderabad", 560)],
    "Nashik": [("Mumbai", 170), ("Surat", 260), ("Pune", 210), ("Aurangabad", 180), ("Indore", 420)],
    "Aurangabad": [("Nashik", 180), ("Nagpur", 480), ("Hyderabad", 560), ("Indore", 410)],
    "Rajkot": [("Ahmedabad", 215), ("Bhuj", 230)],
    "Bhuj": [("Rajkot", 230), ("Ahmedabad", 335)],
    "Udaipur": [("Ahmedabad", 260), ("Vadodara", 330), ("Jaipur", 395), ("Indore", 385), ("Kota", 285)],
    "Jaipur": [("Udaipur", 395), ("Delhi", 280), ("Agra", 240), ("Kota", 250)],
    "Delhi": [("Jaipur", 280), ("Agra", 233), ("Chandigarh", 245), ("Lucknow", 555)],
    "Agra": [("Delhi", 233), ("Jaipur", 240), ("Gwalior", 120), ("Kanpur", 285)],
    "Gwalior": [("Agra", 120), ("Jhansi", 100), ("Bhopal", 420)],
    "Jhansi": [("Gwalior", 100), ("Bhopal", 330), ("Kanpur", 220)],
    "Kanpur": [("Agra", 285), ("Jhansi", 220), ("Lucknow", 90), ("Prayagraj", 200)],
    "Lucknow": [("Delhi", 555), ("Kanpur", 90), ("Prayagraj", 200), ("Varanasi", 315)],
    "Prayagraj": [("Kanpur", 200), ("Lucknow", 200), ("Varanasi", 125)],
    "Varanasi": [("Prayagraj", 125), ("Lucknow", 315), ("Patna", 255)],
    "Patna": [("Varanasi", 255), ("Ranchi", 330), ("Kolkata", 585)],
    "Ranchi": [("Patna", 330), ("Kolkata", 400), ("Raipur", 560)],
    "Kolkata": [("Patna", 585), ("Ranchi", 400), ("Bhubaneswar", 440)],
    "Bhubaneswar": [("Kolkata", 440), ("Visakhapatnam", 440), ("Raipur", 530)],
    "Visakhapatnam": [("Bhubaneswar", 440), ("Vijayawada", 350), ("Hyderabad", 620)],
    "Vijayawada": [("Visakhapatnam", 350), ("Hyderabad", 275), ("Chennai", 450)],
    "Hyderabad": [("Pune", 560), ("Aurangabad", 560), ("Nagpur", 500), ("Vijayawada", 275), ("Bengaluru", 570), ("Chennai", 630), ("Visakhapatnam", 620)],
    "Nagpur": [("Indore", 445), ("Bhopal", 350), ("Aurangabad", 480), ("Hyderabad", 500), ("Raipur", 285)],
    "Indore": [("Ahmedabad", 400), ("Vadodara", 390), ("Udaipur", 385), ("Bhopal", 195), ("Nagpur", 445), ("Nashik", 420), ("Aurangabad", 410)],
    "Bhopal": [("Indore", 195), ("Nagpur", 350), ("Jhansi", 330), ("Gwalior", 420)],
    "Raipur": [("Nagpur", 285), ("Ranchi", 560), ("Bhubaneswar", 530)],
    "Chandigarh": [("Delhi", 245)],
    "Kota": [("Jaipur", 250), ("Udaipur", 285)],
    "Bengaluru": [("Hyderabad", 570), ("Chennai", 345)],
    "Chennai": [("Bengaluru", 345), ("Vijayawada", 450), ("Hyderabad", 630)],
    "Solapur": [("Pune", 250)]
}

# Alias graph to road_network for compatibility with both naming conventions
graph = road_network

# Geographic coordinates (latitude, longitude) of all cities for straight-line distance heuristic
coordinates = {
    "Ahmedabad": (23.0225, 72.5714),
    "Vadodara": (22.3072, 73.1812),
    "Surat": (21.1702, 72.8311),
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Nashik": (19.9975, 73.7898),
    "Aurangabad": (19.8762, 75.3433),
    "Rajkot": (22.3039, 70.8022),
    "Bhuj": (23.2420, 69.6669),
    "Udaipur": (24.5854, 73.7125),
    "Jaipur": (26.9124, 75.7873),
    "Delhi": (28.6139, 77.2090),
    "Agra": (27.1767, 78.0081),
    "Gwalior": (26.2183, 78.1828),
    "Jhansi": (25.4484, 78.5685),
    "Kanpur": (26.4499, 80.3319),
    "Lucknow": (26.8467, 80.9462),
    "Prayagraj": (25.4358, 81.8463),
    "Varanasi": (25.3176, 82.9739),
    "Patna": (25.5941, 85.1376),
    "Ranchi": (23.3441, 85.3096),
    "Kolkata": (22.5726, 88.3639),
    "Bhubaneswar": (20.2961, 85.8245),
    "Visakhapatnam": (17.6868, 83.2185),
    "Vijayawada": (16.5062, 80.6480),
    "Hyderabad": (17.3850, 78.4867),
    "Nagpur": (21.1458, 79.0882),
    "Indore": (22.7196, 75.8577),
    "Bhopal": (23.2599, 77.4126),
    "Raipur": (21.2514, 81.6296),
    "Chandigarh": (30.7333, 76.7794),
    "Kota": (25.1825, 75.8391),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Solapur": (17.6599, 75.9064),
}

def straight_line_distance(city1, city2):
    """Calculate straight line distance in km between two cities using the Haversine formula."""
    if city1 == city2:
        return 0
    if city1 not in coordinates or city2 not in coordinates:
        return 0
    lat1, lon1 = coordinates[city1]
    lat2, lon2 = coordinates[city2]
    R = 6371.0  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return int(round(R * c))