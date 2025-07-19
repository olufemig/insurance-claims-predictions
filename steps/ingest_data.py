import logging
import pandas as pd
from zenml import step
from typing_extensions import Annotated

@step
def import_csv_data(
    file_path: str
) -> Annotated[pd.DataFrame, "csv_data"]:
    """
    ZenML step to import data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        encoding: File encoding (defaults to 'utf-8')
        delimiter: CSV delimiter (defaults to ',')
    
    Returns:
        pandas DataFrame containing the CSV data
    """
    file_path = "/data/insurance.csv"
    logging.info(f"Starting CSV import from...")
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")