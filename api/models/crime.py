class Crime:
    columns = [
        'id',
        'lurn_sak',
        'incident_date',
        'incident_reported_date',
        'category',
        'stat',
        'stat_desc',
        'address',
        'street',
        'city',
        'zip',
        'incident_id',
        'reporting_district',
        'seq',
        'gang_related',
        'unit_id',
        'unit_name',
        'longitude',
        'latitude',
        'part_category'
    ]

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        for key, value in kwargs.items():
            setattr(self, key, value)
