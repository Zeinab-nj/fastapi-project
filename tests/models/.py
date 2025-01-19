from sqlalchemy import Integer, String, Boolean
import pytest


def test_true():
    assert True

@pytest.mark.model
def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("category")
    

@pytest.mark.model
def test_model_structure_column_data_types(db_inspector):
    table="category"
    columns = {columns["name"] : columns for columns in db_inspector.get_columns(table)}


    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["parent_id"]["type"], Integer)


@pytest.mark.model
def test_model_structure_nullable_constraints(db_inspector):
    table = "category"
    columns = db_inspector.get_columns(table)

    expected_nullable = {
        "id": False,
        "name": False,
        "slug": False,
        "is_active": False,
        "level": False,
        "parent_id": True,
    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"] == expected_nullable.get(
            column_name
            ), f"column '{column_name}' is not nullable as expected"


@pytest.mark.model
def test_model_structure_column_constraints(db_inspector):
    table = "category"
    constraints = db_inspector.get_check_constraints(table)

    assert any(constraint["name"] == "name_length_check" for constraint in constraints)
    assert any(constraint["name"] == "name_length_check" for constraint in constraints)


@pytest.mark.model
def test_model_structure_default_values(db_inspector):
    table = "category"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}
    
    assert columns["is_active"]["default"] == "false"
    assert columns["level"]["default"] == "100"


@pytest.mark.model
def test_model_structure_column_lengths(db_inspector):
    table = "category"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}

    assert columns["name"]["type"].length == 100
    assert columns["slug"]["type"].length == 120


@pytest.mark.model
def test_model_structure_unique_constriants(db_inspector):
    table = "category"
    constraints = db_inspector.get_unique_constraints(table)

    assert any(constraint["name"] == "uq_category_name_level" for constraint in constraints)
    assert any(constraint["name"] == "uq_category_slug" for constraint in constraints)

