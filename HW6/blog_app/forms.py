from django import forms
from .models import Comment


class AddAuthorForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Your name"}),
    )
    surname = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Your surname"}),
    )
    email = forms.EmailField(
        label=False, widget=forms.EmailInput(attrs={"placeholder": "Your email"})
    )
    biography = forms.CharField(
        label=False, widget=forms.Textarea(attrs={"placeholder": "Your biography"})
    )
    birthday = forms.DateField(
        label=False,
        widget=forms.DateInput(attrs={"type": "date", "placeholder": "dd.mm.yyyy"}),
    )

# другой способ создания class AddAuthorForm, когда нужно все поля формы подтягиваются   как поля модели , изменения поля(например виджеты) прописываем перед Meta
# from .models import Author  # импортируем модель автора
# class AddAuthorForm(forms.ModelForm):
# birthday = forms.DateField(widget=forms.DateInput(attrs={"type":"data"}))
#     class Meta:
#         model = Author
#         fields = ['name', 'surname', 'email', 'biography', 'birthday']


class ArticleForm(forms.Form):
    title = forms.CharField(
        label=False,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Title"}),
    )
    content = forms.CharField(
        label=False, widget=forms.Textarea(attrs={"placeholder": "Content"})
    )
    publication_date = forms.DateField(
        label=False,
        widget=forms.DateInput(attrs={"type": "date", "placeholder": "dd.mm.yyyy"}),
    )
    author = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Author's name"}),
    )
    category = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Category"}),
    )
    is_published = forms.BooleanField(
        required=False,
        label="Published?",
        widget=forms.CheckboxInput(attrs={"placeholder": "Published?"}),
    )


class AddCommentForm(forms.Form):
    class Meta:
        model = Comment

    fields = ["author", "comment"]

    author = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Your name"}),
    )
    comment = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={"placeholder": "Add your comment here"}),
    )
