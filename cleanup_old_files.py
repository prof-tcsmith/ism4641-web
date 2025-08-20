#!/usr/bin/env python3
"""
Clean up old files that have been replaced by new versions in docs/ folder.
Only removes files that we've already moved to docs/ and verified work.
"""

import os
import glob

# Files that have been moved to docs/ and can be safely removed from old locations
files_to_remove = [
    # Week 2 - we have new versions in docs/week02/
    'week02/lecture-notes.html',
    'week02/Week02-lecture-notes_files/',
    'week02/problem-set-solutions.html',
    'week02/Week02-problem-set-solutions_files/',
    
    # Week 3 - we have new versions in docs/week03/
    'week03/problem-set.html', 
    'week03/Week03-problem-set_files/',
    'week03/problem-set-solutions.html',
    'week03/Week03-problem-set-solutions_files/',
    
    # Week 4 - we have new versions in docs/week04/
    # Note: old week04/lecture-notes.html might be different from new docs version
    
    # Week 5 - we have new versions in docs/week05/
    # Note: old week05/lecture-notes.html might be different from new docs version
    
    # Week 7 - we have new version in docs/week07/
    # Note: keeping old week07/lecture-notes.html since it might be different
    
    # Week 8 - we have new version in docs/week08/
    # Note: keeping old week08/lecture-notes.html since it might be different
]

def safe_remove(path):
    """Safely remove a file or directory."""
    if os.path.isfile(path):
        print(f"Removing file: {path}")
        os.remove(path)
        return True
    elif os.path.isdir(path):
        print(f"Removing directory: {path}")
        import shutil
        shutil.rmtree(path)
        return True
    else:
        print(f"Path not found (already removed?): {path}")
        return False

def main():
    """Clean up old files."""
    removed_count = 0
    
    for item in files_to_remove:
        if safe_remove(item):
            removed_count += 1
    
    print(f"\nCleaned up {removed_count} old files/directories")
    print("Note: Kept most files as they are still referenced in index.html")

if __name__ == "__main__":
    main()