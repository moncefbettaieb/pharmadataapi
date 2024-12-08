from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    cip_code: int
    title: Optional[str]
    brand: Optional[str]
    category: Optional[str]
    sub_category_1: Optional[str]
    sub_category_2: Optional[str]
    sub_category_3: Optional[str]
    sub_category_4: Optional[float]
    description: Optional[str]
    composition: Optional[str]
    use: Optional[str]
    cat_name_pharmago: Optional[str]
    cat_id_parmago: Optional[str]
    sub_cat_pharmado: Optional[str]
    sub_cat_id_pharmago: Optional[str]
    source: Optional[str]
