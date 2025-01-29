from middleware import ActiveMethodWhitelist

# No interceptors used
interceptors = []

middleware_backend = [
    ActiveMethodWhitelist(user="username", methods=["set", "get"]),
    ActiveMethodWhitelist(user="Bob", methods=[]),
    ActiveMethodWhitelist(user="Alice", methods=["add_year", "set"]),
]

# Not using middleware for MetadataService
middleware_metadata = []
