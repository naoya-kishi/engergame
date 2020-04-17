### 環境構築 
**Docker install**

docker images
```
engergame_vue_app              latest              *************        * minutes ago      360MB
engergame_nginx                latest              *************        * hours ago         127MB
engergame_front                latest              *************        * hours ago        915MB
engergame_db                   latest              *************        * hours ago        373MB
```

build コマンド
```
docker-compose up --build
```

Vue 起動コマンド
```
cd vue_app
npm run serve
```

