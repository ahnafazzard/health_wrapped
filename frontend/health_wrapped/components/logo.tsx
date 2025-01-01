import { Activity } from 'lucide-react'
import { Button } from '@/components/ui/button'
import Link from 'next/link'

export function Logo() {
  return (
    <Button variant="ghost" className="px-0 text-2xl font-bold" asChild>
      <Link href="/">
        <Activity className="mr-2 h-6 w-6" />
        Health Wrapped
      </Link>
    </Button>
  )
}

