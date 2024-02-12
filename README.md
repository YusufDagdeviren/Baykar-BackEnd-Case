# Django Rest API Projesi

## Giriş

Bu proje, Django ve Django Rest Framework kullanılarak geliştirilmiş bir RESTful API sunucusudur. Projede kullanıcı kayıt, giriş,  İHA (İnsan Hava Araçları) listesi, kiralama işlemleri ve kullanıcı detayları gibi işlemler gerçekleştirilebilir.

## Kurulum

Projeyi kurmak ve  çalıştırmak için aşağıdaki adımları izleyin:

1. Python  3.x ve pip (Python paket yöneticisi) kurulu olduğundan emin olun.
2. Proje dizinine gidin ve gerekli Python paketlerini yüklemek için `pip install -r requirements.txt` komutunu  çalıştırın.
3. `.env` dosyasını oluşturun ve gerekli ortam değişkenlerini (`SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`) ekleyin.
4. Veritabanınızı oluşturun ve Django modelinizi uygun  şekilde güncelleyin.
5. Veritabanı migrasyonlarını uygulamak için `python manage.py migrate` komutunu  çalıştırın.
6. Sunucuyu başlatmak için `python manage.py runserver` komutunu  çalıştırın.

## Kullanılan Teknolojiler

- **Django**: Web framework ve ORM (Object-Relational Mapping) kütüphanesi.
- **Django Rest Framework**: Django için RESTful API oluşturmak üzere tasarlanmış bir kütüphane.
- **Simple JWT**: Django Rest Framework için JSON Web Token (JWT) desteği sağlayan bir kütüphane.
- **PostgreSQL**: Veritabanı sistemi.
- **environ**: Ortam değişkenlerini yönetmek için kullanılan bir kütüphane.

## Endpointler

Projedeki kullanılabilir endpointler ve bu endpointlerin ne yaptığına dair bilgiler burada belirtilecektir. Örneğin:

- `/api/login`: Kullanıcı girişi için kullanılır.
- `/api/register`: Yeni bir kullanıcı kaydı oluşturmak için kullanılır.
- `/api/refresh`: Eski bir JWT tokenunu yenilemek için kullanılır.
- `/api/iha`:  İHA listesi için kullanılır.
- `/api/iha/{id}`: Belirli bir  İHA'yı almak, güncellemek veya silmek için kullanılır.
- `/api/kiralama`: Kiralama işlemleri için kullanılır.
- `/api/kiralama/{id}`: Belirli bir kiralama işlemi için kullanılır.
- `/api/kullanicidetay`: Kullanıcı detayları için kullanılır.
- `/api/kullanicidetay/{id}`: Belirli bir kullanıcı detayı için kullanılır.

## Filtreleme

Projede, `Kiralama` modeli için filtreleme özellikleri bulunmaktadır. Filtreleme için aşağıdaki parametreler kullanılabilir:

- `iha_id`:  İHA ID'si ile filtreleme yapılabilir.
- `kiralayan_uye`: Kiralayan kullanıcının kullanıcı adı ile filtreleme yapılabilir.
- `baslangic_tarihi_gte`: Başlangıç tarihinin belirtilen tarihten sonraki tarihlere sahip kiralamaları filtrelemek için kullanılır.
- `baslangic_tarihi_lte`: Başlangıç tarihinin belirtilen tarihten  önceki tarihlere sahip kiralamaları filtrelemek için kullanılır.
