from middleware import JamesCanDoAgeThings, JohnCanOnlyRead

# No interceptors used
interceptors = []

middleware_backend = [
    JohnCanOnlyRead(),
    JamesCanDoAgeThings(),
]

# Not using middleware for MetadataService
middleware_metadata = []
