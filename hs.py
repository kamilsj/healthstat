import sys
import argparse
import os


def healthstat(argv=None):

    parser = argparse.ArgumentParser(description='Welcome to helthstat - data science for your health and performane',
                                     usage='Type "start", to start your server')
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--configure', action='store_true')
    parser.add_argument('--relearn', action='store_true')
    parser.add_argument('--tensorflow', action='store_true')
    parser.add_argument('--export_data', action='store_true')

    args = parser.parse_args()

    if args.start == True:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthstat.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'runserver'])
    elif args.configure == True:
        pass
    elif args.relearn == True:
        pass
    elif args.tensorflow == True:
        pass
    elif args.export_data == True:
        pass
    else:
        exit(0)


if __name__=='__main__':
    healthstat(sys.argv[1:])