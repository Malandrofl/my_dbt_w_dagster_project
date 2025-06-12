from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import dbt_w_dagster_project


@dbt_assets(manifest=dbt_w_dagster_project.manifest_path)
def dbt_w_dagster_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    