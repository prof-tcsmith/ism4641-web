#!/bin/bash

echo "Copying rendered files to public repository..."

# Week 2
echo "Copying Week 2..."
cp "/home/tim/Workspace/teaching/4641f25/Week02-Control Flow and Data Structures - lists and dictionaries/Week02-lecture-notes.html" docs/week02/lecture-notes.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week02-Control Flow and Data Structures - lists and dictionaries/Week02-lecture-notes_files" docs/week02/
cp "/home/tim/Workspace/teaching/4641f25/Week02-Control Flow and Data Structures - lists and dictionaries/Week02-problem-set.html" docs/week02/problem-set.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week02-Control Flow and Data Structures - lists and dictionaries/Week02-problem-set_files" docs/week02/

# Week 3
echo "Copying Week 3..."
cp "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-lecture-notes.html" docs/week03/lecture-notes.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-lecture-notes_files" docs/week03/
cp "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-problem-set.html" docs/week03/problem-set.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-problem-set_files" docs/week03/
cp "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-problem-set-solutions.html" docs/week03/problem-set-solutions.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week03-Data Structures  - Tuples and Sets/Week03-problem-set-solutions_files" docs/week03/

# Week 4
echo "Copying Week 4..."
cp "/home/tim/Workspace/teaching/4641f25/Week04-Functions and Modules/week4-lecture-notes.html" docs/week04/lecture-notes.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week04-Functions and Modules/week4-lecture-notes_files" docs/week04/
cp "/home/tim/Workspace/teaching/4641f25/Week04-Functions and Modules/week4-practice-problem-set.html" docs/week04/practice-problem-set.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week04-Functions and Modules/week4-practice-problem-set_files" docs/week04/

# Week 5
echo "Copying Week 5..."
cp "/home/tim/Workspace/teaching/4641f25/Week05-Numpy/week5-lecture-notes.html" docs/week05/lecture-notes.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week05-Numpy/week5-lecture-notes_files" docs/week05/

# Week 7 (named week6-problem-set but goes to week07)
echo "Copying Week 7..."
cp "/home/tim/Workspace/teaching/4641f25/Week07-Pandas/week6-problem-set.html" docs/week07/problem-set.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week07-Pandas/week6-problem-set_files" docs/week07/

# Week 8 (named week09-lecture-notes but goes to week08)
echo "Copying Week 8..."
cp "/home/tim/Workspace/teaching/4641f25/Week08-Matplotlib/week09-lecture-notes.html" docs/week08/lecture-notes.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week08-Matplotlib/week09-lecture-notes_files" docs/week08/

# Week 12
echo "Copying Week 12..."
cp "/home/tim/Workspace/teaching/4641f25/Week12-LogisticRegression/week12-problem-set.html" docs/week12/problem-set.html
cp -r "/home/tim/Workspace/teaching/4641f25/Week12-LogisticRegression/week12-problem-set_files" docs/week12/

echo "All files copied successfully!"