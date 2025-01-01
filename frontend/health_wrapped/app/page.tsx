import { Activity, BarChart, FileUp, TrendingUp, Check } from 'lucide-react'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'
import { Logo } from '@/components/logo'
import { AnimatedTitle, AnimatedCard, AnimatedFeature } from '@/components/animated-components'
import Link from 'next/link'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, PieChart, Pie, Cell, ResponsiveContainer } from 'recharts'

export default function LandingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-zinc-50">
      <header className="px-4 lg:px-6 h-14 flex items-center border-b bg-white">
        <Logo />
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Button variant="ghost" className="text-sm font-medium" asChild>
            <Link href="/login">Login</Link>
          </Button>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-white flex items-center justify-center">
          <div className="container px-4 md:px-6 max-w-[1200px] mx-auto">
            <div className="flex flex-col items-center space-y-8 text-center">
              <div className="space-y-4 max-w-[800px] mx-auto">
                <AnimatedTitle>
                  Your Health Journey, Beautifully Wrapped
                </AnimatedTitle>
                <p className="mx-auto max-w-[700px] text-zinc-500 md:text-xl">
                  Upload your Apple Health data and get a stunning year-in-review dashboard of your wellness journey.
                </p>
              </div>
              <div className="space-x-4">
                <Button size="lg" className="inline-flex items-center justify-center bg-zinc-900 hover:bg-zinc-800" asChild>
                  <Link href="/login">Get Started</Link>
                </Button>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-zinc-100">
          <div className="container px-4 md:px-6 max-w-[1200px] mx-auto">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12 text-zinc-900">Key Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-[1000px] mx-auto">
              <AnimatedCard>
                <Card className="bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-zinc-900">
                      <Activity className="h-5 w-5 text-zinc-900" />
                      Comprehensive Analysis
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="text-zinc-600">
                    Get insights on your steps, heart rate, sleep patterns, and more, all in one place.
                  </CardContent>
                </Card>
              </AnimatedCard>
              <AnimatedCard>
                <Card className="bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-zinc-900">
                      <BarChart className="h-5 w-5 text-zinc-900" />
                      Beautiful Visualizations
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="text-zinc-600">
                    See your health data come to life with stunning charts and graphs.
                  </CardContent>
                </Card>
              </AnimatedCard>
              <AnimatedCard>
                <Card className="bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-zinc-900">
                      <TrendingUp className="h-5 w-5 text-zinc-900" />
                      Year-over-Year Comparisons
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="text-zinc-600">
                    Track your progress and see how your health metrics have changed over time.
                  </CardContent>
                </Card>
              </AnimatedCard>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-white">
          <div className="container px-4 md:px-6 max-w-[1200px] mx-auto">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12 text-zinc-900">
              How It Works
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center max-w-[1000px] mx-auto">
              <AnimatedFeature index={0}>
                <Card className="flex flex-col h-[250px] bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center justify-center gap-2 text-zinc-900">
                      <FileUp className="h-8 w-8 text-zinc-900" />
                      1. Upload Your Data
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex-grow flex items-center justify-center text-zinc-600">
                    <p>Securely upload your Apple Health data zip file to our platform.</p>
                  </CardContent>
                </Card>
              </AnimatedFeature>
              <AnimatedFeature index={1}>
                <Card className="flex flex-col h-[250px] bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center justify-center gap-2 text-zinc-900">
                      <Activity className="h-8 w-8 text-zinc-900" />
                      2. We Analyze
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex-grow flex items-center justify-center text-zinc-600">
                    <p>Our algorithms process your data to extract meaningful insights.</p>
                  </CardContent>
                </Card>
              </AnimatedFeature>
              <AnimatedFeature index={2}>
                <Card className="flex flex-col h-[250px] bg-white border-zinc-200">
                  <CardHeader>
                    <CardTitle className="flex items-center justify-center gap-2 text-zinc-900">
                      <BarChart className="h-8 w-8 text-zinc-900" />
                      3. Get Your Wrap
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex-grow flex items-center justify-center text-zinc-600">
                    <p>Receive a beautiful, interactive dashboard of your year in health.</p>
                  </CardContent>
                </Card>
              </AnimatedFeature>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-zinc-100">
          <div className="container px-4 md:px-6 max-w-[1200px] mx-auto">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12 text-zinc-900">
              Frequently Asked Questions
            </h2>
            <div className="max-w-[800px] mx-auto">
              <Accordion type="single" collapsible className="w-full">
                <AccordionItem value="item-1" className="border-zinc-200">
                  <AccordionTrigger className="text-zinc-900">Is my health data secure?</AccordionTrigger>
                  <AccordionContent className="text-zinc-600">
                    Yes, we take data security very seriously. Your health data is encrypted and never stored on our servers after processing.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-2" className="border-zinc-200">
                  <AccordionTrigger className="text-zinc-900">How do I export my Apple Health data?</AccordionTrigger>
                  <AccordionContent className="text-zinc-600">
                    You can export your Apple Health data from the Health app on your iPhone. Go to your profile, tap "Export Health Data", and follow the prompts.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-3" className="border-zinc-200">
                  <AccordionTrigger className="text-zinc-900">Can I use Health Wrapped with other fitness apps?</AccordionTrigger>
                  <AccordionContent className="text-zinc-600">
                    Currently, Health Wrapped only supports Apple Health data. We're working on integrating other popular fitness apps in the future.
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t bg-white">
        <Logo />
        <p className="text-xs text-zinc-500">© 2024 Health Wrapped. All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Button variant="link" size="sm" className="text-zinc-600">Terms of Service</Button>
          <Button variant="link" size="sm" className="text-zinc-600">Privacy</Button>
        </nav>
      </footer>
    </div>
  )
}

