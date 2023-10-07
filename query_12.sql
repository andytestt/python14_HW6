WITH LastClass AS (
    SELECT MAX(date_taken) AS last_date
    FROM grades
    WHERE subject_id = 1
)

SELECT students.first_name, students.last_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN LastClass ON grades.date_taken = LastClass.last_date
WHERE students.group_id = 1 AND subjects.id = 1;