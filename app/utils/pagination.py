def paginate(query, page: int = 1, size: int = 10):
    # Exemple simplifié
    offset = (page - 1) * size
    return query.limit(size).offset(offset)
