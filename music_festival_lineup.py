from array import array

# Integers: Number of performances per stage
performance_counts = [12, 15, 9, 20, 17]
total_performances = sum(performance_counts)
average_performances = total_performances / len(performance_counts)
min_performances = min(performance_counts)
max_performances = max(performance_counts)

# Strings: Formatted report
report = (
    f"Total performances: {total_performances}\n"
    f"Average performances per stage: {average_performances:.2f}\n"
    f"Minimum performances on a stage: {min_performances}\n"
    f"Maximum performances on a stage: {max_performances}\n"
)
print("=== Music Festival Lineup Report ===")
print(report)

# Booleans: Threshold condition
threshold = 14
if average_performances > threshold and max_performances > 18:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: List of band names
bands = ["Echoes", "Sunrise", "Pulse", "Groove", "Harmony"]
print("\nBands before modification:", bands)

# Add a new band
bands.append("Rhythm")
# Remove a band with less than 6 letters
bands = [band for band in bands if len(band) >= 6]
bands.sort()
print("Bands after modification and sorting:", bands)

# Arrays: Store subset of performance counts
performance_array = array('i', performance_counts[:3])  # first 3 stages
array_sum = sum(performance_array)
list_sum = sum(performance_counts[:3])
print(f"\nSum of array subset: {array_sum}")
print(f"Sum of list subset: {list_sum}")

# Dictionaries: List of artist records
artists = [
    {"id": 1, "name": "Echoes", "value": 1200},
    {"id": 2, "name": "Sunrise", "value": 1500},
    {"id": 3, "name": "Pulse", "value": 900},
    {"id": 4, "name": "Groove", "value": 2000},
]

# Update one record (change 'value' for 'Pulse')
for artist in artists:
    if artist["name"] == "Pulse":
        artist["value"] = 950

# Delete another record (remove 'Sunrise')
artists = [artist for artist in artists if artist["name"] != "Sunrise"]

# Compute total 'value'
total_value = sum(artist["value"] for artist in artists)
print("\nArtist records after update and delete:")
for artist in artists:
    print(artist)
print(f"Total value across all artists: {total_value}")