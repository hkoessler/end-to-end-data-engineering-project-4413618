import os
from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource
from my_dagster import assets  # noqa: TID252

# Laden der Assets aus dem Modul
all_assets = load_assets_from_modules([assets])

# Pfad zur dbt-Projektverzeichnis aus der Umgebungsvariable
PATH_TO_DBT = os.getenv("DBT_PROJECT_DIR")

# Definieren der Ressourcen
resources = {
    "dbt": DbtCliResource(project_dir=PATH_TO_DBT)
}

# Definitions-Instanz mit Assets und Ressourcen
defs = Definitions(
    assets=all_assets,
    resources=resources
)
