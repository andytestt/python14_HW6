SELECT students.id, students.first_name, students.last_name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.first_name, students.last_name
ORDER BY avg_grade DESC
LIMIT 5;
