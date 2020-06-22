import pytest
from utils import get_shape
from pyspark.sql import SparkSession


@pytest.fixture
def spark():
    """Spark Session fixture
    """
    spark = SparkSession.builder.master("local[2]").appName(
        "Unit Testing").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark


def test_get_shape(spark):
    """Test data transform"""
    shape_2_2_df = spark.read.option("multiLine",
                                     True).json("tests/data/shape_2_2.json")
    assert get_shape(shape_2_2_df) == (2, 2)
