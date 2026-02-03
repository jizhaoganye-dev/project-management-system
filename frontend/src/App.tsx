/**
 * メインアプリケーション
 */

import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './store/authStore'

// ページコンポーネント
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'
import DashboardPage from './pages/DashboardPage'
import ProjectsPage from './pages/ProjectsPage'
import ProjectDetailPage from './pages/ProjectDetailPage'

function App() {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated)

  return (
    <Routes>
      {/* 公開ルート */}
      <Route
        path="/login"
        element={isAuthenticated ? <Navigate to="/dashboard" /> : <LoginPage />}
      />
      <Route
        path="/register"
        element={isAuthenticated ? <Navigate to="/dashboard" /> : <RegisterPage />}
      />

      {/* 保護されたルート */}
      <Route
        path="/dashboard"
        element={isAuthenticated ? <DashboardPage /> : <Navigate to="/login" />}
      />
      <Route
        path="/projects"
        element={isAuthenticated ? <ProjectsPage /> : <Navigate to="/login" />}
      />
      <Route
        path="/projects/:id"
        element={isAuthenticated ? <ProjectDetailPage /> : <Navigate to="/login" />}
      />

      {/* デフォルトリダイレクト */}
      <Route
        path="/"
        element={<Navigate to={isAuthenticated ? '/dashboard' : '/login'} />}
      />
    </Routes>
  )
}

export default App
