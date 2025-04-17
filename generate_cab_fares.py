import csv

# Define the distance range
distances = list(range(1, 101))  # 1 km to 100 km

# Define the base fare rates and per km rates for each ride category (simulated rates) for each company
fare_rates = {
    "uber": {
        "bike": {"base_fare": 20, "per_km_rate": 10},      # Base fare + Per km rate
        "sedan": {"base_fare": 50, "per_km_rate": 15},      # Base fare + Per km rate
        "xl": {"base_fare": 100, "per_km_rate": 20},        # Base fare + Per km rate
        "compact": {"base_fare": 40, "per_km_rate": 12},    # Base fare + Per km rate
        "luxury": {"base_fare": 150, "per_km_rate": 25},    # Base fare + Per km rate
        "minivan": {"base_fare": 120, "per_km_rate": 22},   # Base fare + Per km rate
    },
    "ola": {
        "bike": {"base_fare": 18, "per_km_rate": 12},      # Base fare + Per km rate
        "sedan": {"base_fare": 55, "per_km_rate": 16},      # Base fare + Per km rate
        "xl": {"base_fare": 95, "per_km_rate": 22},        # Base fare + Per km rate
        "compact": {"base_fare": 45, "per_km_rate": 13},    # Base fare + Per km rate
        "luxury": {"base_fare": 145, "per_km_rate": 28},    # Base fare + Per km rate
        "minivan": {"base_fare": 130, "per_km_rate": 24},   # Base fare + Per km rate
    },
    "rapido": {
        "bike": {"base_fare": 15, "per_km_rate": 8},       # Base fare + Per km rate
        "sedan": {"base_fare": 60, "per_km_rate": 17},      # Base fare + Per km rate
        "xl": {"base_fare": 110, "per_km_rate": 23},       # Base fare + Per km rate
        "compact": {"base_fare": 50, "per_km_rate": 14},    # Base fare + Per km rate
        "luxury": {"base_fare": 155, "per_km_rate": 30},    # Base fare + Per km rate
        "minivan": {"base_fare": 140, "per_km_rate": 25},   # Base fare + Per km rate
    },
    "lyft": {
        "bike": {"base_fare": 22, "per_km_rate": 11},      # Base fare + Per km rate
        "sedan": {"base_fare": 53, "per_km_rate": 14},      # Base fare + Per km rate
        "xl": {"base_fare": 105, "per_km_rate": 21},       # Base fare + Per km rate
        "compact": {"base_fare": 42, "per_km_rate": 12},    # Base fare + Per km rate
        "luxury": {"base_fare": 140, "per_km_rate": 26},    # Base fare + Per km rate
        "minivan": {"base_fare": 125, "per_km_rate": 23},   # Base fare + Per km rate
    },
    "bolt": {
        "bike": {"base_fare": 17, "per_km_rate": 9},       # Base fare + Per km rate
        "sedan": {"base_fare": 58, "per_km_rate": 18},      # Base fare + Per km rate
        "xl": {"base_fare": 98, "per_km_rate": 19},        # Base fare + Per km rate
        "compact": {"base_fare": 43, "per_km_rate": 13},    # Base fare + Per km rate
        "luxury": {"base_fare": 135, "per_km_rate": 27},    # Base fare + Per km rate
        "minivan": {"base_fare": 115, "per_km_rate": 24},   # Base fare + Per km rate
    },
}

# Open the CSV file for writing
with open('cab_fare_estimates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    header = ["distance (km)", "uber_bike", "uber_sedan", "uber_xl", "uber_compact", "uber_luxury", "uber_minivan",
              "ola_bike", "ola_sedan", "ola_xl", "ola_compact", "ola_luxury", "ola_minivan",
              "rapido_bike", "rapido_sedan", "rapido_xl", "rapido_compact", "rapido_luxury", "rapido_minivan",
              "lyft_bike", "lyft_sedan", "lyft_xl", "lyft_compact", "lyft_luxury", "lyft_minivan",
              "bolt_bike", "bolt_sedan", "bolt_xl", "bolt_compact", "bolt_luxury", "bolt_minivan"]
    writer.writerow(header)
    
    # Write the fare estimates for each distance (from 1 km to 100 km)
    for distance in distances:
        row = [distance]
        for company, rates in fare_rates.items():
            for ride_type, rate in rates.items():
                fare = rate["base_fare"] + (distance * rate["per_km_rate"])
                row.append(fare)
        writer.writerow(row)

print("CSV file 'cab_fare_estimates.csv' created successfully!")
