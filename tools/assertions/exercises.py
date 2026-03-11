from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными созданного упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, 'title')
    assert_equal(request.course_id, response.exercise.course_id, 'course_id')
    assert_equal(request.max_score, response.exercise.max_score, 'max_score')
    assert_equal(request.min_score, response.exercise.min_score, 'min_score')
    assert_equal(request.order_index, response.exercise.order_index, 'order_index')
    assert_equal(request.description, response.exercise.description, 'description')
    assert_equal(request.estimated_time, response.exercise.estimated_time, 'estimated_time')
