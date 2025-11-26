from datetime import datetime

def calculate_priority(task, all_tasks):
    # Extract values safely
    importance = int(task.get('importance', 0))
    estimated_hours = float(task.get('estimated_hours', 0))
    due_date_str = task.get('due_date', None)
    dependencies = task.get('dependencies', [])

    # Urgency calculation: days until due
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        days_left = (due_date - datetime.now()).days
    except Exception:
        days_left = 0  # treat invalid/missing dates as urgent

    overdue = days_left < 0

    # Dependency score: if this task blocks others, boost its score
    dep_score = sum(1 for t in all_tasks if task.get('title') in t.get('dependencies', []))

    # Simple scoring formula (tune as needed):
    score = (
        importance * 2
        - estimated_hours
        + max(0, 10 - days_left)
        + dep_score * 5
    )
    if overdue:
        score += 5  # overdue gets extra boost

    return round(score, 2)
