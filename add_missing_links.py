#!/usr/bin/env python3
"""
Add missing links to problem sets in index.html for weeks that have them.
"""

import re

def add_missing_links():
    """Add missing problem set links to index.html."""
    
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Add problem set link to week 2
    week02_pattern = r'(<a href="week02/solutions\.html"[^>]*>.*?</a>)'
    week02_replacement = r'\1\n                    <a href="docs/week02/problem-set.html" class="material-link">\n                        <i class="fas fa-file-alt material-icon"></i>\n                        <span>Problem Set</span>\n                    </a>'
    
    if 'docs/week02/problem-set.html' not in content:
        content = re.sub(week02_pattern, week02_replacement, content)
        print("Added Problem Set link to Week 2")
    
    # Add problem set link to week 3 (already has problem-set-solutions link)
    week03_pattern = r'(<a href="week03/case-study\.html"[^>]*>.*?</a>)'
    week03_replacement = r'<a href="docs/week03/problem-set.html" class="material-link">\n                        <i class="fas fa-file-alt material-icon"></i>\n                        <span>Problem Set</span>\n                    </a>\n                    <a href="docs/week03/problem-set-solutions.html" class="material-link">\n                        <i class="fas fa-check-circle material-icon"></i>\n                        <span>Problem Set Solutions</span>\n                    </a>\n                    \1'
    
    if 'docs/week03/problem-set.html' not in content:
        content = re.sub(week03_pattern, week03_replacement, content)
        print("Added Problem Set and Solutions links to Week 3")
    
    # Add practice problem set link to week 4
    week04_pattern = r'(<a href="week04/case-study\.html"[^>]*>.*?</a>)'
    week04_replacement = r'<a href="docs/week04/practice-problem-set.html" class="material-link">\n                        <i class="fas fa-puzzle-piece material-icon"></i>\n                        <span>Practice Problem Set</span>\n                    </a>\n                    \1'
    
    if 'docs/week04/practice-problem-set.html' not in content:
        content = re.sub(week04_pattern, week04_replacement, content)
        print("Added Practice Problem Set link to Week 4")
    
    # Add problem set link to week 7
    week07_pattern = r'(<a href="week07/case-study\.html"[^>]*>.*?</a>)'
    week07_replacement = r'<a href="docs/week07/problem-set.html" class="material-link">\n                        <i class="fas fa-file-alt material-icon"></i>\n                        <span>Problem Set</span>\n                    </a>\n                    \1'
    
    if 'docs/week07/problem-set.html' not in content:
        content = re.sub(week07_pattern, week07_replacement, content)
        print("Added Problem Set link to Week 7")
    
    # Add problem set link to week 12
    week12_pattern = r'(<a href="week12/solutions\.html"[^>]*>.*?</a>)'
    week12_replacement = r'<a href="docs/week12/problem-set.html" class="material-link">\n                        <i class="fas fa-file-alt material-icon"></i>\n                        <span>Problem Set</span>\n                    </a>\n                    \1'
    
    if 'docs/week12/problem-set.html' not in content:
        content = re.sub(week12_pattern, week12_replacement, content)
        print("Added Problem Set link to Week 12")
    
    # Save updated index.html
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("Index.html updated with missing problem set links!")

if __name__ == "__main__":
    add_missing_links()