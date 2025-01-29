from middleware import ActiveMethodWhitelist

# No interceptors used
interceptors = []

middleware_backend = [
    ActiveMethodWhitelist(user="username", methods=["set", "get"]),
    ...
]

# Not using middleware for MetadataService
middleware_metadata = []
