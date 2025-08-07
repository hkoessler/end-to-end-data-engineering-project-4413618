# set env vars - die sind im dbt
source ../dbt_transformation/config/variables.env

# dagster wird aus dem Verzeichnis mit dem dagster projekt gestartet
cd my_dagster
dagster dev