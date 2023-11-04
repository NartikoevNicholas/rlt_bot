
# Telegram-bot  
## Описание  
  
Вашей задачей в рамках этого тестового задания будет написание алгоритма агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам. Ссылка на скачивание коллекции со статистическими данными, которую необходимо использовать при выполнении задания, находится в конце документа.  
  
**Ваш алгоритм должен принимать на вход:**  
	{
	"dt_from":"2022-09-01T00:00:00",
	"dt_upto":"2022-11-30T23:59:00",
	"group_type":"month"
	}
	
  **На выходе ваш алгоритм формирует ответ содержащий:**
	{
	'dataset': [5906586, 5515874, 5889803],
	 'labels': ['2022-09-01T00:00:00', '2022-10-01T00:00:00', '2022-11-01T00:00:00']
	 }

**Комментарий к ответу: **
В нулевом элементе датасета содержится сумма всех выплат за сентябрь, в первом
элементе сумма всех выплат за октябрь и т.д. В лейблах подписи соответственно
элементам датасета.

После разработки алгоритма агрегации, вам необходимо создать телеграм бота, который будет принимать от пользователей текстовые сообщения содержащие JSON с входными данными и отдавать агрегированные данные в ответ. Посмотрите @rlt_testtaskexample_bot - в таком формате должен работать и ваш бот.

**Коллекция со статистическими данными**
https://drive.google.com/file/d/1pcNm2TAtXHO4JIad9dkzpbNc4q7NoYkx/view?usp=sharing

## Работа с приложением  
  
### Требования  
  
Необходимо, чтобы были установлены следующие компоненты:  
  
- `Docker` и `docker-compose`   
  
### Установка и запуск(linux)  
1. Создание виртуального окружения. Прописать в командной строке:
`cp .env.example .env` 
и в файле .env указать свой `TELEGRAM_TOKEN=` 
2. Поднять docker-compose.  Прописать в командной строке:
`docker-compose -f docker-compose.yml up -d --remove-orphans`
3. Импортировать дамп базы данных. Проприсать в командной строке:
`docker exec -i mongodb /usr/bin/mongorestore --uri "mongodb://test:test@mongodb:27017/test" --drop /var/backups/sampleDB`
  
## Реализация
Проект реализовал на языке Python. Проект расположен в папке src. 
При реализации проекта использовал паттерн clean architecture.

