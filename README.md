Run this command to clone this repository: 
```
git clone https://github.com/amirgar/BayMaxSafetySistem.git
```
##### 1. Introduction
By the [statics from RBK](https://www.rbc.ru/life/news/67c701169a79471c14b76fa5) (on of the most influential media in the Russia), in 2024, scammers stole more than 295 billion rubles by the internet. This number is equal with budget of my native republic (Russia, Tatarstan).
I think, that you usually hear on TV news about problem of internet scammers. Unfortunatelly, this problem can affect all of us, so I think, nowadays this problem potentionaly is on of the most important.

I know, that it is absurdly to solve this problem by the harassmenting them in internet, because they can hide themself by powerful encryption technologies. However, I assumbed, that banks can prevent part of those transctions by ATM machines. We can implement AI technologies in ATM machine, and if behavior of user is strange, ATM machine and AI will block this transaction. Of course, this solution of problem can't solve all problem with internet scammers, but it can solve some parts of this issue.  
##### 2. Used technologies
When i has created this project, I were using two programming languages: Python and C++. C++ was used for Arduino, Python was used for GUI and AI. 
So, let's talk about Python modules, that were used in this project. 
1) PyQT5 was used for GUI
2) SQLite3 was used for saving user data in database
3) FaceRecognition was used for detecting user's face
4) DeepFace was used for detecting user's emotions
5) OpenCV was used for communication of code with camera
6) PyWebIo was used for creating a chat of user with administrator
7) Aiogram was used for creating a Telegram Bot
##### 3. Realisation
![Scheme of project (on Russian)](project_scheme.PNG "Scheme of project (on Russian)") 
##### 4. Creating virtual enviroment (venv), installing libraries and modules 
Run this command to create virtual enviroment in your cmd: 
```
python3 -m venv venv
```
Then run this command to activate venv: 
```
venv\Scripts\activate
```
Run this command to install libraries from ***requirements.txt***:
```
pip install -r requiremenets.txt
```
