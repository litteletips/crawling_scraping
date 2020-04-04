# マイグレーションするためのshell
docker exec -it scraper python django/manage.py makemigrations nutrition
docker exec -it scraper python django/manage.py migrate