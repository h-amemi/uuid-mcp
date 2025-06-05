# uuid-mcp

UUID を生成する MCP サーバー。

## プロジェクトの目的
This project provides a simple **MCP** server that generates Universally Unique Identifiers (UUIDs). It can be used as an example or starting point for building custom MCP tools.

## 使い方
### 依存関係のインストール
依存パッケージは [Rye](https://rye-up.com/) で管理します。次のコマンドでロックファイルに基づきインストールできます。

```bash
rye sync
```

`requirements.lock` を使って `pip install -r requirements.lock` を実行すること
も可能ですが、基本的には Rye を利用する前提です。

### サーバーの起動
Run the server using Python:

```bash
python -m uuid_mcp.server
```

The server communicates over standard IO. Connect with any compatible MCP client and invoke the `generate_uuid` tool.

## 依存パッケージの概要
主要な依存パッケージは以下の通りです。

- **mcp** – MCP プロトコルの実装およびサーバーフレームワーク。
- **pydantic** – 設定やデータ検証に使用。
- **starlette** / **uvicorn** – ASGI 対応の Web サーバー。
- **httpx** など – SSE 通信を含む HTTP クライアント機能。

その他の依存関係については `requirements.lock` を参照してください。
