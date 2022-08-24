
def build_record(Class, record):
    if not record: return None

    attrs = dict(zip(Class.columns, record))
    class_instance = Class()
    class_instance.__dict__ = attrs
    return class_instance