# city_map.py
# Graph representation of Indian cities and road distances in kilometers

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