from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        from test_app.models import RelatedModel, MyModel

        m = MyModel.objects.create()
        r = RelatedModel.objects.create(thing=m)

        print(list(r.many.all()))
        #
        # import sys, sysconfig, collections
        # from django.utils.autoreload import iter_all_python_module_files
        # counter = collections.Counter()
        # purelib = sysconfig.get_path("purelib")
        # stdlib = sysconfig.get_path("stdlib")
        # for path in iter_all_python_module_files():
        #     if str(path).startswith(purelib):
        #         key = "purelib"
        #     elif str(path).startswith(stdlib):
        #         key = "stdlib"
        #     else:
        #         key = "other"
        #     counter[key] += 1
        #     print(f'{path} = {key}')
        # print(purelib)
        # print(counter)
