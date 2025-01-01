'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Logo } from "@/components/logo"
import { Activity, BarChart as BarChartIcon, FileUp, TrendingUp, Upload } from 'lucide-react'
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend, 
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Bar,
  BarChart 
} from 'recharts'

// Placeholder data
const weeklyData = [
  { week: 'Week 1', steps: 49000, distance: 35, calories: 12000, vo2max: 40 },
  { week: 'Week 2', steps: 45000, distance: 32, calories: 11000, vo2max: 41 },
  { week: 'Week 3', steps: 55000, distance: 40, calories: 13500, vo2max: 42 },
  { week: 'Week 4', steps: 40000, distance: 28, calories: 10000, vo2max: 40 },
]

const workoutTypes = [
  { name: 'Running', value: 30 },
  { name: 'Cycling', value: 20 },
  { name: 'Swimming', value: 15 },
  { name: 'Weightlifting', value: 25 },
  { name: 'Yoga', value: 10 },
]

const workoutDuration = [
  { type: 'Running', duration: 45 },
  { type: 'Cycling', duration: 60 },
  { type: 'Swimming', duration: 30 },
  { type: 'Weightlifting', duration: 50 },
  { type: 'Yoga', duration: 40 },
]

const workoutHeartRate = [
  { type: 'Running', heartRate: 150 },
  { type: 'Cycling', heartRate: 130 },
  { type: 'Swimming', heartRate: 140 },
  { type: 'Weightlifting', heartRate: 120 },
  { type: 'Yoga', heartRate: 100 },
]



export default function UserHomePage() {
  const [hasData, setHasData] = useState(true)
  const username = "John Doe" // This would normally come from authenticated user's data

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    // Here you would handle the file upload and processing
    setHasData(true)
  }

  return (
    <div className="flex flex-col min-h-screen bg-zinc-50">
      {/* Header */}
      <header className="px-4 lg:px-6 h-14 flex items-center justify-between border-b bg-white">
        <Logo />
        <span className="text-zinc-600">Welcome, {username}</span>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-4 md:p-6">
        {!hasData ? (
          <Card className="w-full max-w-md mx-auto">
            <CardHeader>
              <CardTitle className="text-2xl font-bold text-center text-zinc-900">
                Upload Your Health Data
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col items-center">
              <p className="text-zinc-600 mb-4">
                Upload your Apple Health data zip file to get started
              </p>
              <Button className="bg-zinc-900 hover:bg-zinc-800">
                <Upload className="mr-2 h-4 w-4" />
                Upload Health Data
                <input
                  type="file"
                  className="hidden"
                  onChange={handleFileUpload}
                  accept=".zip"
                />
              </Button>
            </CardContent>
          </Card>
        ) : (
<div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {/* Stats Cards */}
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Total Steps</CardTitle>
                <Activity className="h-4 w-4 text-zinc-600" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">189,000</div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Total Distance Walked</CardTitle>
                <TrendingUp className="h-4 w-4 text-zinc-600" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">135 km</div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Total Calories Burned</CardTitle>
                <FileUp className="h-4 w-4 text-zinc-600" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">46,500</div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Average VO2 Max</CardTitle>
                <BarChartIcon className="h-4 w-4 text-zinc-600" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">40.75</div>
              </CardContent>
            </Card>

            {/* Weekly Metrics Chart */}
            <Card className="md:col-span-2 h-[400px]">
              <CardHeader>
                <CardTitle>Weekly Metrics</CardTitle>
              </CardHeader>
              <CardContent className="h-[300px]">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={weeklyData}>
                    <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
                    <XAxis 
                      dataKey="week"
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                    />
                    <YAxis 
                      yAxisId="left"
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                    />
                    <YAxis 
                      yAxisId="right" 
                      orientation="right"
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                    />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: "hsl(var(--background))",
                        border: "1px solid hsl(var(--border))",
                        borderRadius: "var(--radius)",
                      }}
                      labelStyle={{ color: "hsl(var(--foreground))" }}
                    />
                    <Legend 
                      wrapperStyle={{ 
                        fontSize: "12px",
                        color: "hsl(var(--muted-foreground))"
                      }}
                    />
                    <Line
                      yAxisId="left"
                      type="monotone"
                      dataKey="steps"
                      stroke="hsl(var(--chart-1))"
                      strokeWidth={2}
                      dot={false}
                    />
                    <Line
                      yAxisId="left"
                      type="monotone"
                      dataKey="distance"
                      stroke="hsl(var(--chart-2))"
                      strokeWidth={2}
                      dot={false}
                    />
                    <Line
                      yAxisId="right"
                      type="monotone"
                      dataKey="calories"
                      stroke="hsl(var(--chart-3))"
                      strokeWidth={2}
                      dot={false}
                    />
                    <Line
                      yAxisId="right"
                      type="monotone"
                      dataKey="vo2max"
                      stroke="hsl(var(--chart-4))"
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Workout Types Pie Chart */}
            <Card className="h-[400px]">
              <CardHeader>
                <CardTitle>Workout Types</CardTitle>
              </CardHeader>
              <CardContent className="h-[300px]">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={workoutTypes}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      outerRadius={80}
                      dataKey="value"
                      label={({name, percent}) => `${name} ${(percent * 100).toFixed(0)}%`}
                    >
                      {workoutTypes.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={`hsl(var(--chart-${(index % 5) + 1}))`}
                        />
                      ))}
                    </Pie>
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "hsl(var(--background))",
                        border: "1px solid hsl(var(--border))",
                        borderRadius: "var(--radius)",
                      }}
                      labelStyle={{ color: "hsl(var(--foreground))" }}
                    />
                  </PieChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Workout Duration Bar Chart */}
            <Card className="h-[400px]">
              <CardHeader>
                <CardTitle>Average Duration per Workout Type</CardTitle>
              </CardHeader>
              <CardContent className="h-[300px]">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={workoutDuration}>
                    <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
                    <XAxis 
                      dataKey="type" 
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                    />
                    <YAxis
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                      label={{ 
                        value: 'Minutes', 
                        angle: -90, 
                        position: 'insideLeft',
                        style: { fill: "hsl(var(--muted-foreground))" }
                      }}
                    />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "hsl(var(--background))",
                        border: "1px solid hsl(var(--border))",
                        borderRadius: "var(--radius)",
                      }}
                      labelStyle={{ color: "hsl(var(--foreground))" }}
                    />
                    <Bar
                      dataKey="duration"
                      fill="hsl(var(--chart-1))"
                      radius={[4, 4, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Heart Rate Bar Chart */}
            <Card className="md:col-span-2 h-[400px]">
              <CardHeader>
                <CardTitle className="text-zinc-900">Average Heart Rate per Workout Type</CardTitle>
              </CardHeader>
              <CardContent className="h-[300px]">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={workoutHeartRate}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="type" />
                    <YAxis label={{ value: 'BPM', angle: -90, position: 'insideLeft' }} />
                    <Tooltip />
                    <Legend />
                    <Bar 
                      dataKey="heartRate" 
                      fill="#82ca9d" 
                      name="Heart Rate (BPM)"
                      radius={[4, 4, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="py-6 text-center border-t bg-white">
        <p className="text-sm text-zinc-500">© 2024 Health Wrapped. All rights reserved.</p>
      </footer>
    </div>
  )
}

