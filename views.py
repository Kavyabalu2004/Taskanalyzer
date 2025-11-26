from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

def calculate_priority(task, all_tasks, strategy="smart"):
    importance = int(task.get('importance', 0))
    estimated_hours = float(task.get('estimated_hours', 0))
    due_date_str = task.get('due_date', "")
    dependencies = task.get('dependencies', [])

    # Days left calculation (default: urgent if missing)
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        days_left = (due_date - datetime.now()).days
    except Exception:
        days_left = 0  # Treat missing/invalid date as urgent

    overdue = days_left < 0
    dep_score = sum(1 for t in all_tasks if task.get('title') in t.get('dependencies', []))

    # Four strategies
    if strategy == "fastest":
        score = -estimated_hours + max(0, 15 - days_left)
        reason = "Prioritizes low-effort, quick wins."
    elif strategy == "impact":
        score = importance * 3 - estimated_hours
        reason = "Prioritizes most important tasks."
    elif strategy == "deadline":
        score = max(0, 15 - days_left) + importance - estimated_hours
        reason = "Prioritizes earliest deadlines."
    else: # default "smart"
        score = (
            importance * 2
            - estimated_hours
            + max(0, 10 - days_left)
            + dep_score * 5
        )
        if overdue:
            score += 5
            reason = "Overdue task! Gets extra boost."
        else:
            reason = (
                f"Importance x2 + Days left adjusted + Blocks {dep_score} tasks. "
                "Balanced scoring."
            )
    if not due_date_str or not importance:
        reason += " (Missing due date or importance, treated as medium priority.)"
    return round(score, 2), reason

@csrf_exempt
def analyze_tasks(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except Exception:
            return JsonResponse({"error": "Invalid JSON format!"}, status=400)

        strategy = data.get("strategy", "smart")
        tasks = data.get("tasks", [])
        results = []
        for task in tasks:
            score, reason = calculate_priority(task, tasks, strategy)
            # Add color for visual for frontend
            color = (
                "red" if score >= 20 else
                "orange" if score >= 12 else
                "green"
            )
            results.append({
                "title": task.get("title", "Untitled"),
                "score": score,
                "priority_color": color,
                "reason": reason,
                "due_date": task.get("due_date", ""),
                "estimated_hours": task.get("estimated_hours", ""),
                "importance": task.get("importance", ""),
                "dependencies": task.get("dependencies", [])
            })
        sorted_tasks = sorted(results, key=lambda x: x['score'], reverse=True)
        return JsonResponse({"tasks": sorted_tasks})

    elif request.method == "GET":
        return JsonResponse({"message": "API Connected! (GET request successful)"})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
