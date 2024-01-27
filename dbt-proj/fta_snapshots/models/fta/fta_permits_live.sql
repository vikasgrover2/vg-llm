
/*
    dbt init --project-dir /home/jovyan/dbt-proj --profiles-dir /home/jovyan/dbt-proj/.dbt --profile fta_snapshots -d
	
{{ config(materialized='view') }}

*/
{{ config(materialized='table',
		  unique_key = ['tenure_app_id', 'forest_file_id']
		) 
}}

with source_data as (

    Select * from app_fta_backups.fta_backup_combined
	where freeze_date = '{{ var('freeze_date') }}'
)
select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
