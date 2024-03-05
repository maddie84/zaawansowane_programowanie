import requests

class Brewery:
    def __init__(self, id, name, brewery_type, street, city, state, postal_code, country, phone, website_url):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return f"Brewery ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\n" \
               f"Address: {self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}\n" \
               f"Phone: {self.phone}\nWebsite: {self.website_url}\n"

def fetch_breweries():
    api_url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(api_url)
    breweries_data = response.json()[:20]  # Pobranie 20 pierwszych obiektów
    return breweries_data

def main():
    breweries_data = fetch_breweries()

    breweries_instances = []
    for brewery_data in breweries_data:
        brewery_instance = Brewery(
            id=brewery_data['id'],
            name=brewery_data['name'],
            brewery_type=brewery_data['brewery_type'],
            street=brewery_data['street'],
            city=brewery_data['city'],
            state=brewery_data['state'],
            postal_code=brewery_data['postal_code'],
            country=brewery_data['country'],
            phone=brewery_data['phone'],
            website_url=brewery_data['website_url']
        )
        breweries_instances.append(brewery_instance)

    for brewery_instance in breweries_instances:
        print(brewery_instance)

if __name__ == "__main__":
    main()