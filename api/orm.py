
def build_record(Class, record):
    if not record: return None

    attrs = dict(zip(Class.columns, record))
    class_instance = Class()
    class_instance.__dict__ = attrs
    return class_instance

def save_record(conn, cursor, object, table):
    
    keys = object.__dict__.keys() # list of values
    values = [str(value) for value in object.__dict__.values()]
    keys_str = ','.join(keys)
    values_str = ','.join(values)

    insert_sql = f"""
        INSERT INTO {table} ({keys_str})
        VALUES ({values_str})
    """
    cursor.execute(insert_sql)

def drop_records(conn, cursor, table):
    cursor.execute(f'DELETE FROM {table}')



