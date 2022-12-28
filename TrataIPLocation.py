import re

class TrataIPLocation:
    def __init__(self, data):
        self.ip = data.get("query")
        self.country = data.get("country")
        self.region = data.get("regionName")
        self.city = data.get("city")
        self.latitude = data.get("lat")
        self.longitude = data.get("lon")
        self.time_zone = data.get("timezone")
        self.isp = data.get("isp")
        self.organization = data.get("org")
        self.asn = data.get("as")

    def __str__(self):
        return f"Endereço IP: {self.ip}\n" \
            f"País: {self.country}\n" \
            f"Região: {self.region}\n" \
            f"Cidade: {self.city}\n" \
            f"Latitude: {self.latitude}\n" \
            f"Longitude: {self.longitude}\n" \
            f"Fuso horário: {self.time_zone}\n" \
            f"ISP: {self.isp}\n" \
            f"Organização: {self.organization}\n" \
            f"ASN: {self.asn}"

    @staticmethod
    def is_valid_input(text):
        ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        domain_pattern = r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
        return bool(re.match(ip_pattern, text)) or bool(re.match(domain_pattern, text))
    