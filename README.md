# 環境構築 
## Docker install(Docker for Mac)

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


## Vue.js install
### ローカルにInstall
### VERSION 一覧
**npm**
```
npm -v
6.11.3n
```
**node**
```
node -v
v12.11.1
```
**yarn**
```
yarn -v
1.19.0
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

**Vue** port http://localhost:8081/

<img width="1440" alt="スクリーンショット 2020-04-17 16 29 50" src="https://user-images.githubusercontent.com/56709557/79543688-d72bae00-80c8-11ea-8df6-4dde1752cdb0.png">

### homebrowのインストール
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### nodebrewのインストール
```
 brew install nodebrew
```
**確認**
```
 nodebrew -v
```
### バージョンを指定してインスール
```
nodebrew install-binary 12.11.1
```
**確認**
```
 nodebrew list
 > v12.11.1
```

### Webpack install
```
 npm install webpack-dev-server -g
```

### webpack-dev-serverの導入
```
//最新のバージョンを確認
$npm info webpack-dev-server
//インストール
$npm install --save-dev webpack-dev-server@2.9.1
```

### ライブラリー
**Reset CSS**
```
npm install -D normalize.css
```

**Font awesome**
```
> yarn add @fortawesome/fontawesome-svg-core
> yarn add @fortawesome/free-solid-svg-icons
> yarn add @fortawesome/vue-fontawesome
```





**参考URL**
 > https://qiita.com/akakuro43/items/600e7e4695588ab2958d
 > https://qiita.com/fuwamaki/items/3d8af42cf7abee760a81
 >> https://qiita.com/yn01/items/d1fa10dbe4850f7cd693
 >> https://qiita.com/bumptakayuki/items/01c3ebeb928a127e7af9
 
**Vue.js VS code 拡張機能**
 > https://iwb.jp/vscode-vuejs-extensions-install-settings/
