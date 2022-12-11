Прикреплен python-скрипт для поиска MTU в пути. В реализации использовалась утилита `ping`. Скрипт можно запустить на докере (Dockerfile также прикреплен).

```
docker build . -t mtu
docker run mtu <host> 
```

Пример работы (здесь `3326b5744469` - image-id образа):
```
zvank@WIN-5G93L7Q7BSN ~/tmpss> sudo docker run 3326b5744469 ya.ru
MTU: 1500
zvank@WIN-5G93L7Q7BSN ~/tmpss> sudo docker run 3326b5744469 google.com
MTU: 96
zvank@WIN-5G93L7Q7BSN ~/tmpss> sudo docker run 3326b5744469 aboba
^[[DAre you sure you provided valid host?
zvank@WIN-5G93L7Q7BSN ~/tmpss> sudo docker run 3326b5744469 192.168.10.10
Are you sure you provided valid host?
```
