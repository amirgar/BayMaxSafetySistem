**Причина создания данного проекта.** 
Большинство преступлений, связанных с переводом денег на карты мошенников, происходят через банкоматы. Люди (особенно пожилые люди), слишком сильно доверяют мошенникам, что приводит к необратимым последствиям для жертвы. Такой человек может, к примеру, 
может всю жизнь откладывать в сумме около 3 миллионов на пенсию, и лишится их в один миг, послушав незнакомца и переведя деньги на незнакомый номер. Да, данная технология в банкоматах все равно не сможет предотвратить абсолютно все преступления мошенников, 
но точно может предотвратить какой-то определенный процент преступлений. 

**Как будет все работать?** 
1. Человек проходит регистрацию/вход в аккаунт
2. При успешном входе в аккаунт он выбирает тип операции
3. В момент когда он вводит данные, камера три раза фоткает его
4. Далее после отправки запроса о получении денег/кредита и тп. ИИ обрабатывает все фотографии, определяет настроение поьзователя и его возраст
5. Если система посяитает, что человек находится в состоянии испуга/злости или его возраст больше 55 лет, то тогда она выведет сообщение оповещение о возможной угрозе
6. Если человек согласиться перейти по сообщению, то ему откроется сайт-мессенджер с админом, где админ может, если будет необходимо, решить все проблемы связанные с различными финансовыми махинациями.
7. В конце либо операция отменяется, либо либо издается звук об успешной оплате и выполняется небольшая работа Arduino(для демонстрации макета, доказательство того что вске работает)
Также у админа есть собственный интерфейс - это мессенджер (на данный момент его можно запускать только локально), и телеграмм бот - @baymax_safety_system_bot. Его функционал будет описан ниже

**Используемые технологии** 
Для работы с Arduino использовался язык программирования C++. В остальном, был задействован Python. Для создания интерфейсов приложений использовалась библиотека PyQt5, 
для регистрации данных ользователя в базе данных - SQLite3, для определения лица (Face ID) - face_recognition, для определения эмоций человека - DeepFace, для получения фотографий с камеры - OpenCV, 
для создания чата с админом - pywebio, для создания админского тг бота - aiogram. Также было взаимодействовано много менее важных библиотек, на которых я останавливаться не буду. Полный список 
можно найти в файле requiremets.txt 

**Что есть в телеграмм боте?** 
Телеграмм бот предназначен для того, чтобы админу получать информацию о пользователе банкомата. Использовав необходимые команды, можно олучить фотографии человека, информацию о его банковской карте и тп. 
![ыы](https://github.com/amirgar/BayMaxSafetySistem/assets/81811152/fb4079d0-0f1e-4193-b8da-e0623d737dc1)
![вв](https://github.com/amirgar/BayMaxSafetySistem/assets/81811152/c9fd6069-77d2-461d-ad10-2a9ffb356bb4)

**Видео демонстрация работы приложения**
Ссылка на Google Диск - https://drive.google.com/file/d/1se_vj4-0hR_YknHW1DipvOY1Z1nyFdAZ/view?usp=sharing

**Планы** 
Планируется дальше развиваться в плане создания макета банкомата. Также планируется поработать с конфедециальностью пользователей, так как в данном проекте используются не только данные карточек, но и биометрия человека
