**ER図**
***
**schemaspy Relationships.html**

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


***Vue.js install***

### VERSION 一覧
|  command   |   version   |
|:-----------|------------:|
| npm -v     |  6.11.3n    |
| node -v    |  v12.11.1   |
| yarn -v    |  1.19.0     |


+ [x] homebrewのインストール
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
+ [x] nodebrewのインストール
```
 brew install nodebrew
```
**確認**
```
 nodebrew -v
```
+ [x] バージョンを指定してインスール
```
nodebrew install-binary 12.11.1
```
**確認**
```
 nodebrew list
 > v12.11.1
```

+ [x] Webpack install
```
 npm install webpack-dev-server -g
```

+ [x] webpack-dev-serverの導入
```
//最新のバージョンを確認
$npm info webpack-dev-server
//インストール
$npm install --save-dev webpack-dev-server@2.9.1
```

+ [x] 使用Library
**Reset CSS**
```
npm install -D normalize.css
```

**Font awesome**
```
$ yarn add @fortawesome/fontawesome-svg-core
$ yarn add @fortawesome/free-solid-svg-icons
$ yarn add @fortawesome/vue-fontawesome
```

**axios**
```
npm install axios
```

**Vuex**
```
npm install vuex install --save
```

参考URL
> https://github.com/axios/axios#example

**起動**
```
npm run dev
```

**Vue** port http://localhost:8081/


+ [x] Mock Server を使用
仮想サーバーを構築してJSON型Dataを扱うため
```
npm install axios --save
npm install -g instant-mock
cd mymock
instant-mock
```

**参考URL**
 - https://qiita.com/akakuro43/items/600e7e4695588ab2958d
 - https://qiita.com/fuwamaki/items/3d8af42cf7abee760a81
 - https://qiita.com/yn01/items/d1fa10dbe4850f7cd693
 - https://qiita.com/bumptakayuki/items/01c3ebeb928a127e7af9
 
**Vue.js VS code 拡張機能**
 - https://iwb.jp/vscode-vuejs-extensions-install-settings/
