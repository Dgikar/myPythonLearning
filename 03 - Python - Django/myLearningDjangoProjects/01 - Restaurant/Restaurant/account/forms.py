from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserRegistration(forms.ModelForm):
    """
        Цей клас є формою UserRegistration для створення нового користувача. Вона має поля:
            username - ім'я користувача,
            password - пароль,
            password2 - пароля2 (для підтвердження пароля).
    """

    class Meta:
        """
            Цей клас Meta використовується для визначення інформації про модель.
                У моделі є User, а атрибут fields визначає поле імені користувача. Це дозволяє користувачеві отримати
                доступ до поля імені користувача для моделі User.
        """

        model = User
        fields = ('username',)

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        """
            Метод clean_password2 використовується для перевірки збігу двох паролів, і якщо вони не збігаються, то
                згенерується ValidationError.
        """

        data = self.cleaned_data

        if data.get('password') == data.get('password2'):
            return data['password2']
        raise forms.ValidationError('Помилка в паролі')


class UserLogin(forms.Form):
    """
        Цей клас використовується для створення форми входу користувача. Він містить два поля:
            username : TextInput - ім'я користувача
            password : PasswordInput - пароль,
    """

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        """
            Метод clean використовується для аутентифікації облікових даних користувача і перевірки їхньої дійсності.
            Якщо облікові дані недійсні, буде видано помилку валідації.
        """

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user or not user.check_password(password):
                raise forms.ValidationError('Помилка в логіні або паролі')
        else:

            raise forms.ValidationError('Помилка в логіні або паролі')
        return super().clean()
