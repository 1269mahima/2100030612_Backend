# Query without JOIN
for location in locations:
    if location["country_id"] == "CA":
        country_name = ""
        for country in countries:
            if country["country_id"] == location["country_id"]:
                country_name = country["country_name"]
                break
        print(f"Location ID: {location['location_id']}, Street Address: {location['street_address']}, City: {location['city']}, State/Province: {location['state_province']}, Country Name: {country_name}")
