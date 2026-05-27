from ingestion.coingecko_ingest import (
    fetch_memecoin_data
)

from ingestion.upload_to_blob import (
    upload_file_to_blob
)

from ingestion.utils import setup_logger


logger = setup_logger()


def run_pipeline():

    try:

        logger.info(
            "Starting Memecoin ETL Pipeline"
        )

        # -----------------------------------
        # INGEST DATA
        # -----------------------------------

        file_path = fetch_memecoin_data()

        logger.info(
            f"CSV Generated: {file_path}"
        )

        # -----------------------------------
        # UPLOAD TO AZURE BLOB
        # -----------------------------------

        upload_file_to_blob(file_path)

        logger.info(
            "File Uploaded To Azure Blob"
        )

        logger.info(
            "Pipeline Executed Successfully"
        )

        print("Pipeline Executed Successfully")

    except Exception as e:

        logger.error(
            f"Pipeline Failed: {e}"
        )

        print("Pipeline Failed")


if __name__ == "__main__":

    run_pipeline()