/* dbt snapshot --select "fta_weekly_snapshot" --profiles-dir /home/jovyan/dbt-proj/.dbt --profile fta_snapshots*/

{% snapshot fta_weekly_snapshot %}

    {{
        config(
          target_schema='dbt_snapshots',
          strategy='check',
          unique_key='id',
          invalidate_hard_deletes=True,
          check_cols=['tenure_application_state_code','tenure_application_type_code','tenure_app_purp_code','district_code','region_code','decision_date','issuance_date','submission_date']
        )
    }}

    select tenure_app_id||'-'||forest_file_id as id, * from {{ source('fta_raw', 'fta_permits_live') }}

{% endsnapshot %}