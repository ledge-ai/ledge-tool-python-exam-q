# Python課題

## 準備

- Dockerのインストール

[Macでのインストール方法](https://docs.docker.com/docker-for-mac/install/)


## 課題の取り組み方

- （初回のみ）git cloneで本リポジトリをローカルPCにクローンする

- クローンしたディレクトリに移動し、以下コマンドを実行する

```
docker-compose up -d
```

- コマンド実行後、下記にアクセスすると、Jupyterlabが起動する

```
https://localhost:8888
```

- 終了したい時は以下のコマンドを実行する

```
docker-compose down
```

再開したい場合は、`docker-compose up -d`を行うことでJupyterlabにアクセスできる


## 課題の提出方法

- 