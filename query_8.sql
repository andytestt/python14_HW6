SELECT professors.first_name, professors.last_name, AVG(grades.grade) as avg_grade
FROM professors
JOIN subjects ON professors.id = subjects.professor_id
JOIN grades ON subjects.id = grades.subject_id
GROUP BY professors.first_name, professors.last_name;