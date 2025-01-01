'use client'

import { useEffect } from 'react'

declare global {
  interface Window {
    google?: {
      accounts: {
        id: {
          initialize: (config: any) => void
          renderButton: (element: HTMLElement, config: any) => void
        }
      }
    }
  }
}

interface GoogleSignInButtonProps {
  onSuccess: (response: any) => void
}

export function GoogleSignInButton({ onSuccess }: GoogleSignInButtonProps) {
  useEffect(() => {
    const script = document.createElement('script')
    script.src = 'https://accounts.google.com/gsi/client'
    script.async = true
    script.defer = true
    document.body.appendChild(script)

    script.onload = () => {
      if (window.google) {
        window.google.accounts.id.initialize({
          client_id: 'YOUR_GOOGLE_CLIENT_ID', // Replace with your actual Google Client ID
          callback: handleCredentialResponse
        })
        window.google.accounts.id.renderButton(
          document.getElementById("googleSignInDiv")!,
          { theme: "outline", size: "large" }
        )
      }
    }

    return () => {
      document.body.removeChild(script)
    }
  }, [onSuccess])

  function handleCredentialResponse(response: any) {
    console.log("Encoded JWT ID token: " + response.credential)
    onSuccess(response)
  }

  return <div id="googleSignInDiv"></div>
}

