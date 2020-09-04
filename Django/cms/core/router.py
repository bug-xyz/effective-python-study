
class MyAppRouter(object):
    """A router to control all database operations on models in
    the myapp application"""

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        # print model._meta.app_label
        if model._meta.app_label in ['common']:
            return "common"
        if model._meta.app_label in ['desktop']:
            return "desktop"
        if model._meta.app_label in ['youhong']:
            return "youhong"
        return "default"

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label in ['common']:
            return "common"
        if model._meta.app_label in ['desktop']:
            return "desktop"
        if model._meta.app_label in ['youhong']:
            return "youhong"
        return "default"


