def round_scores(student_scores):
    
    round_score = []
    for student in student_scores:
        round_score.append(round(student))

    return round_score


def count_failed_students(student_scores):
    
    count=0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    
    above_threshold_students = []

    for student in student_scores:
        if student >= threshold:
            above_threshold_students.append(student)

    return above_threshold_students


def letter_grades(highest):
        
    return [
        41,
        int(41 + (highest - 40) * 0.25),
        int(41 + (highest - 40) * 0.50),
        int(41 + (highest - 40) * 0.75)
    ]


def student_ranking(student_scores, student_names):
    
    ranking = []
    student = 0

    while student < len(student_scores):
        ranking.append(f"{student+1}. {student_names[student]}: {student_scores[student]}")
        student += 1
    return ranking


def perfect_score(student_info):
    
    for student in student_info:
        if student[1] == 100:
            return student

    return []