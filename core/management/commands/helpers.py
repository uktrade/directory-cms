from django_pglocks import advisory_lock


class ExclusiveDistributedHandleMixin:
    lock_id = None

    def handle(self, *args, **options):
        with advisory_lock(lock_id=self.lock_id, wait=False) as acquired:
            # if this instance was the first to call the command then
            # continue to execute the underlying management command...
            if acquired:
                super().handle(*args, **options)
            else:
                # ...otherwise wait for the command to finish to finish.
                with advisory_lock(lock_id=self.lock_id):
                    pass
