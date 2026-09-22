# random_states.py
# 15 Random Initial and Final State pairs for AI Search Algorithms Benchmark
# Practical 1, 2, 3: Search Algorithms on Indian City Map

# 15 randomly selected (initial_state, final_state) pairs
test_pairs = [
    ("Chandigarh", "Ahmedabad"),
    ("Kota", "Kanpur"),
    ("Jhansi", "Chennai"),
    ("Bhuj", "Visakhapatnam"),
    ("Bhubaneswar", "Ranchi"),
    ("Aurangabad", "Ahmedabad"),
    ("Bhubaneswar", "Jaipur"),
    ("Jhansi", "Varanasi"),
    ("Ahmedabad", "Indore"),
    ("Visakhapatnam", "Rajkot"),
    ("Jhansi", "Solapur"),
    ("Kota", "Agra"),
    ("Gwalior", "Ranchi"),
    ("Nashik", "Kota"),
    ("Delhi", "Jaipur")
]

def get_test_pairs():
    """Return the list of 15 test pairs."""
    return test_pairs

if __name__ == "__main__":
    print("=" * 65)
    print(" 15 RANDOM INITIAL AND FINAL STATES (INDIAN CITIES MAP)")
    print("=" * 65)
    print(f"{'No.':<4} | {'Initial State (Start)':<24} | {'Final State (Goal)':<24}")
    print("-" * 65)
    for idx, (initial_state, final_state) in enumerate(test_pairs, 1):
        print(f"{idx:<4} | {initial_state:<24} | {final_state:<24}")
    print("=" * 65)
