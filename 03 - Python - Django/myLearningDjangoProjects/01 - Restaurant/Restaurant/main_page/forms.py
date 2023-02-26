from django import forms
from .models import UserReservation, ContactUs


class ContactUsForm(forms.ModelForm):
    """
        Клас для створення форми "Зв'яжіться з нами"
    """

    name = forms.CharField(
        max_length=50,
        label="Ваше ім'я",
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Ваше ім'я",
        })
    )

    email = forms.CharField(
        max_length=63,
        label="Ваш E-Mail",
        widget=forms.TextInput(attrs={
            "type": "email",
            "name": "email",
            "class": "form-control",
            "id": "email",
            "placeholder": "Ваш E-Mail",
        })
    )

    subject = forms.CharField(
        max_length=100,
        label="Тема",
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "subject",
            "class": "form-control",
            "id": "subject",
            "placeholder": "Тема",
        })
    )

    message = forms.CharField(
        max_length=250,
        label="Повідомлення",
        widget=forms.Textarea(attrs={
            "name": "message",
            "type": "message",
            "class": "form-control",
            "rows": "5",
            "placeholder": "Повідомлення",
        })
    )

    class Meta:
        model = ContactUs
        fields = ("name", "email", "subject", "message")


class UserReservationForm(forms.ModelForm):
    """
        Клас для створення коректної форми "Бронювання користувачів"
    """

    name = forms.CharField(
        max_length=50,
        label="Ім'я",
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Ваше ім'я.",
            "data-rule": "minlen:4",
            "data-msg": "Введіть принаймні 4 символи"
        })
    )

    email = forms.CharField(
        max_length=63,
        label="E-Mail",
        widget=forms.TextInput(attrs={
            "type": "email",
            "name": "email",
            "class": "form-control",
            "id": "email",
            "placeholder": "Ваш E-Mail",
            "data-rule": "email",
            "data-msg": "Введіть дійсний E-Mail"
        })
    )

    phone = forms.CharField(
        max_length=15,
        label="Телефон",
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "phone",
            "class": "form-control",
            "id": "phone",
            "placeholder": "Ваш телефон.",
            "data-rule": "minlen:4",
            "data-msg": "Введіть не менше 10 символів"
        })
    )

    date_reservation = forms.CharField(
        label="Дата",
        widget=forms.DateInput(attrs={
            "type": "text",
            "name": "date",
            "class": "form-control",
            "id": "date",
            "placeholder": "Дата",
            "data-rule": "minlen:4",
            "data-msg": "Введіть не менше 4 символів"
        })
    )

    time_reservation = forms.CharField(
        label="Час",
        widget=forms.TimeInput(attrs={
            "type": "text",
            "name": "time",
            "class": "form-control",
            "id": "time",
            "placeholder": "Час",
            "data-rule": "minlen:4",
            "data-msg": "Введіть не менше 4 символів"
        })
    )

    persons = forms.CharField(
        max_length=15,
        label="Кількість осіб",
        widget=forms.NumberInput(attrs={
            "type": "number",
            "name": "people",
            "class": "form-control",
            "id": "people",
            "placeholder": "Кількість осіб",
            "data-rule": "minlen:1",
            "data-msg": "Введіть хоча б 1 символ"
        })
    )

    message = forms.CharField(
        max_length=250,
        label="Повідомлення",
        widget=forms.Textarea(attrs={
            "name": "message",
            "type": "message",
            "class": "form-control",
            "rows": "5",
            "placeholder": "Повідомлення",
        })
    )

    class Meta:
        model = UserReservation
        fields = ("name", "email", "phone", "date_reservation", "time_reservation", "persons", "message")
