# scrapper-project
Book scrapper with BeautifulSoap and MongoDB

# KURULUM
Kurulum için bilgisayarınızda Docker bulunmalıdır.
- Docker'ı çalıştırın
- mongodb klasörü içerisinde bir terminal açın ve `docker-compose up` komutunu çalıştırın
internet hızınıza bağlı olarak 3 dakika içerisinde sistem hazır olacak.

# KULLANIM
- Kurulum kısmından sonra, scrappers adlı klasöre gidin. `.py` uzantılı dosyaları IDE'nizde çalıştırın.
- Kazınan veriler console'a yazılacaktır.
- Veriler kazındıktan sonra, `docker-compose.yml`'da belirtildiği üzere ./mongodb/database-data:/data/db şeklinde saklanacaktır.

# MONGODB'ye erişim
- pymongo kütüphanesi arayıcılığı ile mongodb://root:password@localhost:27017 adresine bağlanarak mongodb içeriğini görüntüleyebilirsiniz.
- Herhangi bir veri kazımadığınızda db boş olacaktır.

# Kullanılan teknolojiler
- Docker
- Python MongoDB Image
- docker-compose
- Python Libraries and Frameworks
  - requests
  - bs4
  - pandas
  - pymongo
