1. Запускаем Flask приложение
2. Вводим любой логин
3. Добавляем клиента в OAuth2:
   ```json
   {
       "client_name": "alice",
       "client_uri": "",
       "scope": "smart_home",
       "redirect_uris": [
           "https://social.yandex.net/broker/redirect"
       ],
       "grant_types": [
           "authorization_code",
           "password"
       ],
       "response_types":[
           "code"
       ],
       "token_endpoint_auth_method": "client_secret_post"
   }
   ```
   
   Получим что-то такое:
   ```
   Client Info client_id: 15fnOuPbZK7jHAx6JyFWyniP client_secret: qO8pztPglYvXrwQtQqjjYgJmCc1Qean9ChYkf5ZuFFirFiBC
   client_id_issued_at: 1725831511 client_secret_expires_at: 0 Client Metadata client_name: alice
   client_uri: grant_types: ['authorization_code', 'password']
   redirect_uris: ['https://social.yandex.net/broker/redirect']
   response_types: ['code'] scope: smart_home token_endpoint_auth_method: client_secret_post
   ```
   
4. Если отлаживаем локально (без белого IP), то используем например ngrok для проксирования.
   ```shell
   $ ngrok http 5000
   ```
   Получим что-то такое:
   ```shell
   ngrok                                                                                                         (Ctrl+C to quit)
   
   Policy Management Examples http://ngrok.com/apigwexamples
   
   Session Status                online
   Account                       Alexander Kovalev (Plan: Free)
   Update                        update available (version 3.15.1, Ctrl-U to update)
   Version                       3.3.4
   Region                        Europe (eu)
   Latency                       39ms
   Web Interface                 http://127.0.0.1:4040
   Forwarding                    https://791b-2a02-2168-8a19-c500-d808-cd72-5396-5eb3.ngrok-free.app -> http://localhost:5000
   
   Connections                   ttl     opn     rt1     rt5     p50     p90
                                 58      0       0.00    0.00    5.99    179.27
   
   HTTP Requests
   -------------
   ```

5. Идем в https://dialogs.yandex.ru/developer/
6. Создаем новый диалог - умный дом
7. В настройках:
   - Backend: Endpoint URL: https://791b-2a02-2168-8a19-c500-d808-cd72-5396-5eb3.ngrok-free.app/api
8. Связка аккаунтов:
   - Идентификатор приложения: 15fnOuPbZK7jHAx6JyFWyniP
   - Секрет приложения: qO8pztPglYvXrwQtQqjjYgJmCc1Qean9ChYkf5ZuFFirFiBC
   - URL авторизации: https://791b-2a02-2168-8a19-c500-d808-cd72-5396-5eb3.ngrok-free.app/oauth/authorize
   - URL для получения токена: https://791b-2a02-2168-8a19-c500-d808-cd72-5396-5eb3.ngrok-free.app/oauth/token
   - URL для обновления токена: https://791b-2a02-2168-8a19-c500-d808-cd72-5396-5eb3.ngrok-free.app/oauth/token
   - Идентификатор группы действий: smart_home
9. Вкладка "Тестирование" (эмулятор мобильного приложения)
10. Кнопка "+" справа вверху
11. Большая кнопка сверху "Устройство умного дома"
12. Если не появится сразу, то нажимаем кнопку "Обновить список устройств"
13. Дальше появляется настройка нового устройства