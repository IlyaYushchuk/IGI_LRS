import calendar
from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse
import pytz
import tzlocal

from main_page.forms import ReviewForm
from main_page.models import News, Vacancy, Coupon, Review
from django.utils import timezone
from goods.models import Products, Categories, Order
from users.models import User


class ProcessingOrdersTest(TestCase):
    def setUp(self):
        # Создаем клиентов
        self.client = Client()

        # Создаем пользователей
        self.master_user = User.objects.create_user(username='master', password='password', is_master=True)
        self.regular_user = User.objects.create_user(username='user', password='password', is_master=False)

        # Создаем заказы для мастера
        self.order1 = Order.objects.create(user=self.regular_user, master=self.master_user, is_processing=True, date_order=timezone.now())
        self.order2 = Order.objects.create(user=self.regular_user, master=self.master_user, is_processing=True, date_order=timezone.now())

        # Создаем заказы для обычного пользователя
        self.order3 = Order.objects.create(user=self.regular_user, master=self.master_user, is_processing=True, date_order=timezone.now())
        self.order4 = Order.objects.create(user=self.regular_user, master=self.master_user, is_processing=True, date_order=timezone.now())

    def test_processing_orders_for_master(self):
        """Тестирование обработки заказов для пользователя-мастера"""
        self.client.login(username='master', password='password')
        response = self.client.get(reverse('processing_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.master, self.master_user)

    def test_processing_orders_for_regular_user(self):
        """Тестирование обработки заказов для обычного пользователя"""
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('processing_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.user, self.regular_user)

class ReleasedOrdersTest(TestCase):
    def setUp(self):
        # Создаем клиентов
        self.client = Client()

        # Создаем пользователей
        self.master_user = User.objects.create_user(username='master', password='password', is_master=True)
        self.regular_user = User.objects.create_user(username='user', password='password', is_master=False)

        # Создаем заказы для мастера
        self.order1 = Order.objects.create(user=self.regular_user, master=self.master_user, is_released=True, date_order=timezone.now())
        self.order2 = Order.objects.create(user=self.regular_user, master=self.master_user, is_released=True, date_order=timezone.now())

        # Создаем заказы для обычного пользователя
        self.order3 = Order.objects.create(user=self.regular_user, master=self.master_user, is_released=True, date_order=timezone.now())
        self.order4 = Order.objects.create(user=self.regular_user, master=self.master_user, is_released=True, date_order=timezone.now())

    def test_released_orders_for_master(self):
        """Тестирование готовых заказов для пользователя-мастера"""
        self.client.login(username='master', password='password')
        response = self.client.get(reverse('released_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.master, self.master_user)
            self.assertTrue(order.is_released)

    def test_released_orders_for_regular_user(self):
        """Тестирование готовых заказов для обычного пользователя"""
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('released_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.user, self.regular_user)
            self.assertTrue(order.is_released)

class CanceledOrdersTest(TestCase):
    def setUp(self):
        # Создаем клиентов
        self.client = Client()

        # Создаем пользователей
        self.master_user = User.objects.create_user(username='master', password='password', is_master=True)
        self.regular_user = User.objects.create_user(username='user', password='password', is_master=False)

        # Создаем отмененные заказы для мастера
        self.order1 = Order.objects.create(user=self.regular_user, master=self.master_user, is_canceled=True, date_order=timezone.now())
        self.order2 = Order.objects.create(user=self.regular_user, master=self.master_user, is_canceled=True, date_order=timezone.now())

        # Создаем отмененные заказы для обычного пользователя
        self.order3 = Order.objects.create(user=self.regular_user, master=self.master_user, is_canceled=True, date_order=timezone.now())
        self.order4 = Order.objects.create(user=self.regular_user, master=self.master_user, is_canceled=True, date_order=timezone.now())

    def test_canceled_orders_for_master(self):
        """Тестирование отмененных заказов для пользователя-мастера"""
        self.client.login(username='master', password='password')
        response = self.client.get(reverse('canceled_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.master, self.master_user)
            self.assertTrue(order.is_canceled)

    def test_canceled_orders_for_regular_user(self):
        """Тестирование отмененных заказов для обычного пользователя"""
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('canceled_orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 2)
        for order in response.context['orders']:
            self.assertEqual(order.user, self.regular_user)
            self.assertTrue(order.is_canceled)

class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_status_code(self):
        """Тестирование статуса кода для index view"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        """Тестирование использования правильного шаблона для index view"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_context_data(self):
        """Тестирование правильности данных контекста для index view"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['title'], 'Main')
        self.assertEqual(response.context['content'], 'Ремонт одежды и обуви StitchWiz')

class AddReviewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_add_review_get_request(self):
        """Тестирование GET запроса к add_review"""
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')
        self.assertIsInstance(response.context['form'], ReviewForm)

        local_zone = tzlocal.get_localzone()
        date = datetime.now()
        utc_date = date.astimezone(pytz.utc)
        c = calendar.HTMLCalendar()
        s = c.formatmonth(date.year, date.month)

        self.assertEqual(response.context['local_zone'], local_zone)
        self.assertEqual(response.context['date'].date(), date.date())
        self.assertEqual(response.context['utc_date'].date(), utc_date.date())
        self.assertEqual(response.context['calendar'], s)

    def test_add_review_post_request_valid_form(self):
        """Тестирование POST запроса с валидной формой к add_review"""
        form_data = {
            'text': 'Отличный сервис!',
            'rating': 5,
        }
        response = self.client.post(reverse('add_review'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Проверяем редирект
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.text, 'Отличный сервис!')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.user, self.user)

    def test_add_review_post_request_invalid_form(self):
        """Тестирование POST запроса с невалидной формой к add_review"""
        form_data = {
            'text': '',
            'rating': 5,
        }
        response = self.client.post(reverse('add_review'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')
        self.assertIsInstance(response.context['form'], ReviewForm)
        self.assertTrue(response.context['form'].errors)
        self.assertEqual(Review.objects.count(), 0)
