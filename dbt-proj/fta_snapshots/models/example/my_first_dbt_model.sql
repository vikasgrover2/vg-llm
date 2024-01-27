
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml
	dbt init --project-dir /home/jovyan/dbt-proj --profiles-dir /home/jovyan/dbt-proj/.dbt --profile fta_snapshots -d
    Try changing "table" to "view" below


{{ config(materialized='table') }}
*/
{{ config(materialized='view') }}

with source_data as (

    select '011824' as freeze_id
,days_to_process
,days_of_backlog
,backlog_ind
,active_ind
,target_days_to_process
,tenure_app_id
,tenure_appname
,tenure_application_state_code
,tenure_application_state_desc
,tenure_application_type_code
,tenure_application_type_desc
,tenure_app_purp_code
,app_purpose_desc
,org_unit_no
,district_code
,district_name
,region_org_unit_no
,region_org_unit_code
,region_code from app_fta_backups.fta_backup_after2015_011824
)
select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
