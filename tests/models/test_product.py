from sqlalchemy import Integer, String, Boolean, Text, DateTime, Enum
import pytest
from sqlalchemy.dialects.postgresql import UUID

def test_true():
    assert True

@pytest.mark.model
def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("product")
    

@pytest.mark.model
def test_model_structure_column_data_types(db_inspector):
    table="product"
    columns = {columns["name"] : columns for columns in db_inspector.get_columns(table)}


    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["pid"]["type"], UUID)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["description"]["type"], Text)
    assert isinstance(columns["is_digital"]["type"], Boolean)
    assert isinstance(columns["created_at"]["type"], DateTime)
    assert isinstance(columns["updated_at"]["type"], DateTime)
    assert isinstance(columns["stock_status"]["type"], Enum)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["category_id"]["type"], Integer)
    


@pytest.mark.model
def test_model_structure_nullable_constraints(db_inspector):
    table = "product"
    columns = db_inspector.get_columns(table)

    expected_nullable = {
        "id": False,
        "name": False,
        "slug": False,
        "is_active": False,
        "description": True,
        "is_digital": False,
        "created_at": False,
        "updated_at": False,
        "stock_status": False,
        "category_id": False,
    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"] == expected_nullable.get(
            column_name
            ), f"column '{column_name}' is not nullable as expected"


@pytest.mark.model
def test_model_structure_column_constraints(db_inspector):
    table = "product"
    constraints = db_inspector.get_check_constraints(table)

    assert any(constraint["name"] == "product_name_length_check" for constraint in constraints)
    assert any(constraint["name"] == "product_slug_length_check" for constraint in constraints)


@pytest.mark.model
def test_model_structure_default_values(db_inspector):
    table = "product"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}
    
    assert columns["is_digital"]["default"] == "false"
    assert columns["is_active"]["default"] == "false"
    assert columns["stock_status"]["default"] == "oos'::status_enum"


@pytest.mark.model
def test_model_structure_column_lengths(db_inspector):
    table = "product"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}

    assert columns["name"]["type"].length == 200
    assert columns["slug"]["type"].length == 220


@pytest.mark.model
def test_model_structure_unique_constriants(db_inspector):
    table = "product"
    constraints = db_inspector.get_unique_constraints(table)

    assert any(constraint["name"] == "uq_product_name_level" for constraint in constraints)
    assert any(constraint["name"] == "uq_product_slug" for constraint in constraints)

