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
http://localhost:888/lab8
```

- 終了したい時は以下のコマンドを実行する

```
docker-compose down
```

再開したい場合は、`docker-compose up -d`を行うことでJupyterlabにアクセスできる


## 課題の提出方法

- ipynbファイル、およびSubmitフォルダ内のソースコード（.py）の所定の欄を埋め、masterブランチにpushすること

- ipynbファイルは実行結果が表示されている状態で保存すること

## レビュー要件

- レビュー対象は「.py」ファイルのみ
	- （ipynbの内容を参考にすることもあります）

- masterに反映されているもののみをレビュー対象とする
	- 途中経過は自分でブランチ切るなどして保存して良い
