import sys
import importlib

from django.core.management.base import BaseCommand, CommandError

# Some colors
OKGREEN = '\033[92m'
ENDC    = '\033[0m'
WARNING = '\033[93m'
SUC_PX  = '[success] '
WARN_PX = '[warning] '

def succ(string):
    return OKGREEN + SUC_PX + ENDC + string

def warn(string):
    return WARNING + WARN_PX + ENDC + string

MODULES = [
    'todo',
]

class Command(BaseCommand):
    args = '<module module ...>'
    help = 'File the database with fake data for the specified modules'

    def add_arguments(self, parser):
        parser.add_argument('module', nargs='+')

    def handle(self, *args, **options):
        modules = options['module']
        for module in modules:
            if module not in MODULES:
                raise CommandError('%s: unknown module' % module)
            if not importlib.util.find_spec(module):
                raise CommandError('%s: module not loaded' % module)
        for module in modules:
            fixtures_module = module + '.fixtures'
            try:
                fixtures = importlib.import_module(fixtures_module)
                if not hasattr(fixtures, 'load'):
                    self.stderr.write(warn('%s.fixtures: module does NOT '
                            'implement the required "load" function' % module))
                    continue
                results = fixtures.load()
                prefix = '%s: ' % module
                spaces = ' ' * (len(prefix) + len(WARN_PX))
                prefix = succ(prefix)
                if results:
                    self.stdout.write(prefix + results[0])
                    for i in range(1, len(results)):
                        self.stdout.write(spaces + results[i])
                    self.stdout.flush()
            except ImportError as e:
                self.stdout.write(warn('%s: module doesn\'t have fixtures'
                        % module))
                importlib.import_module(module + '.fixtures')
