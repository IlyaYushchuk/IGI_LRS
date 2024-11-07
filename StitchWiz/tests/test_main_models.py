from django.test import TestCase

from main_page.models import News, Question, Vacancy, Review, Coupon
from django.utils import timezone

class NewsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        News.objects.create(title='Head', text='text of new')

    def test_title_label(self):
        new=News.objects.get(id=1)
        field_label = new._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Заголовок')

    def test_text_label(self):
        new=News.objects.get(id=1)
        field_label = new._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Текст новости')

    def test_image_label(self):
        new=News.objects.get(id=1)
        field_label = new._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'Изображение')

    def test_title_max_length(self):
        new=News.objects.get(id=1)
        field_label = new._meta.get_field('title').max_length
        self.assertEqual(field_label, 200)


    def test_text_max_length(self):
        new=News.objects.get(id=1)
        field_label = new._meta.get_field('text').max_length
        self.assertEqual(field_label, 2000)

    def test_str(self):
        new=News.objects.get(id=1)
        self.assertEqual(str(new), 'Head')

class VacancyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Vacancy.objects.create(position='Cleaner', some_info='Clean rooms', salary=1234, city='Minsk')

    def test_position_label(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'Должность')

    def test_salary_label(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('salary').verbose_name
        self.assertEqual(field_label, 'Заработная плата')

    def test_some_info_label(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('some_info').verbose_name
        self.assertEqual(field_label, 'Описание должности')

    def test_city_label(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'Город')

    def test_position_max_length(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('position').max_length
        self.assertEqual(field_label, 200)

    def test_some_info_max_length(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('some_info').max_length
        self.assertEqual(field_label, 1000)

    def test_city_max_length(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('city').max_length
        self.assertEqual(field_label, 30)

    def test_salary_default(self):
        vacancy=Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('salary').default
        self.assertEqual(field_label, 0)

    def test_str(self):
        vacancy=Vacancy.objects.get(id=1)
        self.assertEqual(str(vacancy), 'Director')

class CouponModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Coupon.objects.create(title='Coupon example', some_info='Coupon example info', discount=30, date=timezone.now(), code ='123')

    def test_title_label(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Название')

    def test_some_info_label(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('some_info').verbose_name
        self.assertEqual(field_label, 'Описание купона')
    
    def test_code_label(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'Код')

    def test_date_label(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'Дата окончания')

    def test_discount_label(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('discount').verbose_name
        self.assertEqual(field_label, 'Скидка в %')

    def test_title_max_length(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('title').max_length
        self.assertEqual(field_label, 200)

    def test_some_info_max_length(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('some_info').max_length
        self.assertEqual(field_label, 1000)

    def test_discount_default(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('discount').default
        self.assertEqual(field_label, 0)
    
    def test_code_max_length(self):
        promotion=Coupon.objects.get(id=1)
        field_label = promotion._meta.get_field('code').default
        self.assertEqual(field_label, 50)

class QuestionModelTest(TestCase):
    def setUp(self):
        self.question_text = "Какой сегодня день?"
        self.answer_text = "Сегодня пятница."
        self.question = Question.objects.create(
            question=self.question_text,
            answer=self.answer_text,
            date=timezone.now()
        )

    def test_question_creation(self):
        """Тестирование создания объекта Question"""
        self.assertEqual(self.question.question, self.question_text)
        self.assertEqual(self.question.answer, self.answer_text)
        self.assertIsInstance(self.question.date, type(timezone.now()))
        
    def test_default_answer(self):
        """Тестирование значения по умолчанию для поля answer"""
        question_with_default_answer = Question.objects.create(
            question="Какое сегодня число?",
            date=timezone.now()
        )
        self.assertEqual(question_with_default_answer.answer, 'На этот вопрос пока нет ответа.')

    def test_unique_question(self):
        """Тестирование уникальности поля question"""
        with self.assertRaises(Exception):
            Question.objects.create(
                question=self.question_text,
                answer="Дублированный вопрос.",
                date=timezone.now()
            )

    def test_str_method(self):
        """Тестирование метода __str__"""
        self.assertEqual(str(self.question), self.question_text)

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.review_text = "Отличный продукт!"
        self.rating = 5
        self.review = Review.objects.create(
            text=self.review_text,
            rating=self.rating,
            date=timezone.now(),
            user=self.user
        )

    def test_review_creation(self):
        """Тестирование создания объекта Review"""
        self.assertEqual(self.review.text, self.review_text)
        self.assertEqual(self.review.rating, self.rating)
        self.assertIsInstance(self.review.date, type(timezone.now()))
        self.assertEqual(self.review.user, self.user)

    def test_default_rating(self):
        """Тестирование значения по умолчанию для поля rating"""
        review_with_default_rating = Review.objects.create(
            text="Хороший продукт.",
            date=timezone.now(),
            user=self.user
        )
        self.assertEqual(review_with_default_rating.rating, 5)

    def test_str_method(self):
        """Тестирование метода __str__"""
        self.assertEqual(str(self.review), self.review_text)