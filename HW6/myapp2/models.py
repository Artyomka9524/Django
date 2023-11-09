from django.db import models



class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)                      # сторона монетки (орел или решка)
    create_at = models.DateTimeField(auto_now_add=True)             #время броска запоминает

    def __str__(self):
        return f'Сторона: {self.is_eagle}, время: {self.create_at}'

    @staticmethod                       # статический метод работатет без создания экземпляра класса а просто вызываетс
    # получение  n последних результатов бросков монетки и подсчет кол решек и орлов
    def counter(n: int):
        #coins = Coin.object.all()    # в переменную записывается весь список оюъектов Coin - это вариант с начала броска
        coins = Coin.objects.order_by('-create_at')[: n]   # обрезание списка, order_by('-create_at') - сортировка по времени в обратном порядке, [: n] - обрезание по n
        coins_dict = {'орел': 0, 'решка': 0}
        for coin in coins:
            if coin.is_eagle == 'орел':
                coins_dict['орел'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict


# таблица  автор для блога
class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    # метод для возвращения имени и фамилии
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

# таблица статья для блога
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)                        # присваивается автоматически
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)                            # количество просмогтров
    is_published = models.BooleanField(default=False)                   #стапья не опубликована по умолчанию is_published= False


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
