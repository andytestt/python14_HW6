SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 1 AND subjects.professor_id = 1;