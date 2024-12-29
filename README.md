Product Requirements Document: Health Year in Review
1. Product Overview
1.1 Product Description
A web application that transforms Apple Health data into an engaging, Spotify Wrapped-style year-in-review experience, providing visual insights and social comparisons of health metrics.
1.2 Project Context
MVP development for hackathon release, focusing on core functionality and essential features.
1.3 User Problem
Users have access to extensive health data through Apple Health but lack:
Visual representation of annual health trends
Comparative analysis with other users and family members
Engaging presentation of health achievements
Gamification elements to motivate health improvements
2. Technical Requirements
2.1 Authentication
Google OAuth integration only
No email/password authentication options
Secure user session management
2.2 Data Management
Support for Apple Health data zip file upload
Python parser integration for data extraction
Supabase database storage
User-data association
Data overwrite capability for updated uploads
Family group data management
3. Features & Functionality
3.1 Core Analytics
Annual Totals
Total distance walked
Total steps
Number of workouts
Active calories burned
Activity Analysis
Highest calorie-burning activity
Most frequent workout type
Best workout weeks
Peak calorie-burning weeks
Missed workout days
Avg Heart rate
Avg VO2 max
Health Analytics
User metrics vs. platform averages
User metrics vs. family averages (if in family)
3.2 Family Features
Option to create a family group
Option to join existing family group
Family comparison dashboard
Family average metrics
Optional feature (not required for basic functionality)
3.3 User Interface
Mobile-responsive design
Interactive dashboard
Visual data representations
Progress indicators
Achievement badges
Family comparison views (when applicable)
4. User Flow
Authentication


Google sign-in
Account creation/linking
Family Options
Create or join family (optional)
Family code generation/input
Skip option
Data Upload
File upload interface
Progress indicator
Success/error messaging
Dashboard View
Individual summary statistics
Detailed metrics
Global comparative analysis
Family comparative analysis (if applicable)
Share capabilities
5. Technical Architecture
5.1 Frontend
React.js
Responsive design framework
Data visualization libraries
Progressive Web App capabilities
5.2 Backend
Python data parser
Supabase integration
Google OAuth implementation
Family group management system
6. Data Security & Privacy
6.1 Privacy Considerations
User consent for data sharing
Anonymous comparative analytics
Data retention policies
Clear privacy policy
Family data sharing permissions