Setup Instructions
Clone the repository:

text
git clone <your-repo-url>
Navigate to the backend folder:


cd taskanalyser/backend

Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate  # Windows

Install dependencies:
pip install -r requirements.txt
Run the Django development server:


python manage.py runserver
Open analyze.html in a web browser to access the frontend.

Algorithm Explanation
The task priority scoring algorithm calculates a score for each task based on four main factors:

Importance: A user-provided rating (1-10) representing task criticality. It is multiplied by a weight to emphasize its influence.

Urgency: Determined by how soon the task is due. Tasks with closer deadlines or overdue tasks get higher scores.

Effort: Estimated hours required to complete the task. Lower effort tasks get a score boost to capture quick wins.

Dependencies: Tasks that block others gain extra priority, encouraging users to clear bottlenecks.

The algorithm adapts to different sorting strategies, such as prioritizing fast tasks ("Fastest Wins") or focusing solely on importance ("High Impact"). This flexibility helps users tailor task ordering based on preferences or workflow needs. The final score combines these factors with tuned weights, and tasks are sorted descending by priority score. This approach balances urgency, importance, and efficiency while respecting task dependencies.

Design Decisions
Used Django for a robust backend API to keep business logic secure and centralized.

Chose JavaScript and D3.js for frontend interactivity and visualization without heavy frontend frameworks for simplicity.

Allowed configurable sorting strategies to address varied user priorities.

Implemented dependency graph visualization to assist with complex task relationships.

Trade-off: Kept frontend simple to focus more time on algorithm correctness and backend robustness.

Time Breakdown
Task	Time Spent (hours)
Algorithm design & coding	3
Backend API implementation	2
Frontend UI & integration	2
Dependency graph visualization	1
Testing & documentation	1
Total	9

Bonus Challenges Attempted
Implemented dependency graph visualization using D3.js.

Provided different sorting strategies for flexible task prioritization.

Future Improvements
Add authentication and user-specific task management.

Enhance the algorithm with machine learning to learn user preferences.

Add calendar integration for better urgency calculation considering weekends and holidays.

Improve frontend with React for a more dynamic user experience.

Implement unit and integration tests for more comprehensive coverage.

