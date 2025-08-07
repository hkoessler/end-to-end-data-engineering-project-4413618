import os
from pathlib import Path
from dagster import AssetExecutionContext, Definitions
from dagster_dbt import DbtCliResource, dbt_assets, DbtProject

# Pfad zur dbt-Projektverzeichnis aus der Umgebungsvariable
PATH_TO_DBT = os.getenv("DBT_PROJECT_DIR")
PATH_TO_PROFILES = os.getenv("DBT_PROFILES_DIR")

my_project = DbtProject(
    project_dir=PATH_TO_DBT,
    profiles_dir=PATH_TO_PROFILES
)


@dbt_assets(manifest=my_project.manifest_path)
def my_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
