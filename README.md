### 環境構築 
**Docker install**

docker images
```
engergame_nginx                latest              *************        * hours ago         127MB
engergame_python                latest              *************        * hours ago        915MB
engergame_db                   latest              *************        * hours ago        373MB
```

build コマンド
```
docker-compose up --build
```
**Nginx** port http://localhost/
<img width="1440" alt="スクリーンショット 2020-04-17 16 30 05" src="https://user-images.githubusercontent.com/56709557/79543696-d98e0800-80c8-11ea-81c1-0a7de4a5da17.png">

**Django** port http://localhost/8000 
<img width="1440" alt="スクリーンショット 2020-04-17 16 29 40" src="https://user-images.githubusercontent.com/56709557/79543719-e01c7f80-80c8-11ea-8cbe-18c4047790bb.png">


### Vue.js install
**npm  install**
```
npm -v
6.11.3
```
**node install**
```
node -v
v12.11.1
```
**vue cli install**
```
npm install -g vue-cli
```
**Vue 起動コマンド**
```
cd vue_app
npm run dev
```

**Vue** port http://localhost:8080/

<img width="1440" alt="スクリーンショット 2020-04-17 16 29 50" src="https://user-images.githubusercontent.com/56709557/79543688-d72bae00-80c8-11ea-8df6-4dde1752cdb0.png">

**Reset CSS**
```
npm install -D normalize.css
```


