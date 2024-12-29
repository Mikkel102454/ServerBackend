import uuid
def generate_uuid():
    return f"{uuid.uuid4()}".replace('-', '')