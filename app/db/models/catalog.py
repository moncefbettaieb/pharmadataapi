from sqlalchemy import Table, Column, String, BigInteger, Float, MetaData

metadata = MetaData()

catalog_table = Table(
    "pharmao",
    metadata,
    Column("cip_code", BigInteger, primary_key=True, index=True),
    Column("title", String),
    Column("brand", String),
    Column("category", String),
    Column("sub_category_1", String),
    Column("sub_category_2", String),
    Column("sub_category_3", String),
    Column("sub_category_4", Float),
    Column("description", String),
    Column("composition", String),
    Column("use", String),
    Column("cat_name_pharmago", String),
    Column("cat_id_parmago", String),
    Column("sub_cat_pharmado", String),
    Column("sub_cat_id_pharmago", String),
    Column("source", String),
)
