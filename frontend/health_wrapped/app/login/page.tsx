'use client'

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Logo } from "@/components/logo"
import { GoogleSignInButton } from "@/components/GoogleSignInButton"
import { useRouter } from 'next/navigation'

export default function LoginPage() {
  const router = useRouter()

  const handleLoginSuccess = () => {
    // In a real application, you would verify the Google token on your server
    // and create a session. For this example, we'll just redirect to the dashboard.
    router.push('/dashboard')
  }

  return (
    <div className="flex flex-col min-h-screen bg-zinc-50">
      <header className="px-4 lg:px-6 h-14 flex items-center border-b bg-white">
        <Logo />
      </header>
      <main className="flex-1 flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center text-zinc-900">Login to Health Wrapped</CardTitle>
            <CardDescription className="text-center text-zinc-600">
              Sign in with your Google account to access your health dashboard
            </CardDescription>
          </CardHeader>
          <CardContent className="flex justify-center">
            <GoogleSignInButton onSuccess={handleLoginSuccess} />
          </CardContent>
        </Card>
      </main>
      <footer className="py-6 text-center border-t bg-white">
        <p className="text-sm text-zinc-500">© 2024 Health Wrapped. All rights reserved.</p>
      </footer>
    </div>
  )
}

