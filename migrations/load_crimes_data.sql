COPY crimes (
    lurn_sak,
    incident_date,
    incident_reported_date,
    category,
    stat,
    stat_desc,
    address,
    street,
    city,
    zip,
    incident_id,
    reporting_district,
    seq,
    gang_related,
    unit_id,
    unit_name,
    longitude,
    latitude,
    part_category
)

FROM 'C:\Users\Public\Documents\lasd_crimes_data.csv'
DELIMITER ','
CSV HEADER;