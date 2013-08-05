from django.db.models import Manager


class CompatibilityManager(Manager):
    """
    An compatibility layer between Django's Manager class and custom Manager
    classes in the project. Django introduces breaking changes in 1.6 that
    might cause pains when upgrading. This class calls 1.6 style methods
    internally, and expose both 1.6 and pre-1.6 style interfaces. Users should
    always try to use the new style when subclassing to maintain forward-
    compatibility.
    """

    def get_query_set(self):
        """Pre-1.6 style if get_queryset"""
        return self.get_queryset()

    def get_queryset(self):
        """1.6 style of get_query_set"""
        if hasattr(Manager, 'get_queryset'):
            return super(CompatibilityManager).get_queryset()
        else:
            return super(CompatibilityManager).get_query_set()
