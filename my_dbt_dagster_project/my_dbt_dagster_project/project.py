from pathlib import Path

from dagster_dbt import DbtProject

dbt_w_dagster_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_w_dagster").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
dbt_w_dagster_project.prepare_if_dev()