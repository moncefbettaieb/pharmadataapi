from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.db.session import database
from app.db.models.catalog import catalog_table
from app.schemas.catalog import Product
from sqlalchemy import cast, BigInteger
from app.utils.pagination import paginate


router = APIRouter()

@router.get("/", response_model=List[Product])
async def get_all_products(
    page: int = Query(default=1, ge=1, description="Numéro de la page"),
    page_size: int = Query(default=10, ge=1, description="Taille de la page (nombre d'éléments par page)")
):
    # On démarre avec une requête de base qui sélectionne tous les produits
    base_query = catalog_table.select()
    
    # On applique la pagination via votre fonction utilitaire
    paginated_query = paginate(base_query, page=page, size=page_size)
    
    # On exécute la requête paginée
    rows = await database.fetch_all(paginated_query)
    return [Product(**dict(row)) for row in rows]

@router.get("/{cip_code}", response_model=Product)
async def get_product_by_cip_code(cip_code: int):
    query = catalog_table.select().where(cast(catalog_table.c.cip_code, BigInteger) == cip_code)
    row = await database.fetch_one(query)
    if row is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**dict(row))

@router.get("/brand/{brand}", response_model=List[Product])
async def get_products_by_brand(brand: str):
    query = catalog_table.select().where(catalog_table.c.brand == brand)
    rows = await database.fetch_all(query)
    return [Product(**dict(row)) for row in rows]

@router.get("/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str):
    query = catalog_table.select().where(catalog_table.c.category == category)
    rows = await database.fetch_all(query)
    return [Product(**dict(row)) for row in rows]
