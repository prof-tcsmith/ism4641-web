#!/usr/bin/env python3
"""
Update index.html to point to the correct file locations based on what actually exists.
"""

import os
import re

# Map of what files actually exist for each week
week_files = {
    'week01': {
        'lecture-slides.html': 'week01/lecture-slides.html',
        'lecture-notes.html': 'week01/lecture-notes.html', 
        'assignment.html': 'week01/assignment.html',
        'practice-problems.html': 'week01/practice-problems.html',
        'solutions.html': 'week01/solutions.html'
    },
    'week02': {
        'lecture-slides.html': 'week02/lecture-slides.html',
        'lecture-notes.html': 'docs/week02/lecture-notes.html',
        'assignment.html': 'week02/assignment.html',
        'practice-problems.html': 'week02/practice-problems.html',
        'solutions.html': 'week02/solutions.html',
        'problem-set.html': 'docs/week02/problem-set.html'
    },
    'week03': {
        'lecture-slides.html': 'week03/lecture-slides.html',
        'lecture-notes.html': 'docs/week03/lecture-notes.html',
        'assignment.html': 'week03/assignment.html',
        'practice-problems.html': 'week03/practice-problems.html',
        'solutions.html': 'week03/solutions.html',
        'case-study.html': 'week03/case-study.html',
        'problem-set.html': 'docs/week03/problem-set.html',
        'problem-set-solutions.html': 'docs/week03/problem-set-solutions.html'
    },
    'week04': {
        'lecture-slides.html': 'week04/lecture-slides.html',
        'lecture-notes.html': 'docs/week04/lecture-notes.html',
        'assignment.html': 'week04/assignment.html',
        'practice-problems.html': 'week04/practice-problems.html',
        'case-study.html': 'week04/case-study.html',
        'practice-problem-set.html': 'docs/week04/practice-problem-set.html'
    },
    'week05': {
        'lecture-slides.html': 'week05/lecture-slides.html',
        'lecture-notes.html': 'docs/week05/lecture-notes.html',
        'assignment.html': 'week05/assignment.html',
        'practice-problems.html': 'week05/practice-problems.html',
        'case-study.html': 'week05/case-study.html'
    },
    'week06': {
        'review-guide.html': 'week06/review-guide.html',
        'practice-exam.html': 'week06/practice-exam.html'
    },
    'week07': {
        'lecture-slides.html': 'week07/lecture-slides.html',
        'lecture-notes.html': 'week07/lecture-notes.html',
        'assignment.html': 'week07/assignment.html',
        'practice-problems.html': 'week07/practice-problems.html',
        'case-study.html': 'week07/case-study.html',
        'problem-set.html': 'docs/week07/problem-set.html'
    },
    'week08': {
        'lecture-slides.html': 'week08/lecture-slides.html',
        'lecture-notes.html': 'docs/week08/lecture-notes.html',
        'assignment.html': 'week08/assignment.html',
        'practice-problems.html': 'week08/practice-problems.html',
        'case-study.html': 'week08/case-study.html'
    },
    'week09': {
        'lecture-slides.html': 'week09/lecture-slides.html',
        'lecture-notes.html': 'week09/lecture-notes.html',
        'assignment.html': 'week09/assignment.html',
        'practice-problems.html': 'week09/practice-solutions.html',  # Note: file is actually practice-solutions
        'solutions.html': 'week09/practice-solutions.html'
    },
    'week10': {
        'lecture-slides.html': 'week10/lecture-slides.html',
        'lecture-notes.html': 'week10/lecture-notes.html',
        'assignment.html': 'week10/assignment.html',
        'practice-problems.html': None  # Doesn't exist
    },
    'week11': {
        'lecture-slides.html': 'week11/lecture-slides.html',
        'lecture-notes.html': 'week11/lecture-notes.html',
        'assignment.html': 'week11/assignment.html',
        'practice-problems.html': 'week11/practice-problems.html',
        'solutions.html': 'week11/solutions.html'
    },
    'week12': {
        'lecture-slides.html': 'week12/lecture-slides.html',
        'lecture-notes.html': 'week12/lecture-notes.html',
        'assignment.html': 'week12/assignment.html',
        'practice-problems.html': 'week12/practice-problems.html',
        'solutions.html': 'week12/solutions.html',
        'problem-set.html': 'docs/week12/problem-set.html'
    },
    'week13': {
        'lecture-slides.html': 'week13/lecture-slides.html',
        'recap-notes.html': 'week13/recap-notes.html',
        'advanced-concepts.html': None,  # Doesn't exist
        'practice-exam.html': None  # Doesn't exist
    },
    'week14': {
        'project-guidelines.html': None,  # Doesn't exist
        'review-problems.html': None,  # Doesn't exist
        'solutions.html': None  # Doesn't exist
    },
    'week15': {
        'presentation-tips.html': None,  # Doesn't exist
        'final-review.html': None  # Doesn't exist
    }
}

def update_index():
    """Update index.html with correct file paths."""
    
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Track what we're updating
    updates = []
    
    for week, files in week_files.items():
        for filename, actual_path in files.items():
            # Pattern to find links like href="week01/lecture-slides.html"
            pattern = f'href="{week}/{filename}"'
            
            if actual_path:
                # File exists, update path if needed
                new_href = f'href="{actual_path}"'
                if pattern in content and new_href != pattern:
                    content = content.replace(pattern, new_href)
                    updates.append(f"Updated {week}/{filename} -> {actual_path}")
            else:
                # File doesn't exist, we'll need to remove or comment out the link
                # For now, let's change it to a disabled link
                if pattern in content:
                    # Find the entire <a> tag and disable it
                    link_pattern = f'<a href="{week}/{filename}"[^>]*>(.*?)</a>'
                    replacement = r'<span class="material-link disabled" style="opacity: 0.5; cursor: not-allowed;">\1</span>'
                    content = re.sub(link_pattern, replacement, content)
                    updates.append(f"Disabled {week}/{filename} (file doesn't exist)")
    
    # Save updated index.html
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("Index.html updated!")
    for update in updates:
        print(f"  - {update}")
    
    return len(updates)

if __name__ == "__main__":
    updates = update_index()
    print(f"\nTotal updates: {updates}")