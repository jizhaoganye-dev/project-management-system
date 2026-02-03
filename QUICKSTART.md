# 🚀 クイックスタートガイド

**Project Management System - すぐに開発を始めるためのガイド**

---

## ✅ 完成している機能

### Backend（FastAPI）

```
✅ プロジェクト構造完成
✅ データベース接続設定
✅ ユーザーモデル（User）
✅ 案件モデル（Project）
✅ タスクモデル（Task）
✅ JWT認証機能
✅ パスワードハッシュ化
✅ ユーザー登録API
✅ ログインAPI
✅ 現在のユーザー情報取得API
✅ 案件CRUD API（6エンドポイント）
✅ タスクCRUD API（6エンドポイント）
```

### Frontend（React + TypeScript）

```
✅ React 18 + TypeScript
✅ Tailwind CSS
✅ React Router（認証保護ルート）
✅ TanStack Query（サーバー状態管理）
✅ Zustand（クライアント状態管理）
✅ React Hook Form + Zod（バリデーション）
✅ Axios（API通信）
✅ ログインページ
✅ 登録ページ
✅ ダッシュボードページ
✅ 案件一覧ページ
✅ 案件詳細ページ
```

---

## 💻 バックエンド起動

### Step 1: Python環境確認

```bash
# Pythonバージョン確認（3.11以上推奨）
python --version

# 仮想環境作成
cd backend
python -m venv venv

# 仮想環境有効化（Windows）
venv\Scripts\activate
```

### Step 2: 依存関係インストール

```bash
pip install -r requirements.txt
```

### Step 3: 環境変数設定

```bash
copy .env.example .env
```

### Step 4: 開発サーバー起動

```bash
uvicorn app.main:app --reload
```

### Step 5: Swagger UIで動作確認

ブラウザで http://localhost:8000/docs を開く

---

## 🎨 フロントエンド起動

```bash
cd frontend
npm install
npm run dev
```

ブラウザで http://localhost:3000 を開く

---

## 📊 API使用例

### 1. ユーザー登録

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "Test User",
    "password": "testpassword123"
  }'
```

### 2. ログイン

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=testpassword123"
```

### 3. 現在のユーザー情報取得

```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

**準備完了！今すぐ開発を始めましょう！** 🚀

最終更新: 2026年2月2日
