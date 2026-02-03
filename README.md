# Project Management System

**案件管理システム（フルスタックアプリケーション）**

AIプロジェクトマネージャー案件への応募用ポートフォリオ作品

---

## 🔗 リンク

| 項目 | URL |
|------|-----|
| **GitHub** | https://github.com/jizhaoganye-dev/project-management-system |
| **ライブデモ** | https://pm-demo-delta.vercel.app |

---

## 🎯 概要

本格的な案件管理システム（フルスタック）

### 技術スタック

**Backend:**
- FastAPI (Python 3.11+)
- PostgreSQL
- SQLAlchemy 2.0+
- JWT Authentication

**Frontend:**
- React 18
- TypeScript 5
- Tailwind CSS
- TanStack Query

**Deploy:**
- Backend: Railway / Render
- Frontend: Vercel
- Database: Supabase / Railway

---

## ✨ 主な機能

- ✅ ユーザー認証（JWT）
- ✅ 案件管理（CRUD）
- ✅ タスク管理
- ✅ ドキュメント管理
- ✅ 活動ログ
- ✅ ダッシュボード
- ✅ 統計情報

---

## 🌐 デモ

**ライブデモ**: https://pm-demo-delta.vercel.app

---

## 🏗️ プロジェクト構造

```
project-management-system/
├── backend/          # FastAPI バックエンド
│   ├── app/
│   │   ├── api/      # APIエンドポイント
│   │   ├── models/   # データベースモデル
│   │   ├── schemas/  # Pydanticスキーマ
│   │   └── core/     # コア機能
│   └── requirements.txt
│
├── frontend/         # React フロントエンド
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   └── hooks/
│   └── package.json
│
└── README.md
```

---

## 🚀 セットアップ

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📊 API仕様

Swagger UI: http://localhost:8000/docs

---

## 🎯 開発目的

1. Python（FastAPI）スキルの実証
2. REST API設計の実践
3. データベース設計の実践
4. フルスタック開発の実績
5. AIプロジェクトマネージャー案件への強力なアピール材料

---

## 👤 開発者

**作成日**: 2026年2月2日
**開発ツール**: Cursor + Claude（AIツール活用）

---

## 📝 License

MIT
