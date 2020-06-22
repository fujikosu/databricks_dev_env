# %%
# You can define Jupyter-like code cells within Python code using a # %% comment in vscode
# The details is here. https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells
from pyspark.sql import SparkSession


def create_dataframe():
    spark = SparkSession.builder.appName("Dbconnect test").getOrCreate()

    df = spark.createDataFrame([('Fiji Apple', 'Red', 3.5),
                                ('Banana', 'Yellow', 1.0),
                                ('Green Grape', 'Green', 2.0),
                                ('Red Grape', 'Red', 2.0),
                                ('Peach', 'Yellow', 3.0),
                                ('Orange', 'Orange', 2.0),
                                ('Green Apple', 'Green', 2.5)],
                               ['Fruit', 'Color', 'Price'])
    df.show()
    return df


# %%
df = create_dataframe()
