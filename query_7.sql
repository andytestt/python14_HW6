SELECT students.first_name, students.last_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 1;