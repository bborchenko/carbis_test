import dadata


class APIRequests:
    def __init__(self, api_key, language):
        self.api_key = api_key
        self.language = language
        self.dadata = dadata.Dadata(self.api_key)
        self.addresses = None

    def get_address(self, address):
        self.addresses = self.dadata.suggest("address", address, count=10, language=self.language)

        if len(self.addresses) == 0:
            return 1
        count = 1
        for value in self.addresses:
            print(f'{count}. {value["unrestricted_value"]}')
            count += 1

        return 0

    def get_coordinates(self, value):
        data = self.addresses[int(value) - 1]['data']
        print(f'geo_lat: {data["geo_lat"]}')
        print(f'get_lon: {data["geo_lon"]}')
