import Link from 'next/link'
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-background to-muted">
      <main className="container mx-auto px-4 py-16">
        {/* Hero Section */}
        <div className="flex flex-col items-center justify-center text-center space-y-8 pt-20">
          <h1 className="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary/60">
            Health Wrapped
          </h1>
          
          <p className="text-xl text-muted-foreground max-w-2xl">
            Your year in fitness, visualized beautifully. Upload your health data to see your personal health journey.
          </p>

          <div className="space-x-4 pt-8">
            <Button size="lg" asChild>
              <Link href="/auth/login">
                Get Your Health Wrapped
              </Link>
            </Button>
            
          </div>
        </div>

        {/* Features Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-24">
          {[
            {
              title: "Year in Review",
              description: "See your fitness journey throughout the year with beautiful visualizations"
            },
            {
              title: "Personal Insights",
              description: "Discover patterns and achievements in your workout data"
            },
            {
              title: "Share Your Story",
              description: "Create shareable cards highlighting your fitness milestones"
            }
          ].map((feature) => (
            <div key={feature.title} className="p-6 rounded-lg border bg-card">
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-muted-foreground">{feature.description}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}