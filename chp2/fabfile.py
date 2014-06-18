from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test chp2')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

from fabric.api import lcd

def deploy():
    with lcd('/Users/zeph/django-book/'):
        local('git pull /Users/zeph/dev-test/django-book/')
    with lcd('/Users/zeph/django-book/chp2/'):
        local('python manage.py migrate chp2_app')
        local('python manage.py test chp2_app')
        local('python manage.py runserver')
