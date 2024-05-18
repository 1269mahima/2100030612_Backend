for location in locations:
    if location["country_id"] == "CA":
        country_name = [country["country_name"] for country in countries if country["country_id"] == location["country_id"]][0]
        print(f"Location ID: {location['location_id']}, Street Address: {location['street_address']}, City: {location['city']}, State/Province: {location['state_province']}, Country Name: {country_name}")
